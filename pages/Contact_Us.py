from cProfile import label

import streamlit as st

st.header('Contact Me')

with st.form(key='email_form'):
    #st.write('Your email address ')
    email_input=st.text_input(label='Your email address',key='email')
    message_input=st.text_area(label='Your message',key='message')
    submit_button=st.form_submit_button()
    if submit_button:
        st.write()