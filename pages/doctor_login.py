import streamlit as st
from streamlit_extras.switch_page_button import switch_page

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

home = st.button("Home page!")
if home:
    switch_page("Home")
def app():
    st.title("Doctor Login")
    choice = st.selectbox('Login/Sign Up',['Login','SignUp'])
    if choice=='Login':
        email=st.text_input("Email Address")
        passwrd=st.text_input("Password",type="password")
        st.button("Login")
    else:
        email=st.text_input("Email Address")
        passwrd=st.text_input("Password",type="password")
        username=st.text_input("Username") 
        st.button("Create my Account")
  
app()

