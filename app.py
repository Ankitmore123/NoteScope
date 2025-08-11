import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'uploads'
app =Flask(__name__)
os.makedirs(UPLOAD_FOLDER,exist_ok = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS ={"txt"}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/upload",methods =['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename 
    if file and allowed_file(filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return f"File uploaded succefully! Saved at {file_path}"
    else:
        return "INVALID file type. Only .txt allowed. "
    
@app.route("/")
def index():
    return render_template("index.html")

         

if __name__ == "__main__":
    app.run(debug= True)