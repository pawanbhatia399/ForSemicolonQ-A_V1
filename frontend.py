import streamlit as st
from PyPDF2 import PdfReader
from config import THEME_CONFIG, STYLE_CONFIG
from io import BytesIO
import subprocess
import base64
from fpdf import FPDF
import nltk
from nltk.corpus import wordnet

def is_meaningful(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Check if at least one word has a synonym in WordNet
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            return True
    
    return False

def extract_text_from_pdf(file):
    pdf_text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

def execute_backend_script(text_data):
    # Call the backend script with the text data
    result = subprocess.run(["python", "backend.py", text_data], capture_output=True, text=True)
    return result.stdout.strip()

def main():
    # Set Page Configuration here
    st.set_page_config(**THEME_CONFIG)

    # Change the Theme Color
    st.markdown(STYLE_CONFIG, unsafe_allow_html=True)
    header = st.container()

    header.title("Question Generator Tool:pencil:")

    header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
    ### Custom CSS for the sticky header

   # st.title("Question Generator Tool:pencil:")
    st.subheader('''This tool helps you to generate questions based on the Texts/Paragraph provided as an input via PDF upload / Copy Paste in textbox.''')


    # File Upload Section
    st.header("PDF File Upload")
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if pdf_file is not None:
        st.success("File Uploaded Successfully!")

        # Display extracted text from PDF on submit
        if st.button("Extract Text from PDF"):
            pdf_text = extract_text_from_pdf(pdf_file)
            st.subheader("Text Extracted from PDF:")
            st.write(pdf_text)

            # Execute backend script with PDF text and display result
            if is_meaningful(pdf_text):
                backend_result = execute_backend_script(pdf_text)
                st.subheader("Backend Result:")
                st.write(backend_result)
            else:
                st.write("The input text is garbage or trash.")

    # Text Input Section
    st.header("Input Paragraph Section!")
    text_input = st.text_area("Enter Text Here : ", "")

     # Display entered text on submit
    if text_input: 
        #If not empty, enable the button
        button_disabled = False 
    else:
        button_disabled = True 
    # Create a button with the disabled parameter 
    button_clicked = st.button("Display Text", disabled=button_disabled)
    if button_clicked:
        st.subheader("Text Entered:")
        st.write(text_input)
        # Execute backend script with user text and display result
        if is_meaningful(text_input):
            backend_result = execute_backend_script(text_input)
            st.subheader("Backend Result:")
            st.write(backend_result)
        else:
            st.write("The input text is garbage or trash.")

        # questions = generate_questions(text_input)
        # st.subheader("Generated Questions: ")
        # for q in questions:
        #     st.write(q['question'])
    st.caption('''Our innovative tool enables users to effortlessly generate questions from texts or paragraphs by simply uploading a PDF file or copying and pasting the content into the designated text box. 
    This feature is particularly beneficial for educators, students, and anyone looking to enhance their reading comprehension skills by practicing with customized questions tailored to the specific text at hand. This will be helpful for Teachers / Students etc.''')
    st.info('Copyright © 2024 - Developed by 404 Found Team')

if __name__ == "__main__":
    main()