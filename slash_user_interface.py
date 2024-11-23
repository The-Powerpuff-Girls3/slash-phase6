import streamlit as st
from requests_oauthlib import OAuth2Session
import os

st.set_page_config(page_title="Slash - Product Search", page_icon="🔍")

from src.pages.search import render_search
from src.pages.wishlist import render_wishlist
from src.pages.login import render_login
from src.pages.register import render_register
from src.pages.logout import render_logout

# Google OAuth configuration
client_id = '1033192991367-ce9pdg2m2rq4kgklglfmtrcvcjdq4caf.apps.googleusercontent.com'
client_secret = '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'
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://oauth2.googleapis.com/token'
redirect_uri = 'http://localhost:8501'

def google_login():
    google = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['openid', 'email', 'profile'])
    authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", prompt="select_account")
    st.write(f'<a href="{authorization_url}" target="_self">Login with Google</a>', unsafe_allow_html=True)

def google_callback():
    google = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['openid', 'email', 'profile'])
    token = google.fetch_token(token_url, client_secret=client_secret, authorization_response=st.experimental_get_query_params()['code'][0])
    user_info = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    st.session_state.token = token
    st.session_state.user_info = user_info
    st.experimental_rerun()

if 'code' in st.experimental_get_query_params():
    google_callback()

st.markdown("<span class='float-box'><h1 class='float'>Slash - Product Search</h1></span>", unsafe_allow_html=True)
st.session_state.token = st.session_state.get("token", None)

class UIManager:
    def __init__(self):
        self.pages = []

    def addPage(self, title, render_method):
        self.pages.append({"title": title, "function": render_method})

    def render(self):
        st.sidebar.markdown("## Main Menu")
        page = st.sidebar.selectbox("Select Page", self.pages, format_func=lambda page: page["title"])
        page["function"]()

uiManager = UIManager()

def render_register():
    st.title("Register")
    # 你的注册表单代码
    st.write("Or")
    google_login()

uiManager.addPage("Search", render_search)
if st.session_state.token:
    uiManager.addPage("Wishlist", render_wishlist)
    uiManager.addPage("logout", render_logout)
else:
    uiManager.addPage("Login", render_login)
    uiManager.addPage("Register", render_register)
    uiManager.addPage("Google Login", google_login)

uiManager.render()
