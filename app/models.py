# this is the models.py where we are able to create columns for our database 
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manger
from datetime import datetime




@login_manger.user_loader
def load_user(user_id):


	return User.query.get(init(user_id))


# this will contain all the blogs
class Blog(db.Model):
	