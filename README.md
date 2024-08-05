Capstone Project Streamlit Chatbot




Welcome to Project Momentum!

This project involves creating a prototype chatbot for SCL Industries using Streamlit and LangChain.

Getting Started
To set up and run the chatbot application, follow these steps:

Prerequisites
Python: Ensure you have Python 3.10.13 or higher installed on your machine.

Dependencies: Install the required Python packages. You can do this by running:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should include necessary packages such as streamlit, streamlit_chat, streamlit_extras, python-dotenv, langchain, transformers, torch, etc.

Setup
Environment Variables:

Create a .env file in the root directory of your project.
Add the following environment variables to the .env file:
plaintext
Copy code
TOKEN=<your_token>
EMBEDDINGS_MODEL_NAME=<your_embeddings_model_name>
PERSIST_DIRECTORY=<your_persist_directory>
MODEL_TYPE=<your_model_type>
MODEL_PATH=<your_model_path>
MODEL_N_CTX=<model_context_size>
MODEL_N_BATCH=<model_batch_size>
TARGET_SOURCE_CHUNKS=<source_chunks>
Configuration:

Create a .streamlit directory in your repository.
Download secrets.toml and config.toml files and place them in the .streamlit directory.
Run the Application:

Execute the following command to start the Streamlit application:
bash
Copy code
streamlit run your_script_name.py
Replace your_script_name.py with the name of the script file you have (e.g., app.py).
Usage
After running the application, navigate to the local server URL (usually http://localhost:8501) in your web browser.
Interact with the chatbot by entering queries in the provided input field.
Use the sidebar to read the terms and conditions, and find contact information.
Customization
Data: Modify the input directory and other configurations as per your specific use case in the .env file.
Model: You can switch to different models by adjusting the MODEL_TYPE and MODEL_PATH environment variables.
License
This project is licensed under the AGPL v3 License. See the LICENSE file for details.

Feel free to adjust any of the details as needed based on the specific requirements or additional configurations for your project.
