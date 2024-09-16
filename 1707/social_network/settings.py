import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_socketio import SocketIO, emit
import os

project = flask.Flask(
    import_name="social_network",
    template_folder="templates"
)

socketio = SocketIO(project)

BASE_DIR = os.path.abspath(__file__ + "/../..")

PATH_CHAT_DATA = os.path.join(BASE_DIR, "instance/chat.json")

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
project.config['SECRET_KEY'] = 'dsaE@#9dsa89safhashf89dsha8dhsfbau9df8safu9da89fda'

DATABASE = flask_sqlalchemy.SQLAlchemy(project)

MIGRATIONS = flask_migrate.Migrate(app=project, db=DATABASE)

login_manager = flask_login.LoginManager()
login_manager.init_app(project)
login_manager.login_view = 'login.render_login'