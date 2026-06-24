from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Talisman security headers
    Talisman(app, content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
        'style-src': "'self'",
    })

    # CORS configuration
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app
