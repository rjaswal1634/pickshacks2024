from flask import Flask, render_template, request
from stegano import lsb
from PIL import Image
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            message = request.form.get('message')
            secret = lsb.hide(filename, message)
            secret.save("hidden.png")
            return 'Data hidden successfully'
    return render_template('index.html')

@app.route('/reveal', methods=['GET', 'POST'])
def reveal():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            clear_message = lsb.reveal(filename)
            return 'Hidden message is: ' + clear_message
    return render_template('reveal.html')

if __name__ == '__main__':
    app.run(debug=True)
