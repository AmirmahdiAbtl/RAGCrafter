from flask import Flask, render_template
from developerassistant import developerassistant_bp
# from test import test_bp
def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(developerassistant_bp, url_prefix='/developerassistant')
    # app.register_blueprint(test_bp, url_prefix = "/test")
    # Initialize the database
    with app.app_context():
        from database import init_db
        init_db()

    return app

# Define routes after creating the app
app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
