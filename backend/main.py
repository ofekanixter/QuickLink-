# backend/main.py
from flask import Flask, request, jsonify, redirect
from backend.db.models import DB
from backend.db.db_util import URLDatabase
from backend.bl import BL

def create_app():
    app = Flask(__name__)

    # Set the database URI (SQLite in this case)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    DB.init_app(app)


    # Create all tables within the app context
    with app.app_context():
        DB.create_all()  # This will create tables if they do not exist

    url_shortener = BL(DB)

    @app.route('/api/shorten', methods=['POST'])
    def shorten_url():
        data = request.get_json()
        long_url = data.get('url')

        if not long_url:
            return jsonify({"error": "No long URL provided"}), 400

        result = url_shortener.shorten_url_logic(long_url)
        if "error" in result:
            return jsonify(result), 400

        return jsonify(result)

    @app.route('/<short_url>', methods=['GET'])
    def redirect_to_url(short_url):
        result = url_shortener.redirect_to_long_url_logic(short_url)
        if "error" in result:
            return jsonify(result), 404

        return redirect(result['long_url'])

    return app
