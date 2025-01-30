from flask import Flask, request, jsonify
import sqlite3
from vectorstore import VectorStore
from local_llm import GeminiLLM
from config import Config

import torch
torch.cuda.empty_cache()  # Clear GPU memory if available
torch.backends.cudnn.enabled = False  # Disable CUDNN

app = Flask(__name__)
vector_store = VectorStore()
llm = GeminiLLM(api_key=Config.GEMINI_API_KEY)

def get_db_connection():
    conn = sqlite3.connect('data/chat_history.db')
    conn.row_factory = sqlite3.Row  # This enables dictionary-like rows
    return conn

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    
    relevant_chunks = vector_store.query(query)
    context = " ".join(relevant_chunks)
    
    answer = llm.generate_response(query, context)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO chat_history (role, content) VALUES (?, ?)",
        ("user", query)
    )
    
    cursor.execute(
        "INSERT INTO chat_history (role, content) VALUES (?, ?)",
        ("system", answer)
    )
    
    conn.commit()
    conn.close()
    
    return jsonify({
        "answer": answer,
        "retrieved_chunks": relevant_chunks
    })

@app.route('/history', methods=['GET'])
def history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_history ORDER BY timestamp")
    history = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)

