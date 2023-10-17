import streamlit as st 
import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Api-Key XXXXXXXXXXXX',
}

# Now, you can access the 'choices' or other fields from the response_data
st.title('🦜🔗 Keyword.ai Demo')
# text input 



def generate_response(prompt):
    data = {
    'messages': [{'role': 'user', 'content': prompt}],}
    #instantiate LLM 
    response = requests.post('https://keywordsapi.info/api/generate/', headers=headers, json=data)
    result = ""
    if response.status_code == 200:
        # Parse the JSON from the response
        result = response.json()['choices'][0]['message']['content']
    else:
        result= {response.status_code} + "The 'choices' field was not found in the response."
    return st.info(result) 



with st.form('Response'):
    prompt = st.text_area('Enter your text:', '', height=200)
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(prompt)



# [{'index': 0, 
# 'message': {'role': 'assistant', 
# 'content': '"The Impact of Artificial Intelligence (AI) on SEO: Maximizing Website Visibility and Performance"'}, 
# 'finish_reason': 'stop'}]

