from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ConvertOneForm(Form):
    aa_string = StringField('AA Chain', validators=[DataRequired()])
    d_forms = BooleanField('Allow D-forms of AA?')
    submit = SubmitField('Convert')

