import requests

def test_sentiment():
    url = 'http://localhost:5000/predict'
    
    # Test cases
    reviews = [
        "This movie was fantastic! I loved every minute of it.",
        "Terrible waste of time. Don't watch this movie.",
        "Pretty good film with great acting."
    ]
    
    for review in reviews:
        data = {'review_text': review}
        response = requests.post(url, json=data)
        print(f"\nReview: {review}")
        print(f"Sentiment: {response.json()['sentiment_prediction']}")

if __name__ == "__main__":
    test_sentiment()
