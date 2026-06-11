import streamlit as st
from password_generator import RandomPassword, MemoryablePassword, PinPassword

st.set_page_config(
    page_title="Password Generator",
    page_icon="🔑",
    layout="wide",
)

password_type = st.selectbox(
"Type",
("Random Password", "Memoryable Password", "PIN Password"),
)

if password_type == "Random Password":
    user_length = st.slider("Characters", 8, 50, 12)
    numbers = st.toggle("Numbers")
    symbols = st.toggle("Symbols")
    generator = RandomPassword(
        length=user_length,
        include_digits=numbers,
        include_symbols=symbols
    )
elif password_type == "Memoryable Password":
    user_length = st.slider("Number of Words", min_value=10, max_value=75, value=16)
    capitalize = st.toggle("Include Capitalize")
    user_separator = st.text_input("Separator", value='-')
    generator = MemoryablePassword(
        number_of_words=user_length,
        capitalization=capitalize,
        separator=user_separator
    )
else:
    user_length = st.slider("Numbers", min_value=4, max_value=12, value=6)
    generator = PinPassword(length=user_length)

password = generator.generate()
st.write("#### Here is your password:")
st.header(fr"```{password}```")
