from flask import Flask
from flask_cors import CORS
from src.models.sqllite.settings.connection import db_connection_handler

# Importar Blueprints de rotas
from src.main.routes.pets_routes import pets_route_bp

db_connection_handler.connect_to_db()  # Initialize the database connection

app = Flask(__name__)
CORS(app)

app.register_blueprint(pets_route_bp)
