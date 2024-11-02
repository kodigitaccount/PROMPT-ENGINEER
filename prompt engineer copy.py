import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = ''  # Replace with your actual API key

def generate_response(prompt, model="gpt-3.5-turbo", max_length=150, temperature=0.7):
    try:
        # Create a chat completion request
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_length,
            temperature=temperature
        )
        # Extract and return the response content
        return response['choices'][0]['message']['content']
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app layout
st.title("Prompt Engineering with OpenAI")
st.write("Enter your prompt below and see how the model responds.")

# User input for the prompt
user_prompt = st.text_area("Prompt", height=200)

# Generate response button
if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("Generating response..."):
            response = generate_response(user_prompt)
            if response:
                st.subheader("Assistant's Response:")
                st.write(response)
    else:
        st.warning("Please enter a prompt before generating a response.")

# Optional: add footer or additional information
st.write("This app uses OpenAI's API to generate responses based on your prompts.")
