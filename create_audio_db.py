import streamlit as st
import pyttsx3

# Command to execute
command = "apt-get install espeak"
# Execute the command
output = subprocess.check_output(command, shell=True).decode("utf-8")

def get_engine(rate, volume, voice):

    # initialize pyttsx3 engine
    engine = pyttsx3.init("espeak")

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    if voice == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    return engine

# define Streamlit app
def app():
    # create sidebar
    st.sidebar.header("Voice Settings")
    rate = st.sidebar.slider("Rate", min_value=40, max_value=500, value=100, step=10)
    volume = st.sidebar.slider("Volume", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    voice = st.sidebar.radio("Voice", options=['Male', 'Female'])

    # create main app
    st.title("Text to Speech App")
    st.write("Enter text and press the button to hear it spoken.")

    # create text input and button
    text = st.text_input("Text to speak")
    if st.button("Speak"):
        # get pyttsx3 engine based on user settings
        engine = get_engine(rate, volume, voice)
        # speak text
        engine.say(text)
        engine.runAndWait()

if __name__ == '__main__':
    app()