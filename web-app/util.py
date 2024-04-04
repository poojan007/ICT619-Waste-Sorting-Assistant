import tensorflow as tf
import numpy as np

model = None

def load_model():
    global model
    model = tf.keras.models.load_model("web-app/tf_model_1.keras")
    print("Model loaded successfully")

def classify_waste(img_path):
    # Load the image
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))

    # Convert the image to a numpy array
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    # Expand dimensions to match the shape of model input
    img_array = np.expand_dims(img_array, axis=0)

    # Predict (data augmentation is applied automatically)
    prediction = model.predict(img_array)

    if prediction[0][0] == 1:
      predicted_class = 'Recyclable Waste'
    else:
      predicted_class = 'Organic Waste'

    return predicted_class