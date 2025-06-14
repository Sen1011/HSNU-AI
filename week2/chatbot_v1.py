import google.generativeai as genai

genai.configure(api_key='API_KEY')
model = genai.GenerativeModel("gemini-1.5-flash")

while True:
    text_line = input("User: ")
    response = model.generate_content(text_line)
    print("AI: "+response.text)
    if text_line == "exit":
        break
