import streamlit as st

st.title("Welcome to Python website")

name = st.text_input("Enter your name:")
fathername = st.text_input("Enter your Father name:")
address = st.text_area("Enter your Address:")

classdata = st.selectbox("Enter your Skills Level: ", (1, 2, 3, 4, 5, 6))

button = st.button("Done")
if button:
    info_text = f"Name: {name}\nFather's Name: {fathername}\nAddress: {address}\nSkills Level: {classdata}"
    st.markdown(info_text)