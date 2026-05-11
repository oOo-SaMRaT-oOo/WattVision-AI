# py -m streamlit run web_app.py

import streamlit as st
import joblib
from styles.sidebar import custom_sidebar
from pages.vision_terminal import vision_terminal_loading
from pages.system_objectives import display_system_objectives
from pages.about_author import display_about_author

options = custom_sidebar()


@st.cache_resource
def load_all_models():
    return {
        "Fridge":joblib.load("models/fridge_model.pkl"),
        "Kettle":joblib.load("models/kettle_model.pkl"),
        "TV":joblib.load("models/tv_model.pkl"),
        "Microwave":joblib.load("models/microwave_model.pkl"),
        "Washing_Machine":joblib.load("models/washing_machine_model.pkl")

    }

models_dict = load_all_models()


if options == "VISION  \nTERMINAL" :

    vision_terminal_loading(models_dict)

if options == "SYSTEM OBJECTIVES":

    display_system_objectives()

if options =="ABOUT  \nAUTHOR":

    display_about_author()
                
            



