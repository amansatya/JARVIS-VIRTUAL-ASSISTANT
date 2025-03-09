import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCvjgchi7OTfwSlDKGCSjgnPLQALWVXRoQ")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

# Generate response for a query
response = model.generate_content("What is coding?")

# Print response
print(response.text if response.text else "Sorry, I couldn't process that.")
