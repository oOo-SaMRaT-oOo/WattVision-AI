import streamlit as st

def intro_text(content: str):
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .intro-text-container {{
            font-family: 'Dancing Script', cursive, serif !important;
            font-size: 32px !important;
            color: #FFFFFF !important;
            line-height: 1.6;
            margin: 30px 0px;
            
            /* High visibility against moving blobs */
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
            
            /* Entry Animation */
            opacity: 0;
            animation: slideIn 1.5s ease-out forwards;
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .highlight-orange {{
            color: #F39C12 !important;
            font-weight: bold;
        }}
    </style>

    <div class="intro-text-container">
        {content}
    </div>
    """, unsafe_allow_html=True)


def normal_text(content: str):
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .intro-text-container {{
            font-family: 'Dancing Script', cursive, serif !important;
            font-size: 32px !important;
            color: #FFFFFF !important;
            line-height: 1.6;
            margin: 30px 0px;
            
            /* High visibility against moving blobs */
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
            
            /* Entry Animation */
            opacity: 0;
            animation: slideIn 1.5s ease-out forwards;
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .highlight-orange {{
            color: #F39C12 !important;
            font-weight: bold;
        }}
    </style>

    <div class="intro-text-container">
        {content}
    </div>
    """, unsafe_allow_html=True)


def display_my_intro():

    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.intro-text {
    font-family: 'Monotype Corsiva', cursive;
    font-size: 25px;
    color: #ffffff;
    line-height: 1;
    text-align: left;
    opacity: 0;
    transform: translateX(-100px);
    animation: slideIn 1.8s ease-out forwards, glow 3s ease-in-out infinite alternate 1.8s;
}

@keyframes slideIn {
    to { opacity: 1; transform: translateX(0); }
}



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="intro-text"><span style="color:#F39C12;">
            In a Nutshell,</span><br>
            I’m an Electrical Engineering student who loves building real solutions through 
the blend of hardware, software, and creative engineering.  
I work with Python, simulations, and analytical thinking to understand systems, 
solve real-world problems, and design ideas that actually work.  
Every day, I’m learning, experimenting, and shaping myself into a software-based 
engineer ready for the future I’m building.
</div>
""", unsafe_allow_html=True)
    

def display_aesthetic_subheader(text_input):
    """
    Renders a large, glowing, cursive subheader with a slide-in animation.
    """
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .subheading {{
        font-family: 'Great Vibes', cursive !important;
        font-size: 45px !important; 
        line-height: 1.2;
        margin: 10px 0;
        padding: 0;
        text-align: left;
        color: #FFB6C1;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out forwards;
    }}

    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-100px); }}
        to   {{ opacity: 1; transform: translateX(0); }}
    }}
    </style>

    <div class="subheading">{text_input}</div>
    """, unsafe_allow_html=True)