import os
import xlrd
from flask import redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename
from Project2 import app
from Project2.forms import UploadFileForm
from Project2.utils import file_comparison

@app.route('/download/<file>')
def download(file):
    exists = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'],file))
    if exists:
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                               file)
    else:
        flash(f"Please upload a file!", "danger")
        return redirect(url_for('upload_file'))


@app.route('/upload/<filename>')
def compare_file(filename):
    exists = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    if exists:
        file = file_comparison(filename)
        return render_template('compare_file.html', file=file)
    else:
        flash(f"Please upload a file!", "danger")
        return redirect(url_for('upload_file'))


@app.route('/', methods=['GET','POST'])
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        if form.uploaded_file.data:
            file = form.uploaded_file.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f"file is uploaded successfully!", "success")
            return redirect(url_for('compare_file', filename=filename))
    return render_template('upload.html', form=form)


