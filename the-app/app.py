import streamlit as st

st.set_page_config(page_title="Password Checker",layout="centered")

st.title("Password Checker")

count = 0

password = st.text_input("Enter the password",type="password")

if st.button("Check"):
    if len(password) >= 8:
        count += 1
    else : 
        st.error("Password must be at least 8 characters long")
    if any(char.isupper() for char in password):
        count += 1
    else:
        st.error("Password must contain at least one uppercase letter")
    if any(char.islower() for char in password):
        count += 1
    else:
        st.error("Password must contain at least one uppercase letter")
    if any(char.isdigit() for char in password):
        count += 1
    else:
        st.error("Password must contain at least one number")
    if any(char in "!@#$%^&*()" for char in password):
        count += 1
    else:
        st.error("Password must contain at least one special character")
    if count == 5 :
        st.success("Password is strong")
    elif count == 4 or count == 3 :
        st.warning("Password is moderate")
    else:
        st.error("Password is weak")
st.write("The total count is : " ,count)
