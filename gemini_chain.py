import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCT56Gh8mbyhe6jdDsaz5bd0ja7BZ4RxMg") 

model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT = """
You are an assistant that helps students study. Based on the following academic note, perform two tasks:

## Summary:
Summarize the content in concise bullet points.

## Flashcards:
Create clear Q&A flashcards to help revise this topic. Use this format:
Q: [Question]
A: [Answer]

Make sure each flashcard has a clear question and answer pair.

Notes:
{text}
"""

def get_summary_and_flashcards(text):
    response = model.generate_content(PROMPT.format(text=text))
    return response.text
