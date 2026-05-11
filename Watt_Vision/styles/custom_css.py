import streamlit as st

def button_css():

    st.markdown("""
    <style>

    /* DOWNLOAD FONT */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&display=swap');

    /* REMOVE EXTRA TOP/BOTTOM SPACE */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;

        margin-top: 0px !important;
        margin-bottom: 0px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    /* REMOVE STREAMLIT BLOCK SPACING */
    div.element-container:has(div[data-testid="stButton"]) {
        margin-top: 0rem !important;
        margin-bottom: 0rem !important;
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }

    /* ACTUAL BUTTON */
    div[data-testid="stButton"] > button {

        width: 200px !important;
        height: 90px !important;

        border-radius: 50px !important;

        background: #010101 !important;
        color: #00ffcc !important;

        border: 2px solid #00ffcc !important;

        font-family: 'Orbitron', sans-serif !important;
        font-size: 28px !important;
        font-weight: 700 !important;

        letter-spacing: 2px !important;

        box-shadow:
            0 0 10px rgba(0,255,204,0.3),
            0 0 20px rgba(0,255,204,0.15);

        transition: all 0.35s ease !important;
    }

    /* HOVER */
    div[data-testid="stButton"] > button:hover {

        color: white !important;
        border: 2px solid white !important;

        transform: scale(1.05);

        box-shadow:
            0 0 15px #00ffcc,
            0 0 35px rgba(0,255,204,0.7),
            0 0 70px rgba(0,255,204,0.4);
    }

    </style>
    """, unsafe_allow_html=True)