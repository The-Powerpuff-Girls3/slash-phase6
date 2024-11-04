"""
Copyright (c) 2023 Mery Harika Gaddam
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

import requests
import streamlit as st


def render_logout():
    API_URL = "http://127.0.0.1:5050/auth"
    response = requests.get(f"{API_URL}/logout", cookies={"access_token": st.session_state.cookie})
    del st.session_state['token']
    del st.session_state['cookie']
    st.success("Logged out successfully.")
    st.rerun()
