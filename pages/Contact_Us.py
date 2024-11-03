from cProfile import label

import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    #st.write('Your email address ')
    email_input=st.text_input(label='Your email address',key='email')
    message_input=st.text_area(label='Your message',key='message')
    message = f'''Subject: New Email  
    
    From : {email_input}

    {message_input}'''
    submit_button=st.form_submit_button()
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully")