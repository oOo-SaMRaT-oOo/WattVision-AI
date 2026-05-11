import streamlit as st

def styled_header(text, font_size="clamp(40px, 8vw, 90px)"):
    """
    Renders a futuristic, animated RGB signature title.
    :param text: The string to display
    :param font_size: CSS font-size (supports px, rem, or clamp)
    """
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

        <style>
        /* Container cleanup */
        [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }}

        .big-title {{
            font-family: 'Great Vibes', cursive !important;
            font-size: {font_size} !important; 
            line-height: 1.2;
            margin: 0;
            padding: 10px 0;
            text-align: center;
            white-space: nowrap; 
            
            /* Animated RGB Gradient Text */
            background: linear-gradient(to right, #ff0000, #00ff00, #00ffff, #ff00ff, #ff0000);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            /* Glow and Movement Animations */
            animation: 
                slideIn 1.5s ease-out,
                rainbow 4s linear infinite,
                glow-pulse 2s infinite alternate;
        }}

        @keyframes slideIn {{
            from {{opacity:0; transform:translateX(-50px);}}
            to   {{opacity:1; transform:translateX(0);}}
        }}

        @keyframes rainbow {{
            to {{ background-position: 200% center; }}
        }}

        @keyframes glow-pulse {{
            from {{ filter: drop-shadow(0 0 10px rgba(0, 198, 255, 0.4)); }}
            to {{ filter: drop-shadow(0 0 30px rgba(0, 114, 255, 0.8)); }}
        }}
        </style>

        <div class="big-title">{text}</div>
        """,
        unsafe_allow_html=True
    )

# --- HOW TO USE IT ---
# styled_header("Watt Vision : AI")
# styled_header("Dashboard", font_size="50px")