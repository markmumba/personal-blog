from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo


class BlogForm(FlaskForm):

	title = StringField('Title')
	content = TextAreaField('New Blog')
	submit = SubmitField('Submit')
	