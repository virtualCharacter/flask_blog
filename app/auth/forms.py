from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo

class LoginForm(FlaskForm):
    telephone = StringField(validators=[DataRequired(), Length(11, 11),
                Regexp('^[0-9]*$')], render_kw={'placeholder':'请输入电话号码'})
    password = PasswordField(validators=[DataRequired(), Length(6, 64),
                Regexp('^[A-Za-z0-9]*$')], render_kw={'placeholder':'请输入密码'})
    submit = SubmitField('登录')

class ReigisterForm(FlaskForm):
    telephone = StringField(validators=[DataRequired(), Length(11, 11),
                Regexp('^[0-9]*$')], render_kw={'placeholder':'请输入电话号码'})
    username = StringField(validators=[DataRequired(), Length(1, 64),
                Regexp('^[A-Za-z0-9]*$')], render_kw={'placeholder':'请输入用户名'})
    password1 = PasswordField(validators=[DataRequired(), Length(6, 64),
                Regexp('^[A-Za-z0-9]*$'), EqualTo('password2', message='两次密码要相等')],
                              render_kw={'placeholder':'请输入密码'})
    password2 = PasswordField(validators=[DataRequired()],
                              render_kw={'placeholder':'确认密码'})
    submit = SubmitField('注册')