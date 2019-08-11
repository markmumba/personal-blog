# this the form that will allow a person to register into my blog app
# contains registration form and  also the login form
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User





class RegistrationForm():
    username =StringField('username', validators=[Required()])
    email = StringField('email', validators=[Required(),Email()])
    password =PasswordField('password', validators=[Required(),EqualTo('password',message = 'password must match')])
    confirm_password=PasswordField('confirm password',validators=[Required()])
    submit = SubmitField('Sign Up')

    # custom validators

    def validate_email(self,data_field):
        # check if email passed in are in our database 
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError( 'KUNA ACCOUNT IKO NA EMAIL KAMA HIO')

    def validate_username(self,data_field):
        # checks if username passed in exists
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError( 'IYO JINA ISHA CHUKULIWA BANA')



class LoginForm():
    email=StringField(' email ',validators=[Required(),Email()])
    password=PasswordField('password',validators=[Required()])
    remember = BooleanField('remember me')
    submit= SubmitField('Sign in')
   