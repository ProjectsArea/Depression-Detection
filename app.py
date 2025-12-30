from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# ---------------- LOAD MODELS ----------------
try:
    with open("saved_models/tfidf_vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    print("TF-IDF vectorizer loaded successfully")
    print(f"TF-IDF vocabulary size: {len(tfidf.vocabulary_) if hasattr(tfidf, 'vocabulary_') else 'Not fitted'}")
except Exception as e:
    print(f"Error loading TF-IDF vectorizer: {e}")
    tfidf = None

with open("saved_models/svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

with open("saved_models/rf_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

with open("saved_models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

bilstm_model = load_model("saved_models/bilstm_model.keras")

with open("saved_models/ensemble_config.pkl", "rb") as f:
    config = pickle.load(f)

MAX_LEN = config["max_len"]
THRESHOLD = config.get("threshold", 0.4)

# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ---------------- PREDICTION FUNCTION ----------------
def predict_depression(text):
    try:
        print(f"Input text: {text}", flush=True)
        text = clean_text(text)
        print(f"Cleaned text: {text}", flush=True)
        
        # Simple rule-based approach for testing
        depression_keywords = ['sad', 'depressed', 'unhappy', 'miserable', 'hopeless', 'lonely', 'anxious', 'worried', 'empty', 'worthless']
        
        keyword_count = sum(1 for word in depression_keywords if word in text)
        print(f"Depression keywords found: {keyword_count}", flush=True)
        
        # Simple scoring
        if keyword_count >= 2:
            final_prob = 0.8
            label = "Depressed"
        elif keyword_count >= 1:
            final_prob = 0.6
            label = "Depressed"
        else:
            final_prob = 0.2
            label = "Not Depressed"
            
        print(f"Final probability: {final_prob}", flush=True)
        print(f"Final label: {label}", flush=True)
        
        return label, final_prob
    
    except Exception as e:
        print(f"Prediction error details: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return "Error", 0.0

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/detect", methods=["GET", "POST"])
def detect():
    prediction = None
    probability = None

    if request.method == "POST":
        print("POST request received!", flush=True)
        user_text = request.form.get("text", "")
        print(f"Form text: '{user_text}'", flush=True)
        
        if user_text:
            try:
                prediction, probability = predict_depression(user_text)
                probability = round(probability, 3)
                print(f"Final result: {prediction}, {probability}", flush=True)
            except Exception as e:
                print(f"Error in prediction: {e}", flush=True)
                prediction = "Error"
                probability = 0.0
        else:
            prediction = "No text provided"
            probability = 0.0

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)

