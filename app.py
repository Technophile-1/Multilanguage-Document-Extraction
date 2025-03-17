### Health Management APP

from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# Configure Google Gemini Pro Vision API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input_text, image, prompt])
    return response.text

# Function to read the image and set the image format for Gemini Pro model input
def input_image_details(uploaded_file):
    image = Image.open(uploaded_file)
    image_data = uploaded_file.read()
    return image_data, image

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Decode: Multilanguage Document Extraction by Gemini-2.0-flash ")
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini-2.0-flash")

text = ("Utilizing Gemini-2.0-flash AI, this project effortlessly extracts vital information "
        "from diverse multilingual documents, transcending language barriers with "
        "precision and efficiency for enhanced productivity and decision-making.")
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# Streamlit UI components
input_prompt = """
You are an expert in understanding invoices.
We will upload an image as an invoice and you will have to answer any questions based on the uploaded invoice image.
"""

input_text = st.text_input("Input Prompt:", key="input", value=input_prompt)
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    image_data, image = input_image_details(uploaded_file)

    if st.button("Tell me about the document"):
        response_text = get_gemini_response(input_text, image, "Describe the document")
        st.subheader("The response is")
        st.write(response_text)