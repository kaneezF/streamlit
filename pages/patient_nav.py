import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title="Patient",
        options=["Home" , "Prediction" , "Book an Ambulance" , "Make an Appointment" , "Contact Us" , "Log out"],
        icons=["house" , "clipboard-pulse" , "bus-front" , "file-earmark-plus" , "envelope" , "arrow-left-circle-fill"],
        menu_icon="clipboard-check-fill",
    )

    

