import streamlit as st
from langchain.llms import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

def generate_response(input_text):
    #instantiate LLM 
    llm = OpenAI(temperature=0, openai_api_key = openai_api_key)
    # split text 
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(input_text)
    # create documents 
    docs = [Document(page_content=t) for t in texts]
    # text summarisation 
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

st.set_page_config(page_title='🦜🔗 Text Summarization')
st.title('🦜🔗 Text Summarization')

# text input 
txt_input = st.text_area('Enter your text:', '', height=200)

# form 

result = []


with st.form('Summarization_form', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not txt_input)
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner("Working in process ..."):
            response = generate_response(txt_input)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)



