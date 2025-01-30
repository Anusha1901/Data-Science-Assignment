import google.generativeai as genai
from config import Config

class GeminiLLM:
    def __init__(self, api_key):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_response(self, query, context):
        prompt = f"""
        Based on the following context, answer the question.
        
        Context: {context}
        
        Question: {query}
        """
        
        response = self.model.generate_content(prompt)
        return response.text
