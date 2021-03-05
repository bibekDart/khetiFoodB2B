from flask import Flask, request, abort, jsonify, send_from_directory

import os

UPLOAD_DIRECTORY="/static/uploadfiles"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app=Flask(__name__)

@app.route("/files")
def list_files():
    files=[]
    for files in os.listdir(UPLOAD_DIRECTORY):
        path=os.path.join(UPLOAD_DIRECTORY,filename)
        if os.path.isfile(path):
            files.append(filename)
        return jsonify(files)

@app.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):

    if " / " in filename:
        abort(400, "no subdirectories allowed")
    
    with open(os.path.join(UPLOAD_DIRECTORY,filename), "wb") as fp:
        fp.write(request.data)
    return "", 201



# @app.route('/saveFile', methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":

#         if request.files:

#             image = request.files

#             if image.filename=="":
#                 return redirect(request.url)
            
#             if not allowed_image(image.filename):
#                 print("That image extension is not allowed")

#                 return redirect(request.url)
#             else:
#                 filename= secure_filename(image.filename)
#                 image.save(os.path.join(app.config["UPLOAD_FILE"], filename))
            
#             print(image)
#             print("image saved")
            
#             return redirect(request.url)
   
#     return render_template("uploadimage.html")

if __name__ == "__main__":
    app.run(debug=True, port=800)
