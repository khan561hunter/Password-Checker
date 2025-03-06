import streamlit as st

st.set_page_config(page_title="Password Checker",layout="centered")

st.title("Password Checker")

password = st.text_input("Enter the password",type="password")

if st.button("Check"):
    if len(password) < 8:
        st.error("Password should be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        st.error("Password should contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        st.error("Password should contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        st.error("Password should contain at least one digit.")
    else:
        st.success("Password is strong")