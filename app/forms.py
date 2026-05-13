from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=80)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=200)])
    body = TextAreaField("Body", validators=[DataRequired()])
    tags = StringField("Tags (comma separated)")
    submit = SubmitField("Save")


class CommentForm(FlaskForm):
    author = StringField("Name", validators=[DataRequired(), Length(max=80)])
    body = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")
