from database import init_db, Review
from data_processor import load_and_process_data
from model import train_model
from sklearn.metrics import classification_report

def main():
    # Initialize database
    session = init_db()
    
    # Load and process data
    train_data, test_data = load_and_process_data()
    
    # Store in database
    for text, label in train_data:
        review = Review(review_text=text, sentiment='positive' if label == 1 else 'negative')
        session.add(review)
    session.commit()
    
    # Train model
    model = train_model(train_data)
    
    # Evaluate model
    X_test = [text for text, _ in test_data]
    y_test = [label for _, label in test_data]
    predictions = model.predict(X_test)
    
    print(classification_report(y_test, predictions))

if __name__ == '__main__':
    main()
