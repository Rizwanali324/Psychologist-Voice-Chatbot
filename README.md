# AI Voice Psychologist Chatbot
## Project Demo

Check out the demo of our project:

[![Watch the video](https://img.youtube.com/vi/JRpbZZf2HfM/0.jpg)](https://youtu.be/JRpbZZf2HfM)

This AI-based psychologist chatbot offers users an interactive and engaging platform for voice-based communication. Using advanced natural language processing (NLP) techniques and machine learning, the chatbot simulates a conversation with a psychologist, providing insights and responses to user inputs.
![Voice Chatbot](https://github.com/Rizwanali324/Psychologist-Voice-Chatbot/blob/main/vioce%20chatbot.png)

## Features
- **Voice Recognition**: Users can interact with the chatbot via voice inputs.
- **NLP-based Conversations**: The chatbot processes and understands user speech to generate thoughtful responses.
- **Psychological Assessments**: The system is trained to provide conversational assistance related to mental health.
- **User-Friendly Interface**: Powered by Streamlit for an easy-to-use web interface.
  
## Live Demo

You can access the live version of the AI Voice Psychologist Chatbot here:  
**[AI Voice Psychologist Chatbot - Live Demo](https://tec-psychologists.streamlit.app/)**
### Project Structure

```bash
Psychologist-Voice-Chatbot/
│
├── .streamlit/            # Contains secrets.toml for storing API keys
│   └── secrets.toml
├── app.py                 # Main Streamlit app file
├── requirements.txt       # List of dependencies to install
├── README.md 
├── README.md   # Project documentation (this file)
└── utils.py    # Other project-specific files and folders

```
## Setup Instructions

### 1. Clone the Repository

To get started with the project locally, clone the repository to your machine:

```bash
git clone https://github.com/Rizwanali324/Psychologist-Voice-Chatbot.git
cd Psychologist-Voice-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt

```
### 4. Configure the Groq API Key
The application uses the Groq API for some of its functionalities. Follow these steps to configure the API key
Go to the Groq Console and create an API key.

Create a folder named .streamlit in the root directory of your project:
```bash

mkdir .streamlit
```
Inside the .streamlit folder, create a file named secrets.toml and add your Groq API key in the following format:
```bash

[secert]
api_key = "your_groq_api_key_here"
```
### 5. Run the Streamlit Application
Once the API key is set up and the dependencies are installed, you can run the chatbot locally using Streamlit:


```bash

streamlit run app.py

```
This will launch the chatbot in your default web browser.


