# backend/db_insert.py
from backend.main import create_app
from backend.db.models import db, URL


# Create the Flask app and initialize the database
app = create_app()
with app.app_context():
    db.create_all()  # Create all tables

with app.app_context():
    # Create sample URLs
    long_url = "https://example.com/very/long/url"
    short_url = "abc123"
    new_url = URL(long_url=long_url, short_url=short_url)

    # Add and commit to the database
    db.session.add(new_url)
    db.session.commit()

    print(f"Inserted {new_url}")
