from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    # templates and static are placed at project root for easier editing in workspace
    app = Flask(__name__, template_folder="../templates", static_folder="../static", instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="change-me-in-production",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///d:/VS_code/Projects/AWS-Project/instance/app.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # import routes and models so they are registered
        from . import routes  # noqa: F401
        db.create_all()

    return app
