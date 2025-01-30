from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

def train_model(train_data):
    # Separate features and labels
    X_train = [text for text, _ in train_data]
    y_train = [label for _, label in train_data]
    
    # Create pipeline
    model = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=10000)),
        ('classifier', LogisticRegression(random_state=42))
    ])
    
    # Train model
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, 'sentiment_model.pkl')
    return model
