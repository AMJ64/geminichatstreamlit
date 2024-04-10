import streamlit as st
import google.generativeai as genai
import PIL.Image

def main():
    st.title("Simple Chatbot with Vision")
    
    # User input
    user_input = st.text_input("Type your message here:")
    
    # Image upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    
    # Button to submit the message
    submit_button = st.button("Send")
    
    # Placeholder for the chat history
    chat_history = st.empty()
    
    # Function to display the chat history
    def display_chat_history(user_input, image=None):
        # Configure the generative model
        genai.configure(api_key='AIzaSyBoBHDL2yCZucWFP2zKrbUimA8B90bhmps')
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate a response using the user's input as the prompt
        if image:
            # If an image is uploaded, use it along with the user's input
            chatbot_response = generate(user_input, image)
        else:
            # If no image is uploaded, only use the user's input
            chatbot_response = generate(user_input)
        
        chat_history.text(f"User: {user_input}")
        if image:
            chat_history.text(f"Chatbot: {chatbot_response} (based on the uploaded image)")
        else:
            chat_history.text(f"Chatbot: {chatbot_response}")
    
    # Function to generate content using the Gemini API
    def generate(prompt, image=None):
        model = genai.GenerativeModel('gemini-pro')
        model1 = genai.GenerativeModel('gemini-pro-vision')
        if image:
            # Assuming the model can accept both text and image inputs
            response = model1.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    
    # Check if the submit button is clicked
    if submit_button:
        if uploaded_file is not None:
            # Open the uploaded image
            image = PIL.Image.open(uploaded_file)
            display_chat_history(user_input, image)
        else:
            display_chat_history(user_input)

if __name__ == "__main__":
    main()
