from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os
# import time

from main.main import main as main_blueprint
from auth.auth import auth as auth_blueprint
from quiz.quiz import quiz as quiz_blueprint

from auth.models import db, User


def create_app():
    app = Flask(__name__)  # NOQA
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(quiz_blueprint)

    # create db so it can be imported by other modules
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    # check if running on macos or linux
    if os.name == 'posix':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../NEW_QuizSite/auth/db.sqlite'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/auth/db.sqlite'

    db.init_app(app)

    # time.sleep(20)

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
    port = int(os.environ.get('PORT', 5001))
    print('port is', port) if port != 5001 else None
    app.run(debug=True, host='0.0.0.0', port=port)
