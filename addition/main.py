import streamlit as st
import datetime

from addition.gc_funtion import create_patient
from deletion.main import delete_patient


def add_patient():    

    # Empty space
    st.write("#")

    # Title
    st.markdown("<h1 style='text-align: center; color: darkblue;'>New Patients Creator</h1>", unsafe_allow_html=True)
    
    # Empty space
    st.write("#")

    # First and Last Name
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("Enter First Name")
    with col2:
        last_name = st.text_input("Enter Last Name")

    # Empty space
    st.write("#")

    # Gender, Birthdate, Email
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        birthdate = st.date_input("Birthdate",
                                min_value=datetime.date(1923,1,1),
                                max_value=datetime.date.today(),
                                )
    with col3:
        email = st.text_input("Enter Email")

    # Empty space
    st.write("#")

    # Create Patient button
    col1, col2, col3 = st.columns(3, gap="large")
    with col2:
        button = st.button("Create Patient", key="create_patient_button")

    if button:
        
        if first_name and last_name and gender and birthdate and email:
            try:
                st.session_state.patient_id = create_patient(first_name, last_name, gender, str(birthdate), email)
                st.success("Patient created successfully")
                st.session_state.delete_button_visible = True
                
            except:
                st.error("Ooops! Patient not created. Try again please")
                st.session_state.delete_button_visible = False


        else:
            st.error("You must fill all the form!")
            st.session_state.delete_button_visible = False
        

    if st.session_state.delete_button_visible and st.session_state.patient_id != "":
        # Here appears the option to delete this patient!
        st.info("You can delete this created patient by clicking on the button below!")
        if st.button("Delete Patient"):
            delete_patient(st.session_state.patient_id)
            st.success("Patient removed successfully")
            st.session_state.delete_button_visible = False
            st.session_state.patient_id = ""