import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset
df = pd.read_csv('data/tickets.csv')
X = df['text']
y = df['label']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/ticket_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')
print("Model and vectorizer saved.")
