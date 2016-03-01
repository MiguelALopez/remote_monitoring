from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class MagnetLink(Form):
    magnet_link = StringField('magnet_link', validators=[DataRequired()])
    name_link = StringField('name_link', validators=[DataRequired()])
