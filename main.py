import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Priyanka Tangade")
    content="""
    Hi, I am Priyanka Tangade and I am a Devops Engineer working with reputed organiztion
    I like travelling and trying out new things.
    Hello all, how are you today.
    Its such a Pretty day!
    """
    st.info(content)
content="Below you can find some of the apps I have built in Python. Feel Free to contact me for any help you require in python!"
st.write(content)

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")
with col3:
  for index,row in df[:10].iterrows():
    st.header(row["title"])
    st.write(row["description"])
    st.image("images/"+row["image"])
    st.write(f"[Source code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source code]({row['url']})")



