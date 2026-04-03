from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='admin')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(350), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(500))
    category = db.Column(db.String(50), nullable=False, default='News')
    subcategory = db.Column(db.String(50), default='Mumbai')
    author = db.Column(db.String(100), default='Staff Reporter')
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image_url = db.Column(db.String(500))
    is_featured = db.Column(db.Boolean, default=False)
    is_breaking = db.Column(db.Boolean, default=False)
    views = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='published')  # published, draft

    def __repr__(self):
        return f'<Article {self.title[:50]}>'

    def time_ago(self):
        now = datetime.utcnow()
        diff = now - self.publish_date
        seconds = diff.total_seconds()
        if seconds < 60:
            return "Just now"
        elif seconds < 3600:
            mins = int(seconds // 60)
            return f"{mins} minute{'s' if mins > 1 else ''} ago"
        elif seconds < 86400:
            hours = int(seconds // 3600)
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif seconds < 604800:
            days = int(seconds // 86400)
            return f"{days} day{'s' if days > 1 else ''} ago"
        else:
            return self.publish_date.strftime('%B %d, %Y')
