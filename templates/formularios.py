from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class FormularioLogin(FlaskForm):
    user = StringField("user", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])