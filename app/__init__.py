from flask import Flask 
from flask_bootstrap import flask_bootstrap
from config import config_options
from flask_sqlachemy import SQLAlchemy
from flask_login import LoginManager
rom flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE


login_manager =LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view ='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix = '/admin')



    return app
