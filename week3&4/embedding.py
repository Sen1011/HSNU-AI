import google.generativeai as genai
import os

google_api_key = "API_KEY"
genai.configure(api_key=google_api_key)

def get_embed(text):
  text = text.replace("\n", " ")
  result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document",
        title="Custom query")

  return result['embedding']
