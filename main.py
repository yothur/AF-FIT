from flask import Flask
from configdb import db
from dotenv import load_dotenv

load_dotenv()

from blueprints.usuarios import usuarios_bp
from blueprints.auth import auth_bp
import os


app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# [CONECTAR COM O BANCO] - app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:senha@localhost:5432/nome-do-banco'
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql+psycopg2://postgres:femtogodhand8@localhost:5432/AFFIT'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


app.register_blueprint(usuarios_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()

