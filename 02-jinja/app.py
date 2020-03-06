


# layout - skeleton
# page - page template for similar looking pages
# partial - snippets to be inserted that are common

from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")

    with app.app_context():
        from . import routes

        return app

create_app().run(port=5000)