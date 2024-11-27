from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class URL(DB.Model):
    __tablename__ = 'url'  # Optional but helps ensure correct table name
    id = DB.Column(DB.Integer, primary_key=True)
    long_url = DB.Column(DB.String(500), nullable=False)
    short_url = DB.Column(DB.String(100), unique=True, nullable=False)
    def __repr__(self):
        return f"<URL {self.short_url}>"
