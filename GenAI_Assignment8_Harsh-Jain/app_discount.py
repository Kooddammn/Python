import streamlit as st


originalPrice = st.number_input("Original Price")
finalPrice = originalPrice
discount = st.slider("Discount :" ,1,50)
if st.button("Calculate Discount"):
    finalPrice = originalPrice - (originalPrice * discount/100)
    st.write(finalPrice)

