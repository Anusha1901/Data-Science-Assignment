# Assignment 1: End-to-End Sentiment Analysis Pipeline
## Overview
A machine learning API that performs sentiment analysis on movie reviews using the IMDB dataset. The system uses TF-IDF vectorization with Logistic Regression to classify reviews as positive or negative.

## Project Setup
1. Clone the repository
    ```bash
    git clone https://github.com/Anusha1901/Data-Science-Assignment.git
    ```
2. Install dependencies
   ```bash
    pip install -r requirements.txt
    ```

## Data Acquisition
* Dataset: IMDB Movie Reviews (50,000 reviews)
* Source: Hugging Face Datasets
* Automatic download happens when running main.py

## Run Instructions

1. Train the Model
   ```bash
    python main.py
    ```

2. Start the API Server
   ```bash
    python app.py
    ```

3.  Test the Endpoint

    Option 1: Using PowerShell
   
    ```bash
    Invoke-RestMethod -Uri "http://localhost:5000/predict" -Method Post -ContentType "application/json" -Body '{"review_text": "This movie is amazing!"}'
    ```

    Option 2: Using test_request.py

    ```bash
    python test_request.py
    ```

## Model Information

* Architecture:

  * Pipeline combining:
     * TF-IDF Vectorization (feature extraction)
     * Logistic Regression (classification)

This pipeline ensures consistent preprocessing for both training and prediction

* Features:
   * 10,000 most frequent terms from TF-IDF
   * Automatic text cleaning and vectorization

* Model Benefits:
   * Fast training and prediction
   * Memory efficient
   * Highly interpretable results

* Performance Metrics:
    * Accuracy: ~87%
    * F1 Score: ~0.86
    * Precision: ~0.85
    * Recall: ~0.87

The scikit-learn pipeline approach streamlines the entire process from raw text to sentiment prediction, making the code both elegant and maintainable.

## API Endpoints

* GET /: Welcome page with usage instructions
* POST /predict: Sentiment analysis endpoint

  * Input: JSON with "review_text" field
  * Output: JSON with "sentiment_prediction" (positive/negative)

## Files Structure

sentiment_analysis_api/
```
├── main.py                         # Training script
├── app.py                          # Flask API
├── database.py                     # Database operations
├── data_processor.py               # Data cleaning
├── model.py                        # Model definition
├── test_request.py                 # Test script
├── reviews.db.zip                  # Compressed database file
└── requirements.txt                # Dependencies

```

## Important Note

The reviews.db file has been compressed to reviews.db.zip for GitHub upload due to size limitations. Extract the zip file before running the application.
 
   

