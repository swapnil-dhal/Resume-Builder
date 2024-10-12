import PyPDF2
import io

def extract_text_from_pdf(pdf_file):
    # Use the file-like object directly (pdf_file is the uploaded file, not a file path)
    with io.BytesIO(pdf_file.read()) as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text


def preprocess_resume_text(text):
    # Basic preprocessing like removing unnecessary line breaks and whitespaces
    clean_text = text.replace('\n', ' ').strip()
    return clean_text