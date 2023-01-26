import streamlit as st
import pandas


st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.png", width=350)

with col2:
    st.title("Ogeti Jyothika")
    content  = """ Hi, I am Ogeti Jyothika. I am a Python programmer. Currently I am studying in BSC Computer science final year 
     in Avanthi degree & Pg college, Hyderabad.I love to code.
    """
    content1 = "This is a Portfolio website to showcase my Python projects."
    st.info(content)
    st.info(content1)

st.write("Below you can find some of the apps I have built in Python.Feel free to contact me!")

col3, empty_col,  col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        #st.write("[Source code](www.google.com)")
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        st.write(f"[Source Code]({rows['url']})")





