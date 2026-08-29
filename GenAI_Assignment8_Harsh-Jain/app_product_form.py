import streamlit as st


inputText = st.sidebar.text_input("Enter Product Name:")
selectBox = st.sidebar.selectbox(label="Enter Product Category",options=["Electronics","Sports","Fashion","Household"])
priceText = st.sidebar.text_input("Enter Product Price:")

if st.sidebar.button("Add Product"):
    st.write("Success, Product has been added")
    st.write(f"Product Name:{inputText}, Product Caegory:{selectBox}, Product Price: {priceText}")