import streamlit as st
import pandas as pd
import numpy as np
import time 
from styles.glowing_line import draw_glowing_line
from styles.normal_text import intro_text
from styles.custom_css import button_css
from styles.header_text import styled_header
from styles.normal_text import normal_text
from styles.glowing_line import draw_glowing_line


def vision_terminal_loading(models_dict) :

    styled_header("Watt Vision : AI")
    text = "&nbsp;&nbsp;&nbsp;&nbsp;~ Unmasking the invisible heartbeat of your home !"
    normal_text(text)
    draw_glowing_line()


    data = pd.read_csv("Energy_Data_Demo.csv")
    data["power_change"] = data["mains_power_W"].diff()
    st.markdown("<br><br>",unsafe_allow_html=True)
    electrical_data = pd.read_csv("Current_Voltage_Data_Demo.csv")
    data["current_A"] = electrical_data["current_A"]
    data["voltage_V"] = electrical_data["voltage_V"]
    data["pf"] = data["mains_power_W"] / (data["current_A"] * data["voltage_V"])
    data["pf"] = data["pf"].fillna(1.0).replace([np.inf, -np.inf], 1.0).clip(0, 1) # IMP

    button_css()

    if "analysis_active" not in st.session_state:
        st.session_state.analysis_active = False

    if st.button("START ANALYSIS"):
        st.session_state.analysis_active = True


    if st.session_state.analysis_active :

        st.write("---")

        st.subheader("MAINS POWER SUPPLY :")
        st.markdown("<br>",unsafe_allow_html=True)
        col1,col2= st.columns([1,3])
        mains_value = col1.empty()
        mains_graph = col2.empty()

        draw_glowing_line()
        st.subheader("VISUALIZATION : ")
        st.markdown("<br>",unsafe_allow_html=True)
        col1,col2= st.columns([1,1])
        lhs_holder = col1.empty()
        rhs_holder = col2.empty()
        draw_glowing_line()
        

        st.subheader("AI APPLIANCE DETECTION : ")
        st.markdown("<br>",unsafe_allow_html=True)
        col1,col2 = st.columns([1,2.5])
        with col1 :
            prediction_holder = st.empty()
        with col2:
            st.write("MAINS SUPPLY : ")
            mains_graph_new = st.empty()


        draw_glowing_line()


        st.subheader("ELECTRICAL SIGNATURES :")
        st.markdown("<br>",unsafe_allow_html=True)
        voltage_value = st.empty()
        col1,col2 = st.columns(2)
        current_value = col1.empty()
        pf_value = col2.empty()

        draw_glowing_line()
        
        intro_text("~ By Samrat Malla")





        for index,row in data.iterrows():

            if index < 5 : continue

            with mains_value.container():
                st.write("<br><br>",unsafe_allow_html=True)
                st.metric(label = "Mains Power ( W )",
                            value = f"{round(row['mains_power_W'],2)}")
            
            window = data.iloc[max(0, index-100) : index+1]
            
            mains_graph_data = pd.DataFrame()
            mains_graph_data["Value"] = window[["mains_power_W"]].copy()
            mains_graph_data["Max"] = 5000
            mains_graph_data["Min"] = 0
            mains_graph.line_chart(mains_graph_data)

            with lhs_holder.container():
                st.write("MAINS SUPPLY : ")
                st.write(f"VALUE : {np.round(row["mains_power_W"],2)} W")
                st.line_chart(mains_graph_data)

            with rhs_holder.container():
                st.write("POWER CHANGE : ")
                st.write(f"VALUE : {np.round(row["power_change"],2)} W")
                powerchange_graph_data = pd.DataFrame()
                powerchange_graph_data["Value"] = window[["power_change"]].copy()
                powerchange_graph_data["Max"] = 2000
                powerchange_graph_data["Min"] = -2000
                st.line_chart(powerchange_graph_data)


            if index < 5 : continue

            feature_window = data.iloc[index-4:index+1] # Doing rolling phenomena
            mains_power = row["mains_power_W"]
            p_change = row["power_change"]
            r_mean = feature_window["mains_power_W"].mean()
            r_std = feature_window["mains_power_W"].std()
            prev_p = data.iloc[index-1]["mains_power_W"]
            abs_c = abs(p_change)
            current_A = row["current_A"]
            pf = row["pf"]

            feature_df = pd.DataFrame({
                "mains_power_W":[mains_power],
                "power_change":[p_change],
                "rolling_mean":[r_mean],
                "rolling_std" : [r_std],
                "prev_power":[prev_p],
                "abs_change":[abs_c],
                "current_A":[current_A],
                "pf":[pf]

            })

            predictions = {}

            for appliance,appliance_model in models_dict.items():

                probablity_value = appliance_model.predict_proba(feature_df)[0]
                predictions[appliance] = probablity_value[1]*100

            with prediction_holder.container():
                for appliance,probablity_value in predictions.items():

                    if probablity_value >90:
                        text = f"{appliance.upper()}:  \nSTATE : ON  \nCONFIDENCE : {probablity_value:.3f}%"
                        st.success(text)

                    else:
                        text = f"{appliance.upper()}:  \nSTATE : OFF"
                        st.error(text)

            with mains_graph_new.container():
                
                st.write(f"VALUE : {np.round(row["mains_power_W"],2)} W")
                st.line_chart(mains_graph_data)


            with current_value.container():
                st.metric(label = "RMS CURRENT ( Amp )",
                        value = f"{row["current_A"]:.2f} A")
                current_graph_data = pd.DataFrame()
                current_graph_data["Value"] = window["current_A"]
                current_graph_data["Max"] = 50
                current_graph_data["Min"] = -10
                st.line_chart(current_graph_data)

            with pf_value.container():
                st.metric(label = "Power Factor",
                        value = f"{row["pf"]:.2f}")
                pf_graph_data = pd.DataFrame()
                pf_graph_data["Value"] = window["pf"]
                pf_graph_data["Max"] = 2
                pf_graph_data["Min"] = -1
                st.line_chart(pf_graph_data)

            
            time.sleep(0.0001)
                
            



