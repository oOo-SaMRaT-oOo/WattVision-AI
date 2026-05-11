import streamlit as st

def load_background():
    st.markdown(
        """
        <style>
        /* Hide default Streamlit clutter */
        header {visibility: hidden;}
        [data-testid="stHeader"] {background: rgba(0,0,0,0);}
        [data-testid="stDecoration"] {display: none;}
        
        /* Dark Base */
        .stApp {
            background-color: #000000;
        }

        /* Blobs Layer - Fixed at the very back */
        .blob-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1; /* Behind everything */
            filter: blur(80px);
            opacity: 0.5;
            pointer-events: none; /* Allows clicking through blobs */
        }

        .blob {
            position: absolute;
            border-radius: 50%;
            mix-blend-mode: screen;
            animation: move-complex 30s infinite alternate ease-in-out;
        }

        .blob.one {
            width: 500px; height: 500px;
            background: radial-gradient(circle, #5e00ff 0%, #2a0066 100%);
            top: -10%; left: 10%;
            animation-duration: 22s;
        }

        .blob.two {
            width: 600px; height: 600px;
            background: radial-gradient(circle, #0047ff 0%, #000d3d 100%);
            bottom: -15%; right: 5%;
            animation-duration: 35s;
        }

        .blob.three {
            width: 450px; height: 450px;
            background: radial-gradient(circle, #00f2ff 0%, #00334d 100%);
            top: 40%; left: 35%;
            animation-duration: 28s;
        }

        @keyframes move-complex {
            0% { transform: translate(0, 0) scale(1) rotate(0deg); }
            33% { transform: translate(15vw, 10vh) scale(1.1) rotate(120deg); }
            66% { transform: translate(-10vw, 25vh) scale(0.9) rotate(240deg); }
            100% { transform: translate(5vw, -10vh) scale(1.05) rotate(360deg); }
        }

        /* Global text fix to ensure it sits above blobs */
        .stMarkdown, .stText, h1, h2, h3, p {
            position: relative;
            z-index: 10; 
        }
        </style>

        <div class="blob-container">
            <div class="blob one"></div>
            <div class="blob two"></div>
            <div class="blob three"></div>
        </div>
        """,
        unsafe_allow_html=True
    )