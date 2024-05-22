import streamlit as st
from functions.managers import LoginManager

LoginManager().go_home('testapp.py')

st.title("Page 1")
st.write("Welcome to Page 1!")
