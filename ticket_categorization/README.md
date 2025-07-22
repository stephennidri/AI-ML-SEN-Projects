# Support Ticket Categorization (NLP)

A Natural Language Processing (NLP) project that classifies IT support tickets based on urgency, category, and estimated response time.

## 🚀 Features
- Text preprocessing and vectorization (TF-IDF)
- Logistic Regression classifier
- Flask REST API endpoint for predictions
- Dockerized for portability

## 🛠 Tech Stack
Python · Flask · scikit-learn · joblib · Docker

## 🔧 Setup
```bash
git clone https://github.com/nidristephane/AI-ML_Engineer.git
cd AI-ML_Engineer/ticket_categorization
pip install -r requirements.txt
```

## 🧠 Train Model
```bash
python src/train.py
```

## 🔄 Run API
```bash
python src/predict.py
```

## 🐳 Run via Docker
```bash
docker build -t ticket-nlp .
docker run -p 5000:5000 ticket-nlp
```

## 🧪 Example API Call
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "My laptop cannot connect to Wi-Fi"}'
```

## 📊 Results
- Accuracy: ~88% (sample dataset)
- Fast response time under 100ms

## 📌 Future Work
- Label confidence scores
- Multi-label classification
- Deploy on AWS Lambda or Hugging Face Spaces
