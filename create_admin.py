"""Create an admin user for local development.

Usage:
    python create_admin.py username password
"""
import sys
from app import create_app, db
from app.models import User


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_admin.py username password")
        return
    username = sys.argv[1]
    password = sys.argv[2]

    app = create_app()
    with app.app_context():
        if User.query.filter_by(username=username).first():
            print("User already exists")
            return
        u = User(username=username)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        print("Created user", username)


if __name__ == "__main__":
    main()
