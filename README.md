# HIP Detection Project

## Overview
This project aims to detect hip fractures in medical images using a deep learning model integrated with Flask web framework. It utilizes Roboflow for model training and inference and supervision for image annotation.

## Video Demonstration


## Technologies Used
- Python
- Flask
- Roboflow
- supervision
- OpenCV
## Usage
### Running the Application
1. Start the Flask server:
2. Open a web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.

### Uploading Images
- Navigate to the homepage and use the upload form to select an image file.
- Click on the "Upload" button to initiate the HIP detection process.

### Viewing Results
- After uploading, the application will process the image using Roboflow and supervision.
- Once processed, the annotated image with HIP detection overlays will be displayed.


## File Structure
├── main.py # Main Flask application
├── templates/ # HTML templates
│ ├── index.html # Homepage template
│ ├── show_image.html # Template to display annotated images
├── static/ # Static files
│ ├── outputs/ # Directory to store processed images
├── uploads/ # Directory for uploaded images
├── requirements.txt # Dependencies
└── README.md # Project documentation

