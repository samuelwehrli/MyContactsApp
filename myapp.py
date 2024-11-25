import streamlit as st
from utils.managers import LoginManager

LoginManager().login_page()

st.title("Home Page of the App")

st.sidebar.empty() 
sidebar_placeholder = st.sidebar.empty()
with sidebar_placeholder:
    st.sidebar.title("Menü")


#st.write(st.session_state["authentication_status"])

#st.write(dm.get_credentials_df())