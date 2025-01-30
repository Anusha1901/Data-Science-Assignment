#import os
#os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

from data_collector import get_wiki_data
from text_processor import prepare_documents
from vectorstore import VectorStore
import time

def load_initial_data():
    # Step 1: Get Wikipedia data
    print("Starting data collection...")
    wiki_docs = get_wiki_data()
    time.sleep(2)
    
    # Step 2: Process documents
    print("Processing documents...")
    chunks = prepare_documents(wiki_docs)
    time.sleep(2)
    
    # Step 3: Load into vector store in batches
    print("Loading into vector store...")
    vector_store = VectorStore()
    
    # Process in smaller batches
    batch_size = 10
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        vector_store.add_documents(batch)
        print(f"Processed batch {i//batch_size + 1}")
        time.sleep(1)
    
    print("Data loading complete!")

if __name__ == "__main__":
    load_initial_data()

