import streamlit as st
from number_to_word import number_to_word


st.divider()
st.title("🔢 Number to Word")
user_input = st.number_input("Enter your number", min_value=1, max_value=int(1e15))

ntw = number_to_word(user_input)
st.write("")
st.header(fr"```{ntw}```")
st.divider()
