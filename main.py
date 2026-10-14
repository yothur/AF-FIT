from flask import Flask
from configdb import db
import os

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY")
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:12345@localhost:5432/AFFIT'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

