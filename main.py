from flask import Flask, request, redirect, render_template
import os
from werkzeug.utils import secure_filename
from roboflow import Roboflow


# visualize your prediction
# model.predict("uploads/test.jpg", confidence=40, overlap=30).save("E:/7 sem/project star/HIP DETECTION/static/upload/prediction.jpg")


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/show_image')
# def show_image():
#     return render_template('show_image.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)  # Redirect back to the upload page if no file is uploaded
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)  # Redirect back to the upload page if no file is selected
    
    if file:
        # Save the uploaded file and perform prediction here
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        
        from roboflow import Roboflow
        rf = Roboflow(api_key="Ch0o7kU3qeNdMdVe9zVT")
        project = rf.workspace().project("roi_det_2")
        model = project.version(1).model
        model.predict(file_path, confidence=40, overlap=30).save("static/outputs/prediction.jpg")
        
        return redirect('/show_image')  # Redirect to the show_image route

@app.route('/show_image')
def show_image():
    return render_template('show_image.html')



if __name__ == '__main__':
    app.run(debug=True)
