import streamlit as st
from streamlit_option_menu import option_menu


from home_page.main import dashboard
from addition.main import add_patient


from PIL import Image
img=Image.open('metrikamind.jpeg')

st.set_page_config(page_title = "Metrika Mind", page_icon = img, layout = "wide")

col1, col2, col3 = st.columns([1,3,1])
with col2:
    selected=option_menu(
        menu_title=None,
        options=["Home", "Create Patient"],
        icons=["house", "search"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        
        styles={
                    "container": {"margin": "0px !important","padding": "0!important", "align-items": "stretch", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "18px",
                        "text-align": "center",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
    )


if "delete_button_visible" not in st.session_state:
    st.session_state.delete_button_visible = False

if "patient_id" not in st.session_state:
    st.session_state.patient_id = ""

if selected=="Home":
    st.session_state.delete_button_visible = False
    st.session_state.patient_id = ""
    dashboard()

if selected=="Create Patient":
    add_patient()