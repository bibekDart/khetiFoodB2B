from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.config["UPLOAD_FILE"]="/Users/bibek/OneDrive/Desktop/flask-app/static/uploadfiles"
app.config["ALLOWED_IMAGE_EXTENSIONS"]=["PNG", "JPG", "JPEG", "GIF", "TXT"]

list_dict=[]

def allowed_image(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/', methods=["GET"])
def getFile():
    return render_template('uploadimage.html')
    
@app.route('/saveFile', methods=["GET", "POST"])

def upload_file():
    if request.method == "POST":
        req_file=request.files

        x=request.files['file']

        files=req_file['file']
        
        if files.filename == "":
            return "file name cannot be empty"
        
        if not allowed_image(files.filename):
            return "select image extension is not allowded"
        
        else:
            files.save(os.path.join(app.config["UPLOAD_FILE"], secure_filename(files.filename)))
            
            print(files.filename)

            list_dict.append({'file':files})
        
            print(len(list_dict))

            return "file saved"
            
        return redirect(url_for('saveFile'))
        
    



        
if __name__ == "__main__":
    app.run(debug=True)