import os
from flask import Flask, render_template, request
import subprocess

__author__ = 'agrim'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'another/images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    
    command = 'python another/test_imagenet.py --image another/images/%s' % filename
    output2 = subprocess.check_output(command ,shell=True)
    return output2.split()[-1] #just choosing to display what the recognized item is.
    # return output
    # return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)