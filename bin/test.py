from roboflow import Roboflow
rf = Roboflow(api_key="Ch0o7kU3qeNdMdVe9zVT")
project = rf.workspace().project("h_i_p")
model = project.version(9).model

# infer on a local image
# print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("testing.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
url = "https://prod-images-static.radiopaedia.org/images/53146201/d25c89d45b25c2d132348c5875cce3_big_gallery.jpeg"
print(model.predict(url, hosted=True, confidence=40, overlap=30).json())