from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from main.main import main as main_blueprint
from auth.auth import auth as auth_blueprint
from quiz.quiz import quiz as quiz_blueprint

from auth.models import db as db


def create_app():
    app = Flask(__name__)  # NOQA
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(quiz_blueprint)

    # create db so it can be imported by other modules
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    sqlitedb_uri = 'sqlite:///../NEW_QuizSite/auth/db.sqlite'

    app.config['SQLALCHEMY_DATABASE_URI'] = sqlitedb_uri

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # user stuff
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)  # NOQA

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
