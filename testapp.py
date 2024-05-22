import streamlit as st
from functions.managers import LoginManager

LoginManager().login_page()

st.title("Home Page of the App")




#st.write(st.session_state["authentication_status"])

#st.write(dm.get_credentials_df())