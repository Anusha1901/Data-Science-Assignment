from flask import Flask, request, jsonify
import joblib
from data_processor import clean_text


app = Flask(__name__)
model = joblib.load('sentiment_model.pkl')

@app.route('/')
def home():
    return '''
    <h1>Welcome to the Sentiment Analysis API</h1>
    <h2>How to use:</h2>
    <p>Send a POST request to /predict with your review text</p>
    <p>Example format: {"review_text": "This movie was fantastic!"}</p>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Receive text input
    data = request.json
    if 'review_text' not in data:
        return jsonify({'error': 'No review_text field in request'}), 400
    
    # 2. Apply preprocessing
    cleaned_text = clean_text(data['review_text'])
    
    # 3. Run through model
    prediction = model.predict([cleaned_text])[0]
    
    # 4. Return prediction
    sentiment = 'positive' if prediction == 1 else 'negative'
    return jsonify({'sentiment_prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
