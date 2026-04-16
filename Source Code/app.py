from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
from werkzeug.utils import secure_filename
import base64
from io import BytesIO
from PIL import Image
import cv2

app = Flask(__name__)
CORS(app)

# ---------------- CONFIG ----------------
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- MODEL ----------------
MODEL_PATHS = [
    'mask_mobilenetv2.h5',
    os.path.join(os.path.dirname(__file__), 'mask_mobilenetv2.h5'),
]
model = None
img_size = 224

# ---------------- DNN FACE DETECTOR ----------------
protoPath = "deploy.prototxt"
modelPath = "res10_300x300_ssd_iter_140000.caffemodel"

if not (os.path.exists(protoPath) and os.path.exists(modelPath)):
    print("⚠️ Face detector files missing! Please place deploy.prototxt and res10_300x300_ssd_iter_140000.caffemodel in the same folder.")
    face_net = None
else:
    face_net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
    print("✅ DNN Face detector loaded successfully!")

# ---------------- LOAD MODEL ----------------
def load_ml_model():
    global model
    for path in MODEL_PATHS:
        try:
            if os.path.exists(path):
                model = load_model(path)
                print(f"✅ Model loaded successfully: {path}")
                return
        except Exception as e:
            print(f"⚠️ Error loading {path}: {e}")
    print("❌ Model not found! Place mask_mobilenetv2.h5 in the same folder as app.py.")

# ---------------- HELPERS ----------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_face_dnn(img: Image.Image):
    """Return True if at least one human face is detected."""
    if face_net is None:
        print("⚠️ DNN model not loaded. Skipping face detection.")
        return False

    img_cv = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)
    (h, w) = img_cv.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img_cv, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.6:  # threshold
            return True
    return False

def preprocess_image(img):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize((img_size, img_size))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# ---------------- PREDICT ----------------
def predict_mask(image_source):
    try:
        img = image_source if isinstance(image_source, Image.Image) else Image.open(image_source)

        # ✅ Only predict if human face detected
        if not detect_face_dnn(img):
            return {'error': 'Please upload a human face image only!'}

        img_array = preprocess_image(img)
        prediction = model.predict(img_array, verbose=0)[0][0]

        # 🔁 Corrected logic (fixed reversed output)
        if prediction >= 0.5:
            label = "Without Mask"   # higher score = without mask
            confidence = float(prediction)
        else:
            label = "With Mask"
            confidence = float(1 - prediction)

        return {'label': label, 'confidence': round(confidence * 100, 2)}

    except Exception as e:
        return {'error': f'Prediction error: {str(e)}'}

# ---------------- ROUTES ----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please ensure model file exists.'}), 500

    try:
        if 'image' in request.files:
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            if not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file type. Please upload PNG, JPG, or JPEG'}), 400
            result = predict_mask(Image.open(file))
            return jsonify(result)

        elif 'image' in request.json:
            image_data = request.json['image']
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            img_bytes = base64.b64decode(image_data)
            img = Image.open(BytesIO(img_bytes))
            result = predict_mask(img)
            return jsonify(result)

        return jsonify({'error': 'No image provided'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'model_loaded': model is not None})

# ---------------- MAIN ----------------
if __name__ == '__main__':
    load_ml_model()
    app.run(debug=True, host='0.0.0.0', port=5000)