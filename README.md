# Resume-Builder

In this project, I built a Resume Scanner app with the help of the Streamlit library, Google Gemini API, and PyPDF2 to convert the PDF file into text. Our AI model will process the text input, not the PDF files.

### Prerequisites:

- Python 3.12.6
- pip
- Python virtual environment (`venv`)
- **Google Gemini API Key**: You need to generate an API key for Google Gemini. Visit [Google Gemini API](https://ai.google.dev/) to generate the key.

### Steps to Set Up:

1. **Create a Directory for Your Project**

   - Example: `AI RESUME SCANNER`

2. **Navigate to the Project Directory**

   ```bash
   cd /path/to/AI RESUME SCANNER

   ```

3. **Create a Virtual Environment for the Project**

   - a. For windows system:

   ```bash
          python -m venv nameofyourenvironment
          nameofyourenvironment\Scripts\activate
   ```

   - b. For Mac/Linux(Ubuntu):

   ```bash
         python3 -m venv nameofyourenvironment
         source nameofyourenvironment/bin/activate
   ```

4. **Install Dependencies**

   - a. For windows system:

   ```bash
        pip install -r dependencies.txt
   ```

   - b For Mac/Linux(Ubuntu):

   ```bash
        pip3 install -r dependencies.txt
   ```

5. **Change the Google Gemini API Key in process.py**
   Open process.py and replace the placeholder API key with the API key you generated from the Google Gemini API website.
   import google.generativeai as genai
   import os

# Replace with your actual API key

    api_key = "YOUR_ACTUAL_GOOGLE_GEMINI_API_KEY"
    genai.configure(api_key=api_key)

6. **Run the Application Using Streamlit**

   ```bash
            streamlit run main.py
   ```

   - If you're running on AWS EC2 or any cloud service, configure the server port and address. By default, Streamlit runs on port 8501, but you may need to redirect it to 0.0.0.0 to allow access from outside your local machine.

   ```bash
            streamlit run main.py --server.address=0.0.0.0 --server.port=8501
   ```
