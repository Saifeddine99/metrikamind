import streamlit as st


from home_page.plots import time_series_plot
from search import query_patients, query_scores


# Function to get patient id by name and email
def get_patient_id(index, patient_ids):
    index_int = int(index)
    return patient_ids[index_int]



def dashboard():

    full_names, telecoms, patient_ids = query_patients()

    patients_list_without_id = []
    for index, item in enumerate(full_names):
        patient = str(index + 1) + ": " + item + " (" + telecoms[index] + ")"
        patients_list_without_id.append(patient)

    st.write("#")

    #Here we ask user to choose the Patient
    st.title("Patients List:")

    selected_patient = st.selectbox("Select a patient", patients_list_without_id, index = None)
    st.write("#")

    if selected_patient:
        # Here we'll extract the "id" of the selected patient
        index, patient_details = selected_patient.split(": ")
        patient_id = get_patient_id(index, patient_ids)
        #st.write("id: ", patient_id)

        all_responses_with_titles = query_scores(patient_id)
        
        if all_responses_with_titles:
            time_series_plot(all_responses_with_titles)

        else:
            st.error(f"You don't have any value stored in database")

    else:
        st.error("You need to choose a patient!")