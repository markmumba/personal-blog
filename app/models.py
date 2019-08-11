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

	__tablename__ ='blog'

	id  =db.Column(db.Intger,primary_Key=True)
	title =db.Column(db.String(300))
	content = db.Column(db.String(1000))
	date_posted  =db.Column(db.DateTime,default=datetime.utcnow)
	user_id =db.Column(db.Intger,db.ForeignKey("users.id"))
	comment_id =db.relationship("Comments",backref='blog', lazy= 'dynamic')


	def save_blog(self):
		# this to save the blogs when written

		db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_blog(cls):
    	# this function will help in deleting the blogs.it will apply to all due to the @class method

    	blog = Blog.query.filter_by(id=blog_id).delete()
    	comment = Comments.query.filter_by(blog_id =blog_id).delete()


# The users class
class User(UserMixin,db.Model):
	# this helps us to create new users into our database and save them

	__tablename__='users'

	id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    blog = db.relationship("Blog", backref = "user", lazy = "dynamic")
    comment = db.relationship("Comments", backref = "user", lazy = "dynamic")
    is_admin = db.Column(db.Boolean,default=False)

    # makingour password secure 
    # We use the werkzeug.security to generate hash pass
    # and also to check the hashed password
    @property
    # We use the @property decorator to create a write only class property password. 
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

        # this is to save the user to our dabase

    def save_user(self):
        db.session.add(self)
        db.session.commit()



    def __repr__(self):
        return f'User {self.username}'

# commentsclass 
class Comments(db.Model):

	__tablename__ = 'comment'

    # add columns
    id = db.Column(db. Integer,primary_key = True)
    comment_section = db.Column(db.String(500))
    author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blog.id"))

    def save_comment(self):

    	db.session.add(self)
    	db.session.commit()

     @classmethod
    def get_comments(self,id):
        comment = Comments.query.filter_by(blog_id=id).all()
        return comment

    @classmethod
    def delete_comment(cls,comment_id):
        '''
        Function that delete a simgle comment in a blog post
        '''
        comment = Comments.query.filter_by(id=comment_id).delete()
        db.session.commit()




