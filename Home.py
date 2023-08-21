import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

pg_bg_color="""
<style>
[data-testid=stAppViewContainer]{
    background-color:white;
}
</style>
"""
st.markdown(pg_bg_color , unsafe_allow_html=True)
col1, col2, col3  = st.columns([2,2,2])

with col1:
    
    st.image("pages/patient.png")
    patient = st.button("Patient's Registration")
    if patient:
        switch_page("newlogin")
   
with col2:
  
    st.image("pages/doctor.png")
    doctor = st.button("Doctor's Registration")
    if doctor:
        switch_page("doctor_login")

with col3:
    
    st.image("pages/ambulance.jpg")
    patient = st.button("Ambulance Registration")
    if patient:
        switch_page("patient_login")
