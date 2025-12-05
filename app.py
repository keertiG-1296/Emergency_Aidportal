import os
from flask import Flask
from config import Config
from blueprints.general import general
from blueprints.accident_zone import accident_zone
from blueprints.blood import blood
from blueprints.organ import organ
from blueprints.error import error
from blueprints.dashboard import dashboard
from blueprints.admin import admin
def create_app(config_class=Config):
    """
    Factory function to create and configure the Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Set secret key 
    app.secret_key = os.environ.get("SESSION_SECRET", Config.SECRET_KEY)
    
    # Register blueprints
    app.register_blueprint(general)
    app.register_blueprint(accident_zone)
    app.register_blueprint(blood)
    app.register_blueprint(organ)
    app.register_blueprint(error)
    app.register_blueprint(dashboard, url_prefix="/dashboard")
    app.register_blueprint(admin, url_prefix="/admin")
    return app
