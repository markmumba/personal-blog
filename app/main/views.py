from flask import render_template, redirect,url_for,abort
from . import main
from .. import db
from ..models import Blog,User,Comments
from flask_login import login_required,current_user
from .forms import BlogForm,CommentForm
import markdown2

# the main page in the app
@main.route('/')
def index():

	blogs=Blog.get_blog()
	title = 'HOME _ WELCOME TO THE BLOG SECTOR'
	return render_template('index.html', title = title,blogs = blogs)
	