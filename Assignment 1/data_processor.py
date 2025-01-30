import re
from datasets import load_dataset
from bs4 import BeautifulSoup

def clean_text(text):
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def load_and_process_data():
    dataset = load_dataset("imdb")
    
    train_data = [(clean_text(review), label) 
                  for review, label in zip(dataset['train']['text'], dataset['train']['label'])]
    test_data = [(clean_text(review), label) 
                 for review, label in zip(dataset['test']['text'], dataset['test']['label'])]
    
    return train_data, test_data
