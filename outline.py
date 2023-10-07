import streamlit as st
from langchain.llms import OpenAI 
from langchain import PromptTemplate


st.set_page_config(page_title='🦜🔗 Leo\'s LLM App')
st.title('🦜🔗 Generate blog ideas')

openai_api_key = st.secrets["openai_key"]

def generate_response(input_text):
    llm = OpenAI(model_name='text-davinci-003', openai_api_key= openai_api_key)
    # set template and prompt 
    template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
    prompt = PromptTemplate(input_variables = ['topic'], template=template)
    prompt_query = prompt.format(topic=input_text)
    # run LLM model 
    respone = llm(prompt_query)
    return st.info(respone)


with st.form('blog_form'):
    topic_keywords = st.text_area('Input keywords:',"")
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please set your OpenAI API first on the backend.')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_keywords)









