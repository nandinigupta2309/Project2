from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired

class UploadFileForm(FlaskForm):
    uploaded_file = FileField('',validators=[FileAllowed(['xls']),DataRequired()])
    submit = SubmitField("Upload File")
