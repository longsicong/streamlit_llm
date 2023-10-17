import streamlit as st
import openai


st.set_page_config(page_title='🦜🔗 Transcription Tool')
st.title('🦜🔗 Audio2Text')

# openai.api_key = <API-KEY>
openai.api_key = st.sidebar.text_input('OpenAi API Key',type="password")

if not openai.api_key.startswith('sk-'):
    st.sidebar.info('Please input OpenAI API key started with "sk-"')

# Generate transcript 
# Ref: https://www.datacamp.com/tutorial/converting-speech-to-text-with-the-openAI-whisper-API 

def generate_transcript(audio_file):
    if audio_file is not None:
        response = openai.Audio.transcribe(
            file=audio_file, 
            model='whisper-1',
            response_format='srt', # or you can use "text"  
            # prompt = "这是关于广告的一段中文内容。请转写为中文。"# 
            language='zh'
            )
    if len(response):
        st.info(response)



with st.form('Transcription_form', clear_on_submit=True):
    audio_file = st.file_uploader("Upload an audio file", type=[".wave","wave",".flac",".mp3",".ogg"], accept_multiple_files=False)
    submitted = st.form_submit_button('Submit')
    if submitted and audio_file is not None:
        with st.spinner('Working in process ...'):
            generate_transcript(audio_file)
            






