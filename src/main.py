import os
import shutil
import sys
import json
import warnings
import time 
import streamlit as st
import re
import base64
import requests
from context_retrieval import  ContextRetrieval
from callservice import send_api
# 


warnings.filterwarnings("ignore")
st.title("SuperAI ss4")

retrieval = ContextRetrieval('./index/')
def main():
    
    # Initialize session state variables
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Type your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                message_placeholder = st.empty()
                prompt= retrieval(st.session_state.messages[-1]['content'])
                full_response = send_api(prompt=prompt['prompt'])['content']
                message_placeholder.markdown(full_response)
                message_placeholder = st.empty()

              
                            

        st.session_state.messages.append({"role": "assistant", "content":full_response})
    

if __name__ == '__main__':
    main()