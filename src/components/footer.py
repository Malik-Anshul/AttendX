import streamlit as st

def footer_home():

    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; margin-top:2rem;">
            <p style="margin:0; color:white; font-size:18px;">
                Created by  
                <span style="color:#FFD700; font-weight:bold; font-family:Courier New, monospace; font-size:22px;">
                    'MALIK'
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; margin-top:2rem;">
            <p style="margin:0; color:black; font-size:18px;">
                Created by  
                <span style="color:#EB459E; font-weight:bold; font-family:Courier New, monospace; font-size:22px;">
                    'MALIK'
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)


