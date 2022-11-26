from flask import Flask, render_template

# Return a web server instance


def create_app():
    app = Flask(__name__)

    # Define routes
    @app.route('/')
    def index():
        return render_template('index.html')

    return app
