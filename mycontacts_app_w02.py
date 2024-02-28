import streamlit as st
import pandas as pd
from datetime import datetime, date

# Set page configuration
st.set_page_config(page_title="My Contacts", page_icon="🎂", layout="wide")

def init_dataframe():
    """Initialize or load the dataframe."""
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['Name', 'Birth Date', 'Age'])

def calculate_age(birth_date):
    """Calculate age given the birth date."""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def add_entry(name, birth_date):
    """Add a new entry to the DataFrame using pd.concat and calculate age."""
    age = calculate_age(birth_date)
    new_entry = pd.DataFrame([{'Name': name, 'Birth Date': birth_date, 'Age': age}])
    st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)

def display_dataframe():
    """Display the DataFrame in the app."""
    if not st.session_state.df.empty:
        st.dataframe(st.session_state.df)
    else:
        st.write("No data to display.")

def plot_data():
    """Plot the age data using Pandas' plotting capabilities."""
    if not st.session_state.df.empty:
        df = st.session_state.df
        ax = df.plot(kind='barh', x='Name', y='Age', title = "Age", legend=False)
        st.pyplot(ax.figure)
    else:
        st.write("No data to display.")

def main():
    st.title("My Contacts App")

    init_dataframe()

    with st.sidebar:
        st.header("Add New Entry")
        name = st.text_input("Name")
        birth_date = st.date_input("Birth Date",min_value=date(1950, 1, 1),format="DD.MM.YYYY")
        add_button = st.button("Add")

    if add_button and name:  # Check if name is not empty
        add_entry(name, birth_date)

    display_dataframe()
    plot_data()

if __name__ == "__main__":
    main()
