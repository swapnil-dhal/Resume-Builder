import streamlit as st
import back  # Importing back.py as a module
import process  # Importing process.py as a module

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Resume Scanner")

# Display the title of the web app
st.title("Resume Scanner")

# File uploader for the user to upload a PDF file
input_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Text area for the user to input the prompt (question)
prompt = st.text_area("What do you want to know?")

# Button to start processing the CV
if st.button("Process CV"):
    st.write("Please wait...")  # Show message that processing is ongoing
    
    if input_file is not None:
        # Extract the raw text from the PDF file using back.py
        raw = back.extract_text_from_pdf(input_file)
        
        # Preprocess the extracted text to clean it using back.py
        cleaned = back.preprocess_resume_text(raw)
        
        # Process the cleaned text with the provided prompt using process.py
        output1 = process.process_data(cleaned, prompt)

        # Show the processed result in an expandable section
        with st.expander("View Result"):
            st.text_area("Details:", value=output1, height=300)  # Show result in a text area
    else:
        st.warning("Please upload a resume to continue.")  # Handle the case when no file is uploaded
