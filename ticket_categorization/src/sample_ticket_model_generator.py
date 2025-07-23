import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample support ticket data
texts = [
    "Reset my password", "Unable to login", "Server down", 
    "Need invoice copy", "Refund request", "System crash",
    "Password not working", "Get billing info", "Site not loading"
]
labels = [
    "Account", "Account", "Technical", 
    "Billing", "Billing", "Technical", 
    "Account", "Billing", "Technical"
]

# Create a simple model pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(texts, labels)

# Save the model to disk
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ vectorizer.pkl created.")

