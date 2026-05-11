import streamlit as st

def draw_glowing_line():
    st.markdown(
        """
        <style>

        .glow-divider {
            height: 2px;
            width: 100%;
            margin-top: 10px;
            margin-bottom: 25px;

            background: linear-gradient(
                90deg,
                transparent,
                #00ffff,
                #8a2be2,
                #00ffff,
                transparent
            );

            background-size: 200% auto;

            border-radius: 999px;

            box-shadow:
                0 0 10px #00ffff,
                0 0 20px #8a2be2,
                0 0 40px rgba(138,43,226,0.8);

            animation: dividerFlow 4s linear infinite;
        }

        @keyframes dividerFlow {
            0% {
                background-position: 0% center;
            }

            100% {
                background-position: 200% center;
            }
        }

        </style>

        <div class="glow-divider"></div>
        """,
        unsafe_allow_html=True
    )
