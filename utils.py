
# utils.py

import tempfile
import re
from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# Load the API key from Streamlit secrets
api_key = st.secrets['secrets']["API_KEY"]

# Initialize the Groq client
client = Groq(api_key=api_key)

# Initialize the Groq model for LLM responses
llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=api_key, max_tokens=500)  # Limit tokens to 100

def audio_bytes_to_wav(audio_bytes):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
            with open(temp_wav.name, "wb") as f:
                f.write(audio_bytes)
            return temp_wav.name
    except Exception as e:
        st.error(f"Error during WAV file conversion: {e}")
        return None
def speech_to_text(audio_bytes):
    try:
        temp_wav_path = audio_bytes_to_wav(audio_bytes)
        
        if temp_wav_path is None:
            return "Error"
        
        # Use Groq's Whisper API for transcription in English
        with open(temp_wav_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(temp_wav_path, file.read()),
                model="whisper-large-v3",
                response_format="text",
                language="en",  # Ensure language is set to English
                temperature=0.0
            )
    except Exception as e:
        st.error(f"Error during speech-to-text conversion: {e}")
        transcription = "Error"
    return transcription


def text_to_speech(text):
    try:
        # Enforce English language for text-to-speech
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            tts.save(f.name)
            audio = AudioSegment.from_mp3(f.name)
    except Exception as e:
        st.error(f"Error during text-to-speech conversion: {e}")
        # Return silent audio in case of error
        audio = AudioSegment.silent(duration=1000)
    return audio


def remove_punctuation(text):
    # Remove punctuation from the text
    return re.sub(r'[^\w\s]', '', text)

def get_llm_response(query, chat_history):
    try:
        # Updated template with detailed guidelines
        template = """
               You are a highly qualified female psychiatrist assistant chatbot named "Scoopsie" with extensive experience in mental health. Your role is to provide professional, empathetic, and culturally authentic advice and answers to the user's questions. You communicate using everyday language, incorporating local idioms and expressions while avoiding loanwords from other languages.

                Your expertise is exclusively in providing information and advice related to mental health. If a question falls outside the scope of mental health, you should respond with, "I specialize only in mental health-related queries."

                Key Considerations:

                Professionalism: Maintain a high level of expertise and ethical standards.
                Cultural Authenticity: Understand and reflect the values, beliefs, and customs relevant to the user’s cultural context.
                Empathy: Show genuine compassion and support for the user's emotional well-being.                 
                 **Chat History:** {chat_history}

                **User:** {user_query}

        """

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | llm | StrOutputParser()

        response_gen = chain.stream({
            "chat_history": chat_history,
            "user_query": query
        })

        # Combine all parts of the response and apply text clean-up
        response_text = ''.join(list(response_gen))
        response_text = remove_punctuation(response_text)

        # Remove repeated text
        response_lines = response_text.split('\n')
        unique_lines = list(dict.fromkeys(response_lines))  # Remove duplicates while preserving order
        cleaned_response = '\n'.join(unique_lines)

        return cleaned_response
    except Exception as e:
        st.error(f"Error during LLM response generation: {e}")
        return "Error"

def create_welcome_message():
    welcome_text = "Hello, I'm Scoopsie your chatbot assistant. How can I help you?"  #  greeting with female pronoun
    tts = gTTS(text=welcome_text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tts.save(f.name)
        return f.name



