import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    return text.strip()

def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += len(word) + 1
        
        if current_size >= chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def prepare_documents(documents):
    processed_chunks = []
    for doc in documents:
        clean_content = clean_text(doc['content'])
        chunks = chunk_text(clean_content)
        processed_chunks.extend(chunks)
    return processed_chunks
