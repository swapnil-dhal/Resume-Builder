import google.generativeai as genai

# Directly hardcode the API key (Not recommended for production, but we can do if its a personal project)
api_key = "<YOUR-API-KEY>"

# Configure the Generative AI API with your API key
genai.configure(api_key=api_key)

# Specify the correct model name (check the API documentation for the exact name)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Estimate the maximum number of tokens for a single input (Gemini 1.5 Flash can handle ~4096 tokens)
MAX_TOKENS = 4000  # Adjust as needed based on the actual token limit

# Helper function to estimate the token count (approximated by characters)
def estimate_token_count(text):
    return len(text) // 4  # 1 token ≈ 4 characters

# Function to process the data
def process_data(cleandata, prompt):
    input_data = f"{prompt}\n Resume Text: {cleandata}"

    # Estimate how many tokens the input data will require
    total_tokens = estimate_token_count(input_data)
    
       # If the input data exceeds the token limit, split it into chunks
    if total_tokens > MAX_TOKENS:
        # Split the input_data into chunks based on the token limit
        chunks = [input_data[i:i + MAX_TOKENS * 4] for i in range(0, len(input_data), MAX_TOKENS * 4)]
    else:
        # If input data is within the limit, no need to split
        chunks = [input_data]


    # Store the parsed results
    parsed_result = []

    # Process each chunk
    for i, chunk in enumerate(chunks, start=1):
        print(f"Processing chunk {i} of {len(chunks)}...")
        response = model.generate_content(chunk)
        parsed_result.append(response.text)  # Assuming response.text contains the generated content

    # Return the concatenated results from all chunks
    return "\n".join(parsed_result)
