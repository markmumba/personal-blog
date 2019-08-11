# in the views.py we create the diffrent routes to take on to the rendered html 
# for the login and to register 

from flask import render_template,redirect,url_for,request,flash
from .import auth
from ..models import User
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm, LoginForm
from .. import db


# the registration route 

@auth.route('/register',methods = ['GET','POST'])
def register()


