# News Portal Website — Implementation Plan

A full-featured news portal inspired by **Indian Express Mumbai** section, built per the SRS document requirements.

## Summary

Build a multi-page, responsive news website with a Flask backend, SQLite database, and a modern frontend. The site will feature a homepage with featured/recent articles, category filtering, article detail pages, search, pagination, and an admin panel for content management.

---

## User Review Required

> [!IMPORTANT]
> **Technology Stack Confirmation**: The SRS specifies HTML/CSS frontend + Python Flask backend + MySQL/SQLite database. I'll use **Flask + SQLite** for simplicity (no separate MySQL setup needed). Please confirm this is acceptable.

> [!IMPORTANT]
> **Admin Panel Scope**: The SRS includes a full admin panel (add/edit/delete articles, upload images, manage categories). This will be built as a separate admin area with login authentication. Confirm if you want full admin functionality in v1.

> [!WARNING]
> **No Real API/Scraping**: This will use sample/seed data for news articles — not live data from Indian Express. The admin panel will let you add your own articles.

---

## Proposed Changes

### Architecture Overview

```
News Website/
├── app.py                 # Flask application (routes, API)
├── config.py              # Configuration settings
├── models.py              # SQLAlchemy database models
├── seed_data.py           # Sample news data seeder
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   └── main.js        # Frontend JavaScript
│   ├── images/            # Generated news images
│   └── uploads/           # Admin-uploaded images
├── templates/
│   ├── base.html          # Base template with nav/footer
│   ├── index.html         # Homepage
│   ├── article.html       # Article detail page
│   ├── category.html      # Category listing page
│   ├── search.html        # Search results page
│   ├── admin/
│   │   ├── login.html     # Admin login
│   │   ├── dashboard.html # Admin dashboard
│   │   └── editor.html    # Article editor (add/edit)
```

---

### Component 1 — Backend (Flask + SQLite)

#### [NEW] [app.py](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/app.py)
- Flask app with routes for:
  - `GET /` — Homepage with featured + recent articles
  - `GET /article/<id>` — Article detail page
  - `GET /category/<name>` — Category filtered view
  - `GET /search?q=` — Search results
  - `GET /api/articles` — REST API for articles (with pagination)
  - Admin routes: login, dashboard, CRUD operations

#### [NEW] [models.py](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/models.py)
- **Article** model: id, title, content, short_description, category, author, publish_date, image_url, is_featured, views
- **User (Admin)** model: id, username, password_hash, role

#### [NEW] [config.py](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/config.py)
- Database URI, secret key, upload folder settings

#### [NEW] [seed_data.py](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/seed_data.py)
- Script to populate database with 20+ sample Mumbai news articles across categories (News, Photos, Videos, Politics, Sports, Entertainment)

---

### Component 2 — Frontend Design (Indian Express-inspired)

#### [NEW] [style.css](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/static/css/style.css)

Design system inspired by Indian Express:
- **Color Palette**: White background, dark navy header (#1A1A2E), red accent (#E63946) for breaking news, deep blue (#0D47A1) for links, light gray (#F5F5F5) section backgrounds
- **Typography**: Inter + Merriweather (Google Fonts) — clean sans-serif for UI, serif for article headlines
- **Layout**: Full-width header → breadcrumb → main content (70%) + sidebar (30%) → footer
- **Features**: Breaking news ticker, smooth hover animations, card-based article grid, glassmorphism search bar, gradient accents

#### [NEW] [main.js](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/static/js/main.js)
- "Load More" pagination (AJAX, no page reload)
- Breaking news ticker animation
- Mobile hamburger menu toggle
- Search autocomplete
- Smooth scroll and micro-interactions

---

### Component 3 — Pages (Jinja2 Templates)

#### [NEW] [base.html](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/templates/base.html)
- Sticky header with logo, navigation (Home, India, Cities, Entertainment, Sports, Business, Tech, Opinion)
- Breaking news ticker bar (red banner, scrolling headlines)
- City sub-navigation (Mumbai, Delhi, Pune, Bangalore, etc.)
- Footer with multi-column links, social icons, copyright

#### [NEW] [index.html](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/templates/index.html)
- **Hero Section**: Large featured article with image + title overlay
- **Top Stories Grid**: 4 articles in a 2×2 grid with thumbnails
- **Latest News Feed**: Chronological list with timestamp, category tags
- **Sidebar**: Trending articles, "Most Read" section

#### [NEW] [article.html](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/templates/article.html)
- Full article view with large hero image, title, author, date
- Article body with proper typography
- Share buttons, related articles at bottom
- Breadcrumb navigation (Home > Cities > Mumbai > Article)

#### [NEW] [category.html](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/templates/category.html)
- Category filtered article grid
- Category tabs (News / Photos / Videos)

#### [NEW] [search.html](file:///c:/Users/Amaya/OneDrive/Desktop/News%20Website/templates/search.html)
- Search results with highlighted keywords

#### [NEW] Admin Templates (login.html, dashboard.html, editor.html)
- Login form with JWT/session auth
- Dashboard: article list with edit/delete actions
- Rich text editor for creating/editing articles with image upload

---

### Component 4 — Generated Assets

I'll use the image generation tool to create:
- News portal logo
- Sample hero/featured article images
- Category header images

---

## Key Design Decisions

| Feature | Implementation |
|---|---|
| **Layout** | Indian Express-style: header → ticker → breadcrumb → content + sidebar → footer |
| **Navigation** | Multi-tier: main nav (sections) + sub-nav (cities) + trending bar |
| **Article Cards** | Image left/top, title + excerpt + timestamp + category badge |
| **Breaking News** | Red animated ticker bar below header |
| **Pagination** | "Load More" button with AJAX (no full page reload per SRS) |
| **Responsive** | Mobile-first with hamburger menu, stacked layout |
| **Auth** | Flask-Login with hashed passwords for admin panel |
| **Database** | SQLite with SQLAlchemy ORM (easy setup, portable) |

---

## Open Questions

> [!IMPORTANT]
> 1. **Portal Name**: What should the news portal be called? (e.g., "Mumbai Express", "City Pulse", or your own name?)
> 2. **Color Preference**: I'll use a professional red/white/navy scheme similar to Indian Express. Any color preferences?
> 3. **Admin Panel**: Do you want the full admin panel with authentication in v1, or should I focus on the reader-facing pages first?

---

## Verification Plan

### Automated Tests
- Run Flask dev server and verify all routes respond correctly
- Test pagination API endpoint
- Verify search functionality
- Test admin login/CRUD operations

### Manual Verification
- Open the site in browser, take screenshots of all pages
- Test responsive design at mobile/tablet/desktop breakpoints
- Verify all navigation links work
- Test "Load More" functionality
- Verify article detail page rendering
