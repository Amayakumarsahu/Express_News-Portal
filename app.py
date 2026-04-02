from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from models import db, User, Article
from werkzeug.utils import secure_filename
import os
import re

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text


# ──────────────────────────────────────────
# PUBLIC ROUTES
# ──────────────────────────────────────────

@app.route('/')
def index():
    featured = Article.query.filter_by(is_featured=True, status='published').order_by(Article.publish_date.desc()).first()
    breaking = Article.query.filter_by(is_breaking=True, status='published').order_by(Article.publish_date.desc()).limit(5).all()
    top_stories = Article.query.filter_by(status='published').order_by(Article.publish_date.desc()).limit(8).all()
    trending = Article.query.filter_by(status='published').order_by(Article.views.desc()).limit(5).all()
    latest = Article.query.filter_by(status='published').order_by(Article.publish_date.desc()).limit(12).all()

    categories = db.session.query(Article.category).distinct().all()
    categories = [c[0] for c in categories]

    return render_template('index.html',
                           featured=featured,
                           breaking=breaking,
                           top_stories=top_stories,
                           trending=trending,
                           latest=latest,
                           categories=categories)


@app.route('/article/<slug>')
def article_detail(slug):
    article = Article.query.filter_by(slug=slug, status='published').first_or_404()
    article.views += 1
    db.session.commit()

    related = Article.query.filter(
        Article.category == article.category,
        Article.id != article.id,
        Article.status == 'published'
    ).order_by(Article.publish_date.desc()).limit(4).all()

    return render_template('article.html', article=article, related=related)


@app.route('/category/<category_name>')
def category_page(category_name):
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(
        category=category_name, status='published'
    ).order_by(Article.publish_date.desc()).paginate(
        page=page, per_page=app.config['ARTICLES_PER_PAGE'], error_out=False
    )
    return render_template('category.html', articles=articles, category=category_name)


@app.route('/search')
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    if query:
        results = Article.query.filter(
            Article.status == 'published',
            (Article.title.ilike(f'%{query}%')) | (Article.content.ilike(f'%{query}%'))
        ).order_by(Article.publish_date.desc()).paginate(
            page=page, per_page=app.config['ARTICLES_PER_PAGE'], error_out=False
        )
    else:
        results = None
    return render_template('search.html', results=results, query=query)


# ──────────────────────────────────────────
# REST API
# ──────────────────────────────────────────

@app.route('/api/articles')
def api_articles():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category', None)

    query = Article.query.filter_by(status='published')
    if category:
        query = query.filter_by(category=category)

    articles = query.order_by(Article.publish_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'articles': [{
            'id': a.id,
            'title': a.title,
            'slug': a.slug,
            'short_description': a.short_description,
            'category': a.category,
            'author': a.author,
            'publish_date': a.publish_date.isoformat(),
            'image_url': a.image_url,
            'time_ago': a.time_ago(),
            'views': a.views
        } for a in articles.items],
        'total': articles.total,
        'pages': articles.pages,
        'current_page': articles.page,
        'has_next': articles.has_next
    })


# ──────────────────────────────────────────
# ADMIN ROUTES
# ──────────────────────────────────────────

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('admin/login.html')


@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/admin')
@login_required
def admin_dashboard():
    articles = Article.query.order_by(Article.publish_date.desc()).all()
    total = Article.query.count()
    published = Article.query.filter_by(status='published').count()
    drafts = Article.query.filter_by(status='draft').count()
    return render_template('admin/dashboard.html',
                           articles=articles, total=total,
                           published=published, drafts=drafts)


@app.route('/admin/article/new', methods=['GET', 'POST'])
@login_required
def admin_new_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        short_description = request.form.get('short_description')
        category = request.form.get('category')
        author = request.form.get('author', 'Staff Reporter')
        is_featured = request.form.get('is_featured') == 'on'
        is_breaking = request.form.get('is_breaking') == 'on'
        status = request.form.get('status', 'published')

        slug = slugify(title)
        existing = Article.query.filter_by(slug=slug).first()
        if existing:
            slug = f"{slug}-{Article.query.count() + 1}"

        image_url = '/static/images/default-news.jpg'
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                filename = secure_filename(file.filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = f'/static/uploads/{filename}'

        article = Article(
            title=title, slug=slug, content=content,
            short_description=short_description, category=category,
            author=author, image_url=image_url,
            is_featured=is_featured, is_breaking=is_breaking,
            status=status
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/editor.html', article=None)


@app.route('/admin/article/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        article.short_description = request.form.get('short_description')
        article.category = request.form.get('category')
        article.author = request.form.get('author', 'Staff Reporter')
        article.is_featured = request.form.get('is_featured') == 'on'
        article.is_breaking = request.form.get('is_breaking') == 'on'
        article.status = request.form.get('status', 'published')

        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                filename = secure_filename(file.filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                article.image_url = f'/static/uploads/{filename}'

        db.session.commit()
        flash('Article updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/editor.html', article=article)


@app.route('/admin/article/delete/<int:article_id>', methods=['POST'])
@login_required
def admin_delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted.', 'info')
    return redirect(url_for('admin_dashboard'))


# ──────────────────────────────────────────
# CONTEXT PROCESSORS
# ──────────────────────────────────────────

@app.context_processor
def inject_globals():
    categories = db.session.query(Article.category).distinct().all()
    categories = [c[0] for c in categories]
    breaking_news = Article.query.filter_by(is_breaking=True, status='published').order_by(Article.publish_date.desc()).limit(5).all()
    return dict(all_categories=categories, breaking_news=breaking_news)


# ──────────────────────────────────────────
# INIT DB
# ──────────────────────────────────────────

with app.app_context():
    db.create_all()
    # Create default admin if none exists
    if not User.query.first():
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
