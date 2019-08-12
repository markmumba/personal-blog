from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,PostAblog,PostAComment
from .. import db
from ..models import User,Blog,Comment
from ..requests import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    quotes = get_quotes()

    return render_template('index.html', title = title, quotes=quotes )

@main.route('/account/<uname>',methods=['GET','POST'])
@login_required
def account(uname):

    '''
    View root page function that returns the profile page and its data
    '''

    title = 'Profile'
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(fourOwffour)
    blogs = Blog.query.order_by(Blog.posted.desc()).all()
    
    return render_template('account.html', user = user, blogs=blogs)

@main.route('/update/<uname>',methods=['GET','POST'])
@login_required
def update(uname):

    '''
    View root page function that returns the update page and its data
    '''
    blog_form = PostAblog()
    if update_form.validate_on_submit():
        title = update_form.title.data
        blog = update_form.text.data
    
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(fourOwffour)
    blogs = Blog.query.order_by(Blog.posted.desc()).all()
    
    return render_template('update.html', user = user, blogs=blogs)


@main.route('/blogs',methods=['GET','POST'])
def blog():
        
        form = PostAblog()
        if form.validate_on_submit():
            new_blog = Blog(title=form.title.data, content=form.content.data, user_id=current_user.id)
            new_blog.save_blog()
            return redirect(url_for('main.blog'))
        blogs= Blog.get_blogs()
        users = User.query.all()

        return render_template('blogs.html',blogs=blogs,users=users, form=form )

@main.route('/comment')
def comment():

    '''
    View root page function that returns the comments page and its data
    '''

    title = 'Comment'
    

    return render_template('comment.html', title = title )

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('update.html',uname=uname))

@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    blog_form = PostAblog()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data

        # Updated blog instance
        new_blog = Blog(blog_title=title, blog_content=blog, user=current_user)

        # Save blog method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New blog'
    return render_template('blogs.html', title=title)
