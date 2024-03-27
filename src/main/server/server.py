from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

from src.main.routes.event_routes import event_route_bp
from src.main.routes.attendees_routes import attendees_route_bp
from src.main.routes.check_in_routes import check_in_route_bp

app.register_blueprint(event_route_bp)
app.register_blueprint(attendees_route_bp)
app.register_blueprint(check_in_route_bp)
