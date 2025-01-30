import requests
import json

def test_chat():
    try:
        response = requests.post(
            'http://localhost:5000/chat',
            json={'query': 'What is deep learning?'},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()  # Raise exception for bad status codes
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

def test_history():
    try:
        response = requests.get('http://localhost:5000/history')
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    test_chat()
    test_history()

