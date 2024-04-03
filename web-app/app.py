from flask import Flask, request, render_template, redirect, jsonify
import util
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Loading the model
util.load_model()

# Default page
@app.route("/")
def home():
    return render_template("home.html")

# API Url for the classification
@app.route("/classify", methods = ["POST"])
def classifywaste():
    image_data = request.files["file"]

    #save the image to upload
    basepath = os.path.dirname(__file__)
    image_path = os.path.join(basepath, "uploads", secure_filename(image_data.filename))
    image_data.save(image_path)

    predicted_value = util.classify_waste(image_path)
    os.remove(image_path)
    return jsonify(predicted_value=predicted_value)

# here is route of 404 means page not found error
@app.errorhandler(404)
def page_not_found(e):
    # here i created my own 404 page which will be redirect when 404 error occured in this web app
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run()