import wikipedia
import time

def get_wiki_data():
    topics = [
        "Deep Learning"
        "Machine Learning",        
    ]
    documents = []
    
    for topic in topics:
        try:
            print(f"Fetching data for: {topic}")
            search_results = wikipedia.search(topic, results=1)
            if search_results:
                page = wikipedia.page(search_results[0], auto_suggest=False)
                documents.append({
                    'title': page.title,
                    'content': page.content[:5000]  # Limit content size
                })
                time.sleep(1)  # Add delay between requests
        except Exception as e:
            print(f"Skipping {topic}: {e}")
            continue
    
    return documents


