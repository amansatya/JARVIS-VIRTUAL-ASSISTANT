import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

# Generate response for a query
response = model.generate_content("What is coding?")

# Print response
print(response.text if response.text else "Sorry, I couldn't process that.")
