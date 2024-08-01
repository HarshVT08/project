import streamlit as st
import google.generativeai as genai

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Q&A Demo")

# Directly specify the API key (Note: This is not secure for production)
API_KEY = "AIzaSyCdyRawK0xn3ZDFQhEPtwlsUQfTRIhin7A"

# Print the API key to verify it's loaded correctly
st.write("API Key:", API_KEY)

# Configure the generative AI model with the API key
genai.configure(api_key=API_KEY)

# Function to get the response from the generative model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.header("Gemini Application")

# Text input field for the user question
user_input = st.text_input("Input:", key="input")

# Button to submit the question
submit = st.button("Ask the question")

# Print statements for debugging
st.write("User Input:", user_input)
st.write("Submit Button Clicked:", submit)

# If the ask button is clicked, get and display the response
if submit and user_input:
    try:
        response = get_gemini_response(user_input)
        st.write("API Response:", response)  # Print the API response for debugging
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")

