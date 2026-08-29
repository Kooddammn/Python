import streamlit as st

st.write("Hello world")
st.title("Hello Streamlit")
st.header("Welcome to Streamlit")
st.subheader("This is sub header")
st.text("This is a plain text")

if st.button("Click me"):
    st.write("Button clicked")

agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")


level = st.slider("Select a leve",1,10,5)
st.write(level)

upload = st.file_uploader("Upload a file", type=["csv","txt"])
