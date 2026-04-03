# News24Plus

A modern, full-stack responsive news portal web application. It features dynamic content loading, an admin management panel, advanced routing, robust search functionality, and category filtering.

## 🚀 Key Features

* **Elegant Frontend:** A rich HTML/CSS/JS user interface featuring a breaking news ticker, sliding articles, a persistent top navigation bar with dynamic categories, and robust mock integrations for E-paper and Newsletter signups.
* **Backend Architecture:** Built on Python and the Flask framework to smoothly handle template rendering, data integration, and routing.
* **Database:** Powered by SQLite and SQLAlchemy ORM, tracking User (Admin) data and full Article objects with capabilities for drafts, scheduling, and metrics (like views).
* **Admin Dashboard:** A secure internal portal where editors and administrators can log in to create, edit, format, or delete newspaper articles. 
* **Dynamic Static Pages:** Intelligent backend routing natively handles requests for informative supplementary templates ranging from *About Us*, *Weather*, *Careers*, to legal disclaimers. 

## 🛠️ Installation & Setup

1. **Activate your environment** (Optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database (Optionally Seed Data):**
   *(The database natively creates its tables on its first run, however, you can also run the seed generator)*
   ```bash
   python seed_data.py
   ```

4. **Start the Development Server:**
   ```bash
   python app.py
   ```
   Navigate to `http://127.0.0.1:5000` in your browser.

## 📁 Project Structure

* `app.py`: Central Flask application with definitions for public, API, and Administrative routes.
* `models.py`: Defines the SQLAlchemy database schemas (`User` and `Article`).
* `config.py`: Handles configuration environments and secret keys.
* `seed_data.py`: A helper script for populating the database with fake news articles for development. 
* `templates/`: Jinja2 HTML templates covering public views (`index.html`, `article.html`, `epaper.html`, etc.) and the admin sub-directory. 
* `static/`: Contains local CSS stylesheets, javascript functions, and image uploads. 
