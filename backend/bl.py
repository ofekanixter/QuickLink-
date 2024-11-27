from backend.db.db_util import URLDatabase
from string import ascii_letters, digits
import random
BASE_URL="http://localhost:5000/"
class BL:
    def __init__(self,DB):
        self.db = URLDatabase(DB)

    def generate_short_url(self, length=6):
        """
        Generate a random short URL.
        """
        characters = ascii_letters + digits
        return ''.join(random.choice(characters) for _ in range(length))

    def shorten_url_logic(self, long_url):
        """
        Handle the logic for shortening a long URL.
        """
        # Check if the URL already exists in the database
        existing_url = self.db.get_long_url(long_url)
        if existing_url:
            return {"short_url": existing_url.short_url}

        # Generate a new short URL
        short_url = self.generate_short_url()

        # Ensure the short URL is unique
        while self.db.get_long_url(short_url):
            short_url = self.generate_short_url()

        # Insert the new URL into the database
        url = self.db.insert_url(long_url, short_url)
        
        if url:
            return {"short_url": BASE_URL+url.short_url,
                    "short_code": url.short_url
                    }
        else:
            return {"error": "Failed to insert URL into database"}

    def redirect_to_long_url_logic(self, short_url):
        """
        Retrieve the long URL for a given short URL and return a redirect response.
        """
        url = self.db.get_long_url(short_url)
        if url:
            return {'long_url': url.long_url}
        else:
            return {"error": "URL not found"}
