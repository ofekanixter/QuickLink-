from backend.db.models import URL

class URLDatabase:
    def __init__(self,DB):
        self.DB=DB

    def insert_url(self, long_url, short_url):
        """
        Insert a new URL into the database.
        """
        url = URL(long_url=long_url, short_url=short_url)
        try:
            self.DB.session.add(url)
            self.DB.session.commit()  # Commit after adding the URL
            return url
        except Exception as e:
            self.DB.session.rollback()  # Rollback the session on error
            print(f"Error: {e}")
            return None
    def get_long_url(self, short_url):
        """
        Retrieve the long URL associated with a short URL.
        """
        return URL.query.filter_by(short_url=short_url).first()
