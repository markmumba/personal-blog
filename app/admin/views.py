from flask import render_template,redirect,url_for,request,flash
from . import admin
from ..models import User,Blog,Comments
from flask_login import login_user,logout_user,login_required,current_user
from .. import db
from .forms import BlogForm


# Admin dashboard

def check_admin():


	if not current_user.is_admin:
        abort(403)


@admin.route('/admin/dashboard')
@login_required
def admin_dashboard():

	if not current_user.is_admin:
        abort(403)

    blogs = Blog.get_blog()
    return render_template('admin/admin_dashboard.html', title="AdminDashboard",blogs=blogs)


# blog views
@admin.route('/blogs',methods=['GET','POST'])
@login_required
def list_blogs():
	check_admin()

	blogs =Blog.query.all()

	return render_template('admin/post.html',blogs=blogs, title='Blogs')


@admin.route('/blogs/add', methods=['GET', 'POST'])
@login_required
def add_blog():
	# Returns a list of all
	check_admin()

    add_blog = True

    form = BlogForm()
    if form.validate_on_submit():
    	blogs = Blog(title = form.title.data,content=form.content.data)

    	try:
            db.session.add(blogs)
            db.session.commit()
            flash('Successfully added a new Blog Post.')
        except:

            flash('Error: Blog already exists.')
        return redirect(url_for('admin.list_blogs'))

    return render_template('admin/posts.html', action = "Add", add_blog=add_blog,form=form,title="Add Blog")





