# Assignment 2: RAG (Retrieval-Augmented Generation) Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that uses Wikipedia data, ChromaDB for vector storage, and Google's Gemini API for response generation.

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/Anusha1901/Data-Science-Assignment.git
    ```

2. Create and activate virtual environment:
    ```bash
    python -m venv venv
   venv\Scripts\activate
    ```

3. Install dependencies:
   ```bash
    pip install -r requirements.txt
    ```


## Configuration

1. Create a .env file in the project root:

   ```bash
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

2. Get your Gemini API key from: https://makersuite.google.com/app/apikey


## Database Setup

Initialize SQLite database:

  ```bash
    python init_db.py
  ```

## Data Loading

Load Wikipedia data into ChromaDB:

  ```bash
    python load_data.py
  ```

## Running the Application

1. Start the Flask server:
   ```bash
    python app.py
    ```

2. The server will run at http://localhost:5000


## API Endpoints

#### Chat Endpoint
* URL: /chat
* Method: POST
* Body:

  ```bash
    {
    "query": "What is deep learning?"
    }
    ```

#### History Endpoint
* URL: /history
* Method: GET

Returns the chat history from the chat_history.db 


## Testing

Run the test script:

  ```bash
    python test_api.py
  ```


## Project Structure

  ```bash
├── app.py                             # Main Flask application
├── config.py                          # Configuration settings
├── data_collector.py                  # Wikipedia data collection
├── local_llm.py                      # Gemini API integration
├── init_db.py                         # Database initialization
├── load_data.py                       # Data loading script
├── test_api.py                        # API testing
├── text_processor.py                  # Text chunking and preprocessing  
└── vectorstore.py                     # ChromaDB vector storage

  ```

## Features

* Wikipedia-based knowledge base
* Semantic search using ChromaDB
* Response generation using Google's Gemini API
* Chat history storage in SQLite
* RESTful API endpoints


## Note on Database Implementation

While the assignment specified MySQL, this implementation uses SQLite due to Windows version compatibility limitations that prevented MySQL server installation. SQLite serves as an effective alternative that:

- Provides all necessary database functionality
- Maintains data persistence
- Enables efficient chat history storage
- Works seamlessly with the RAG system
- Requires no external server setup

The core functionality and features of the chatbot remain unchanged with SQLite, delivering the same robust performance as intended with MySQL.


