import streamlit as st

st.set_page_config(layout='wide')
col1,col2=st.columns(2)

with col1:
    st.image("images/jasmin.jpg",width=600)

with col2:
    st.title("Yasmina NASRI")
    content = """
    Hi, I am Yasmina ! I am a python programmer. Graduated in 2011 with a Master in Communication systems from National school of engineers of Tunis.
    I worked as a software programmer with four years of experience with a background in Oracle forms and reports and PL/SQL and a solid understanding
    of software development principles.Recently completed upskilling focusing on Python and Web development, with coursework in HTML, CSS, JavaScript,
    Angular, and mobile development. You can find me exploring new technologies, contributing to open-source projects. I’m always eager to learn and 
    take on new challenges in the tech world. Feel free to browse my portfolio and reach out if you’d like to collaborate or just chat about all things web development!
    """

    st.info(content)
