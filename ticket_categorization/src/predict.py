import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('models/ticket_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    restaurant_name = request.json['restaurant_name']
    restaurant_name_vec = vectorizer.transform([restaurant_name])
    prediction = model.predict(restaurant_name_vec)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
