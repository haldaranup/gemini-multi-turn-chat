import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = input("Enter your Google Gemini API Key: ")
genai.configure(api_key=GOOGLE_API_KEY)

try:
    temperature = float(input("Set temperature (0.0 for precise, 1.0 for creative): "))
except ValueError:
    temperature = 0.7 

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": temperature,
        "top_p": 1.0,
    }
)

chat = model.start_chat()

print("\nGemini Chat Started! Type 'exit' or 'quit' to end.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        print("Chat ended.")
        break

    try:
        response = chat.send_message(user_input)
        print("\nGemini:", response.text, "\n")
    except Exception as e:
        print(f"Error: {e}")
