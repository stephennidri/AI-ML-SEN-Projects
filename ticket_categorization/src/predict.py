import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('models/ticket_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
