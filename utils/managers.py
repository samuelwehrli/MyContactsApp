from functions.github_contents import GithubContents
import streamlit as st
import streamlit_authenticator as stauth  
import pandas as pd

# ============ Manager for multi-user login ============

class LoginManager:

    CREDENTIALS_FILE = 'login_data.csv'

    def __init__(self, credentials_file_location='github', cookie_name='login-cookie', cookie_key=''):
        self.github = DataManager().github

        if 'credentials_df' in st.session_state:
            credentials_df = st.session_state.credentials_df
        else:
            if credentials_file_location == 'github':
                if self.github.file_exists(self.CREDENTIALS_FILE):
                    credentials_df = self.github.read_df(self.CREDENTIALS_FILE, index_col=0)
                else:
                    credentials_df = pd.DataFrame()
            elif credentials_file_location == 'local':
                credentials_df = pd.read_csv(self.CREDENTIALS_FILE, index_col=0)
            else:
                st.error('Invalid credentials_file_location')
            st.session_state.credentials_df = credentials_df

        credentials =  {'usernames':credentials_df.to_dict(orient="index")}
        self.authenticator = stauth.Authenticate(credentials,cookie_name=cookie_name,cookie_key=cookie_key)
        

    def login_page(self):

        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()  # create logout button
            return

        login_tab, register_tab = st.tabs(['Login', 'Register new User'])

        with login_tab:
            self.authenticator.login()
  
            if st.session_state["authentication_status"] is False:
                st.error('Username/password is incorrect')
            else: 
                st.warning('Please enter your username and password')

        with register_tab:
            res = self.authenticator.register_user(pre_authorization=False)
            if res[1] is not None:
                st.success(f'User {res[1]} registered successfully')
                credentials = self.authenticator.authentication_handler.credentials
                new_cred_df = pd.DataFrame.from_dict(credentials['usernames'], orient='index')
                st.session_state.credentials_df = new_cred_df
                self.github.write_df(self.CREDENTIALS_FILE, new_cred_df,
                                     f'Add {res[1]} to {self.CREDENTIALS_FILE}', index=True)
        st.stop()

    def go_home(self, login_page_py_file):
        """
        Create a logout button that logs the user out and redirects to the login page.
        If the user is not logged in, the login page is displayed.

        Parameters
        - login_page_py_file (str): The path to the Python file that contains the login page
        """
        if st.session_state.get("authentication_status") is not True:
            st.switch_page(login_page_py_file)
        else:
            self.authenticator.logout()
            return  # create logout button

# ============ Manager for data storage ============
        
class DataManager:

    GITHUB_SECRETS_SECTION = "github"
    DATA_FOLDER_PREFIX = "user_data_"

    def __init__(self):
        if self.GITHUB_SECRETS_SECTION not in st.secrets: 
            st.error(f"Please provide the Github secrets in the Streamlit secrets in the section {self.GITHUB_SECRETS_SECTION}")
            st.stop()
        else:
             self.github = GithubContents(
                st.secrets["github"]["owner"],
                st.secrets["github"]["repo"],
                st.secrets["github"]["token"])
        
    def get_full_path(self, path):
        user = st.session_state.get("username",'')
        return self.DATA_FOLDER_PREFIX + user + '/' + path
    
    def read_text(self, path):
        full_path = self.get_full_path(path)
        return self.github.read_text(full_path)
    
    def write_text(self, path, text, commit_message='Update'):
        full_path = self.get_full_path(path)
        return self.github.write_text(full_path, text, commit_message)
    
    def read_json(self, path):
        full_path = self.get_full_path(path)
        return self.github.read_json(full_path)
    
    def write_json(self, path, data, commit_message='Update'):
        full_path = self.get_full_path(path)
        return self.github.write_json(full_path, data, commit_message)
    
    def read_df(self, path):
        full_path = self.get_full_path(path)
        return self.github.read_df(full_path)
    
    def write_df(self, path, df, commit_message='Update', index=False, **df_to_csv_kwargs):
        full_path = self.get_full_path(path)
        return self.github.write_df(full_path, df, commit_message, index=index, **df_to_csv_kwargs)
    
    def file_exists(self, path, **pd_read_csv_kwargs):
        full_path = self.get_full_path(path)
        return self.github.file_exists(full_path, **pd_read_csv_kwargs)
