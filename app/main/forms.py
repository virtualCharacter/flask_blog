from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class BlogForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(1, 64)],
                        render_kw={'placeholder':'请输入标题'})
    abstract =TextAreaField('abstract', validators=[DataRequired(), Length(1)],
                            render_kw={'placeholder': '请输入简介', 'rows':4})
    article = TextAreaField('article', validators=[DataRequired()],
                            render_kw={'placeholder':'请输入文章内容', 'rows': 15})
    submit = SubmitField('提交')

