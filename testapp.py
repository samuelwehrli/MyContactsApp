import streamlit as st

# from functions.data_manager import data_manager 
from functions.data_manager import LoginManager

show_pages(['testapp'])

lm = LoginManager()



lm.login_page()






#st.write(st.session_state["authentication_status"])

#st.write(dm.get_credentials_df())