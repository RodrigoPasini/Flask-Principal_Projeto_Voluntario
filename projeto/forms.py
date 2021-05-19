from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    name = StringField('Nome completo', validators=[DataRequired()])
    address = StringField('Rua', validators=[DataRequired()])
    number = IntegerField('Número', validators=[DataRequired()])
    city = StringField('Cidade', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    country_code = IntegerField('CEP', validators=[DataRequired()])
    phone = IntegerField('Telefone', validators=[NumberRange(min=0, max=11)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired(), EqualTo('pass_confirm', message = 'Passwords Must Match')])
    pass_confirm = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Este e-mail já foi registrado por um outro usuário!')


    def check_username(self, field):
        #Check if not None for name!
        if User.query.filter_by(usernname=field.data).first():
            raise ValidationError('Este usuário já existe.')


    def check_name(self, field):
        # Check if not None for that username!
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Este nome já foi registrado anteriormente.')

#class UpdateUserForm(FlaskForm):

#    email = StringField('Email', validators=[DataRequired(), Email()])
#    username = StringField('Usuário', validators=[DataRequired()])
#    submit = SubmitField('Cadastrar')
