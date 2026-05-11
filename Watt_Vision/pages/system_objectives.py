import streamlit as st
from styles.header_text import styled_header
from styles.glowing_line import draw_glowing_line
from styles.normal_text import normal_text,display_aesthetic_subheader
from styles.gaping import remove_vertical_gap

def display_system_objectives():

    styled_header("Watt Vision : AI")
    draw_glowing_line()

    st.markdown("<br><br>",unsafe_allow_html=True)
    display_aesthetic_subheader("System Objectives :")
    st.write("---")

    text = "~ Neural Disaggregation :" 
    normal_text(text)
    remove_vertical_gap()
    text = "To decompose complex aggregate power signals " \
    "into individual appliance signatures using high-precision XGBoost " \
    "architectures, achieving real-time transparency across the domestic energy" \
    " grid."
    normal_text(text)
    st.write("---")

    text = "~ Transient Intelligence :"
    normal_text(text)
    remove_vertical_gap()
    text = "To monitor granular electrical transients—capturing" \
    " fluctuations, Voltage, and Power Factor—to identify the unique " \
    "'electrical heartbeat' of every connected asset with sub-millisecond accuracy."
    normal_text(text)
    st.write("---")

    text = "~ Cognitive Visualization :"
    normal_text(text)
    remove_vertical_gap()
    text = " To bridge the gap between raw data " \
    "and human insight by transforming invisible energy streams into a " \
    "high-fidelity visual narrative, empowering autonomous and informed " \
    "consumption management."
    normal_text(text)
    draw_glowing_line()

    normal_text("~ By Samrat Malla")








    