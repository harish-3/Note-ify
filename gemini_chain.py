import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCT56Gh8mbyhe6jdDsaz5bd0ja7BZ4RxMg")  # Replace with your key

model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

PROMPT = """
You are an assistant that helps students study. Based on the following academic note, perform two tasks:

## Summary:
Summarize the content in concise bullet points.

## Flashcards:
Create clear Q&A flashcards to help revise this topic. Use this format:
Q1: [Question]
A: [Answer]

Make sure each flashcard has a clear question and answer pair.

Notes:
{text}
"""

def get_summary_and_flashcards(text, model_name):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(PROMPT.format(text=text))
    return response.text