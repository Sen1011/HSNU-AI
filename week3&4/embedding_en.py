import google.generativeai as genai
import os, time

google_api_key = "API_KEY"
genai.configure(api_key=google_api_key)

def get_embed(text):
  text = text.replace("\n", " ")
  model = genai.GenerativeModel("gemini-1.5-flash")
  try:
    response = model.generate_content("請把以下句子精準翻譯成英文: "+text)
  except:
    time.sleep(60)
    response = model.generate_content("請把以下句子精準翻譯成英文: "+text)

  result = genai.embed_content(
        model="models/text-embedding-004",
        content=response.text,
        task_type="retrieval_document",
        title="Custom query")

  return result['embedding']
