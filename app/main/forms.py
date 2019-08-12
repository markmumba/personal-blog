from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField,SubmitField,StringField
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio.',validators = [Required()])
    submit = SubmitField('Update')

class PostAblog (FlaskForm):
    title = StringField('Title',validators = [Required()])
    content = TextAreaField('Start blogging',validators = [Required()])
    submit = SubmitField('Blog')

class PostAComment (FlaskForm):
    comment = TextAreaField(validators = [Required()])
    submit = SubmitField('Comment',validators = [Required()])
