from flask import Flask
from app.api import api_blueprint

def create_app():
    app = Flask(__name__)

    # Register API blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)