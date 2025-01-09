import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1,col2=st.columns(2)

with col1:
    st.image("images/jasmin.jpg",width=600)

with col2:
    st.title("Yasmina NASRI")
    content = """
    Hi, I am Yasmina ! I am a Software programmer with four years of experience 
    with a background in Oracle forms and reports and PL/SQL and a solid 
    understanding of software development principles. Recently completed 
    upskilling focusing on Python and Web development, 
    with coursework in HTML, CSS, JavaScript, Networking, and IT Technical 
    Support. You can find me exploring new technologies, 
    contributing to open-source projects. I’m always eager to learn and 
    take on new challenges in the tech world. 
    """

    st.info(content)
content2="""Below you can find some of the apps I have built in Python. Feel free to browse my portfolio and reach 
out if you’d like to collaborate or just chat about all things web development!"""
st.write(content2)

#we add third column(empty_col) to have some space between col3 and col4
#we changed the parameter for st.columns, instead of a number(2) we put a list of float, each float represents the ratio dimension of each col(first col will be 3 times older that second col
col3,empty_col,col4=st.columns([1.5, 0.5, 1.5])
with col3:
    df=pandas.read_csv('data.csv',sep=';')
    for index,row in df[:7].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    df=pandas.read_csv('data.csv',sep=';')
    for index,row in df[8:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")