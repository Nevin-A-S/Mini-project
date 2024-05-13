import google.generativeai as genai
from scraper import scraper

genai.configure(api_key='AIzaSyAm5HDnero63r30sO3kLyyaYLrGzUDOA20')

prompt = """Welcome, Text Summarizer! Your task is to distill the essence of a given text document into a concise summary. Your summary should capture the key points and essential information, presented in bullet points, within a 250-word limit. Let's dive into the provided transcript and extract the vital details for our audience."""


def summarizer(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + "".join(text))
    
    return response.text
