from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the library with the API key
genai.configure(api_key=GOOGLE_API_KEY)

def main():
    st.title('Content Generator')

    prompt = st.text_input('Enter your prompt:')
    points = st.number_input('Points:', min_value=5)
    if st.button('Generate Content'):
        generated_content = generate_content(f"Write a product description in bullet points for'{prompt}' in {points} points")
        st.subheader('Generated Content:')
        st.write(generated_content)
     
def generate_content(prompt):
    model = genai.GenerativeModel(model_name='gemini-pro')
    response = model.generate_content(prompt)
    result = response.text
    return result

if __name__ == '__main__':
    main()
