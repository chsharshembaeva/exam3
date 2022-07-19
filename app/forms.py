from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')

    def validate_password(self, password):
        if len(password.data) < 8:
            raise wf.ValidationError('Пароль должен быть длиннее 8 символов')


class EmployeeForm(FlaskForm):
    fullname = wf.StringField('ФИО', validators=[wf.validators.DataRequired()])
    phone = wf.StringField('Телефон', validators=[wf.validators.DataRequired()])
    short_info = wf.TextAreaField('Краткая информация', validators=[wf.validators.DataRequired()])
    experience = wf.IntegerField('Опыт', validators=[wf.validators.DataRequired()])
    preferred_position = wf.StringField('Предпочитаемая позиция')
    submit = wf.SubmitField('Ok')

    def validate_fullname(self, fullname):
        if " " not in fullname.data:
            raise wf.ValidationError('Введите ФИО полностью')
