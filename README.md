# College resource exchange
# College-Resource

## College Resource Exchange

A Django web app for students to share, sell, donate, or exchange college resources (books, notes, lab items, calculators, and more). Users can list items with photos and categories, browse listings, send requests for items, and post on a request board when they are looking for something specific.

## Features

- User accounts — registration, login, and profiles (year, branch, college).
- Resource listings — title, description, category, condition, optional image, and action type: Donate, Exchange, Request, or Sell (with price when selling).
- Requests — users can request a listed resource; owners can track Pending / Accepted / Declined status.
- Request board — community posts for items people need.
- Admin site — manage users and content at /admin/ (create a superuser first).

## Tech stack

- Python / Django 3.2.x
- SQLite (default; db.sqlite3 in the project root)
- Image uploads — uses Django ImageField (install Pillow for image support)

## Getting started

### 1. Clone and enter the project


##2. Virtual environment (recommended)
python -m venv venv
Windows:

venv\Scripts\activate
macOS / Linux:

source venv/bin/activate
3. Install dependencies
pip install "Django>=3.2,<4" Pillow
4. Database and admin user
python manage.py migrate
python manage.py createsuperuser
5. Run the development server
python manage.py runserver
Open http://127.0.0.1:8000/ for the app and http://127.0.0.1:8000/admin/ for Django admin.

Project layout
Path	Role
manage.py
Django entrypoint
college_resource_exchange/
Project settings and root URLs
resources/
Main app: models, views, templates, static files
media/
Uploaded images (created/used at runtime)
Configuration notes
Debug is enabled in settings.py for local development only. For production, set DEBUG = False, configure ALLOWED_HOSTS, and use a strong SECRET_KEY from environment variables—not the default key in the repo.
Do not commit db.sqlite3 or media/ uploads to a public repository if they contain personal data; add them to .gitignore for shared repos.
License
Specify your license here (e.g. MIT) or remove this section if the project is private coursework.
