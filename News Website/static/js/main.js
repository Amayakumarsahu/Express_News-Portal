// ═══════════════════════════════════════════
// NEWS PORTAL — Main JavaScript
// ═══════════════════════════════════════════

document.addEventListener('DOMContentLoaded', function () {

    // ── Current Date ──
    const dateEl = document.getElementById('current-date');
    if (dateEl) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        dateEl.textContent = now.toLocaleDateString('en-IN', options);
    }

    // ── Hamburger Menu ──
    const hamburger = document.getElementById('hamburger');
    const mainNav = document.getElementById('main-nav');
    if (hamburger && mainNav) {
        hamburger.addEventListener('click', function () {
            hamburger.classList.toggle('active');
            mainNav.classList.toggle('active');
        });
    }

    // ── Search Overlay ──
    const searchToggle = document.getElementById('search-toggle');
    const searchOverlay = document.getElementById('search-overlay');
    const searchClose = document.getElementById('search-close');
    const searchInput = document.getElementById('search-input');

    if (searchToggle && searchOverlay) {
        searchToggle.addEventListener('click', function () {
            searchOverlay.classList.add('active');
            if (searchInput) setTimeout(() => searchInput.focus(), 300);
        });
    }
    if (searchClose && searchOverlay) {
        searchClose.addEventListener('click', function () {
            searchOverlay.classList.remove('active');
        });
    }
    if (searchOverlay) {
        searchOverlay.addEventListener('click', function (e) {
            if (e.target === searchOverlay) searchOverlay.classList.remove('active');
        });
    }

    // Close search on Escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && searchOverlay) {
            searchOverlay.classList.remove('active');
        }
    });

    // ── Load More (AJAX) ──
    const loadMoreBtn = document.getElementById('load-more-btn');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function () {
            const page = parseInt(this.dataset.page);
            const container = document.getElementById('latest-articles');

            loadMoreBtn.textContent = 'Loading...';
            loadMoreBtn.disabled = true;

            fetch(`/api/articles?page=${page}&per_page=6`)
                .then(res => res.json())
                .then(data => {
                    if (data.articles.length === 0) {
                        loadMoreBtn.textContent = 'No More Stories';
                        loadMoreBtn.disabled = true;
                        loadMoreBtn.style.opacity = '0.5';
                        return;
                    }

                    data.articles.forEach((article, i) => {
                        const card = document.createElement('a');
                        card.href = `/article/${article.slug}`;
                        card.className = 'article-card-horizontal animate-in';
                        card.style.animationDelay = `${i * 0.05}s`;

                        const fallbackImg = 'https://images.unsplash.com/photo-1504711434969-e33886168d5c?w=400&h=300&fit=crop';
                        const imgSrc = article.image_url || fallbackImg;

                        card.innerHTML = `
                            <div class="card-image">
                                <img src="${imgSrc}" alt="${article.title}" onerror="this.src='${fallbackImg}'">
                            </div>
                            <div class="card-body">
                                <h3>${article.title}</h3>
                                <p class="excerpt">${article.short_description || ''}</p>
                                <div class="card-meta">
                                    <span class="author">${article.author}</span>
                                    <span>${article.time_ago}</span>
                                    <span>${article.category}</span>
                                </div>
                            </div>
                        `;

                        container.appendChild(card);
                    });

                    if (data.has_next) {
                        loadMoreBtn.dataset.page = page + 1;
                        loadMoreBtn.textContent = 'Load More Stories';
                        loadMoreBtn.disabled = false;
                    } else {
                        loadMoreBtn.textContent = 'All Stories Loaded';
                        loadMoreBtn.disabled = true;
                        loadMoreBtn.style.opacity = '0.5';
                    }
                })
                .catch(err => {
                    console.error('Load more error:', err);
                    loadMoreBtn.textContent = 'Load More Stories';
                    loadMoreBtn.disabled = false;
                });
        });
    }

    // ── Flash message auto-dismiss ──
    const flashContainer = document.getElementById('flash-messages');
    if (flashContainer) {
        setTimeout(() => {
            flashContainer.querySelectorAll('.flash').forEach(el => {
                el.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
                el.style.opacity = '0';
                el.style.transform = 'translateX(20px)';
                setTimeout(() => el.remove(), 300);
            });
        }, 4000);
    }

    // ── Animate on Scroll (Intersection Observer) ──
    const animatedElements = document.querySelectorAll('.animate-in');
    if (animatedElements.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(el);
        });
    }

    // ── Header shrink on scroll ──
    const header = document.querySelector('.header-main');
    if (header) {
        let lastScroll = 0;
        window.addEventListener('scroll', function () {
            const currentScroll = window.pageYOffset;
            if (currentScroll > 100) {
                header.style.padding = '8px 0';
                header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
            } else {
                header.style.padding = '12px 0';
                header.style.boxShadow = '0 1px 3px rgba(0,0,0,0.08)';
            }
            lastScroll = currentScroll;
        });
    }

});
