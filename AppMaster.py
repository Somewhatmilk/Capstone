import streamlit as st
from streamlit_chat import message
import time
# from streamlit_extras.add_vertical_space import add_vertical_space
# import subprocess
# import numpy as np
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader
import openai
import random
import string
import os
import speech_recognition as sr
import json



def check_terms_and_conditions():
    st.markdown('''
            *Introduction:*\n
            Welcome to the SCL System Customer Service Chatbot! Before you engage with our chatbot, please take a moment to review and understand the following terms and conditions. Your use of the chatbot implies your agreement to comply with these terms.

            *Capabilities:*
            1. *Informational Assistance:* The chatbot is designed to offer information and assistance related to our products and services.
            2. *Query Resolution:* It can help address common queries, guide you through processes, and provide relevant information.
            3. *Limited Personalization:* The chatbot may use minimal personal information to enhance user experience but does not store or process sensitive data.

            *Restrictions:*
            1. *No Legal Advice:* The chatbot does not provide legal advice or opinions. For legal matters, consult a professional.
            2. *Limited Scope:* The chatbot's capabilities are confined to predefined tasks and information related to our products and services.
            3. *No Financial Transactions:* The chatbot does not facilitate or process financial transactions. Please use our official channels for such transactions.

            *Data Usage and Privacy:*
            1. *Data Collection:* The chatbot may collect limited personal information to improve user experience and address queries. This data is handled according to our privacy policy.
            2. *Security Measures:* We employ security measures to safeguard the data collected by the chatbot. However, avoid sharing sensitive personal information.

            *Consent:*
            1. *Express Consent:* Before collecting any sensitive data or using it beyond the chatbot's scope, we will seek your express consent.
            2. *Opt-out Option:* You can opt-out of sharing information or terminate the chat at any time.

            *Liability:*
            1. *No Guarantees:* While the chatbot aims for accuracy, we do not guarantee its completeness or accuracy.
            2. *Limited Liability:* We are not liable for any loss or damage resulting from the use of the chatbot.

            Link Warning:
            Warning: The link generated by the chatbot is provided without liability.             

            *Termination:*
            We reserve the right to terminate or suspend chatbot services without notice.

            *Updates:*
            These terms and conditions may be updated periodically. Your continued use of the chatbot implies acceptance of the latest version.

            By using our Customer Service Chatbot, you acknowledge that you have read, understood, and agreed to these terms and conditions. 
            If you disagree, please refrain from using the chatbot. For questions or concerns, contact our customer support through official channels.

            Contact Us:\n
            SCL System Enterprise Pte Ltd,
            41 Jalan Pemimpin,
            #02-01A Kong Beng Industrial Building,
            Singapore 577186

            Phone/WhatsApp: +65-62599968

            Fax: +65-62599282

            Email: sales@sclsystem.com.sg

            Copyright © 2023 SCL SystemTerms & Conditions | Privacy Policy
            ''')

    # Check if the user has agreed to the terms and conditions
    agreed_to_terms = st.checkbox("I have read and agree to the Terms and Conditions")

    if agreed_to_terms:
        st.success("Thank you for agreeing to the Terms and Conditions. You can now access the chatbot.")
        return True
    else:
        st.warning("Please read and agree to the Terms and Conditions before accessing the chatbot.")
        return False

if check_terms_and_conditions():
    
    st.title("SCL System Customer Service Chatbot")

    with st.sidebar:
        st.title('🤗💬 SCL System Customer Service Chatbot')

        # Create an expander widget for the terms and conditions
        with st.expander("Chatbot Terms and Conditions"):
            st.write('''
            *Introduction:*
            Welcome to the SCL System Customer Service Chatbot! Before you engage with our chatbot, please take a moment to review and understand the following terms and conditions. Your use of the chatbot implies your agreement to comply with these terms.

            *Capabilities:*
            1. *Informational Assistance:* The chatbot is designed to offer information and assistance related to our products and services.
            2. *Query Resolution:* It can help address common queries, guide you through processes, and provide relevant information.
            3. *Limited Personalization:* The chatbot may use minimal personal information to enhance user experience but does not store or process sensitive data.

            *Restrictions:*
            1. *No Legal Advice:* The chatbot does not provide legal advice or opinions. For legal matters, consult a professional.
            2. *Limited Scope:* The chatbot's capabilities are confined to predefined tasks and information related to our products and services.
            3. *No Financial Transactions:* The chatbot does not facilitate or process financial transactions. Please use our official channels for such transactions.

            *Data Usage and Privacy:*
            1. *Data Collection:* The chatbot may collect limited personal information to improve user experience and address queries. This data is handled according to our privacy policy.
            2. *Security Measures:* We employ security measures to safeguard the data collected by the chatbot. However, avoid sharing sensitive personal information.

            *Consent:*
            1. *Express Consent:* Before collecting any sensitive data or using it beyond the chatbot's scope, we will seek your express consent.
            2. *Opt-out Option:* You can opt-out of sharing information or terminate the chat at any time.

            *Liability:*
            1. *No Guarantees:* While the chatbot aims for accuracy, we do not guarantee its completeness or accuracy.
            2. *Limited Liability:* We are not liable for any loss or damage resulting from the use of the chatbot.

            Link Warning:
            Warning: The link generated by the chatbot is provided without liability.             

            *Termination:*
            We reserve the right to terminate or suspend chatbot services without notice.

            *Updates:*
            These terms and conditions may be updated periodically. Your continued use of the chatbot implies acceptance of the latest version.

            By using our Customer Service Chatbot, you acknowledge that you have read, understood, and agreed to these terms and conditions. 
            If you disagree, please refrain from using the chatbot. For questions or concerns, contact our customer support through official channels.

            Contact Us
            SCL System Enterprise Pte Ltd,
            41 Jalan Pemimpin,
            #02-01A Kong Beng Industrial Building,
            Singapore 577186

            Phone/WhatsApp: +65-62599968

            Fax: +65-62599282

            Email: sales@sclsystem.com.sg

            Copyright © 2023 SCL SystemTerms & Conditions | Privacy Policy
            ''')
    

    with st.sidebar.expander('Products'):
        st.write("Our product is Enclosure Boxes")
        st.write("4 screws: S series")
        st.write("Hinge and Type: P series")
        st.write("You are able to key in the Specification and Model and Size")




    with st.sidebar.expander("Contact Us"):
        st.title("SCL System Enterprise Pte Ltd")
        st.write("41 Jalan Pemimpin,")
        st.write("#02-01A Kong Beng Industrial Building,")
        st.write("Singapore 577186")
        
        st.subheader("Contact Details:")
        st.write("Phone/WhatsApp: +65-62599968")
        st.write("Fax: +65-62599282")
        st.write("Email: sales@sclsystem.com.sg")



    openai.api_key = st.secrets["OPENAI_API_KEY"]

    if "messages" not in st.session_state.keys(): # Initialize the chat message history
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi, I am Kafka, your personal assistant, ask me any question about SCL System Products!"}
        ]
        with st.expander("messages History"):
            st.session_state.prompt = ""

    @st.cache_resource(show_spinner=False)
    def load_data():
        with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take a few seconds."):
            reader = SimpleDirectoryReader(input_dir=r"C:\Users\gohji\OneDrive\Documents\Chatbot (test version)\Industial data draft", recursive=True)
            docs = reader.load_data()
            service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an sales and customer service employee. You are an expert with 23 years of experience and knowledge in industrial control and automation components. It is your responsibility to figure out what the client wants.Do not be bias and Keep your answers technical and straight to the point based on reputable sources – do not hallucinate features."))
            index = VectorStoreIndex.from_documents(docs, service_context=service_context)
            return index

    index = load_data()

    chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)



        
    if prompt := st.chat_input("Your Inquries"): # Prompt for user input and save to chat history
        user = st.session_state.messages.append({"role": "user", "content": prompt})

    # st.sidebar.button('Clear Chat History', on_click=clear_chat_history)
        

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])
            

    # If last message is not from assistant, generate a new response
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)  # Add response to message history


    # Add a checkbox to allow the user to enable or disable chat log saving
    save_log_checkbox = st.button("Save Chat Log", key="save_log_checkbox")

    # Create a placeholder for the chat log display
    chat_log_placeholder = st.empty()

    # Define the function to save chat logs individually
    def save_chat_log(message):
        log_file_path = f"chat_log_{time.time()}.json"  # Use a timestamp in the file name
        
        # Save the message to the file if the checkbox is selected
        if save_log_checkbox:
            with open(log_file_path, "w", encoding="utf-8") as log_file:
                json.dump(message, log_file, indent=2)


    def clear_chat_history():
        if save_log_checkbox:  # Save chat log only if the checkbox is selected
            save_chat_log(st.session_state.messages)

        st.session_state.messages = [
            {"role": "assistant", "content": "Hi, I am Kafka, your personal assistant, ask me any question about SCL System Products!"}
        ]
        st.session_state.prompt = ""
        st.session_state.generated = []
        st.write("Chat history fully cleared.")




    st.button("Clear History", key="clear_history", on_click=clear_chat_history)

    with st.sidebar:
        st.title('Chatbot History')

        # Create an expander widget for the chat log history
        with st.expander("Chatbot History"):

            # Create a container for the chat log widget
            chat_log_widget = st.container()

            for message in st.session_state.messages:
                with chat_log_widget:  # Use the container for the chat log widget
                    with st.chat_message(message["role"]):
                        st.write(message["content"])







    #def voice_recognition():
        #recognizer = sr.Recognizer()
        
        #with sr.Microphone() as source:
            #st.write("Say something...")
            #st.audio("path/to/audio_file.wav")  # This line is optional if you want to play a sound indicating voice input
            #audio = recognizer.listen(source)
            #st.write("Got it! Processing...")
            
            #try:
                #text_input = recognizer.recognize_google(audio)
                #st.session_state.messages.append({"role": "user", "content": text_input})
                
                # Use OpenAI to generate a response based on the user's input
                #response = chat_engine.chat(text_input)
                #st.write(response.response)
                #message = {"role": "assistant", "content": response.response}
                #st.session_state.messages.append(message)
            #except sr.UnknownValueError as e:
                #st.write(f"Sorry, I couldn't understand that. Error: {e}")
            #except sr.RequestError as e:
                #st.write(f"Error connecting to Google Speech Recognition API. Error: {e}")

    # Button to trigger voice recognition
    #if st.button("Start Voice Recognition"):
        #voice_recognition()


    # Display the last 'show_last' messages in the chat history
    #show_last = st.number_input("Show last messages:", step=1, max_value=len(st.session_state.messages), min_value=1, value=min(10, len(st.session_state.messages)), key="slice")

    # Reverse the loop to display messages in reverse order
    #for i in range(-1, -show_last - 1, -1):
    #with st.container():
            #st.text(st.session_state.messages[i]["role"])
            #st.text(st.session_state.messages[i]["content"])

