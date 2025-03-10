import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai_api_key = os.getenv("GENAI_API_KEY")

# Configure Gemini API key
genai.configure(api_key=genai_api_key)

def aiProcess(command):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(command, stream=True)

        full_response = ""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)  # Print chunk immediately
                full_response += chunk.text

        print("\n")
        return full_response if full_response else "Sorry, I couldn't process that."

    except Exception as ex:
        print(f"Error in AI processing: {ex}")
        return "There was an error processing your request."
