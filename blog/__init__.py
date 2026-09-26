from pathlib import Path
from flask import Flask

from .extensions import db, login_manager


def create_app():

    app = Flask(__name__)

    # Secret key
    app.config["SECRET_KEY"] = "change-this-secret-key"

    # SQLite database
    base_dir = Path(__file__).resolve().parent.parent

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{base_dir / 'blog.db'}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Upload folder
    app.config["UPLOAD_FOLDER"] = str(
        base_dir / "blog" / "static" / "uploads"
    )

    app.config["MAX_CONTENT_LENGTH"] = 4 * 1024 * 1024

    # Create upload folder
    Path(app.config["UPLOAD_FOLDER"]).mkdir(
        parents=True,
        exist_ok=True
    )

    # Initialize database
    db.init_app(app)

    # Initialize login manager
    login_manager.init_app(app)

    login_manager.login_view = "main.login"

    # Import models and routes
    from .models import User
    from .routes import main

    # Register routes
    app.register_blueprint(main)

    # Load logged-in user
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Create database tables
    with app.app_context():
        db.create_all()

    return app