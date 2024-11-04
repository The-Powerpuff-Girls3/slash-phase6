"""
Copyright (c) 2023 Mery Harika Gaddam
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

import streamlit as st
import requests


def render_register():
    API_URL = "http://127.0.0.1:5050/auth"

    # Load external CSS for styling
    with open('assets/style.css') as f:
        st.markdown(f"""
            <style>
            {f.read()}
            </style>
        """, unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        st.header("Register")
        st.subheader("Enter your details below")
        firstname = st.text_input("First Name")
        lastname = st.text_input("Last Name")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        verify_password = st.text_input("Verify Password", type="password")
        register = st.button("Register")

    with col2:
        st.subheader("Why register?")
        st.write(
            "Registering with us will allow you to save your favourite items to your wishlist and access them anytime."
        )

    if register:
        if firstname and lastname and username and email and password and verify_password:
            if password == verify_password:
                response = requests.post(
                    f"{API_URL}/registerUser",
                    data={"username": username, "password": password, "firstname": firstname, "lastname": lastname, "email": email}
                )

                if response.status_code == 200:
                    response_data = response.json()
                    if response_data.get('message') != "User successfully created":
                        st.warning(response_data['message'])
                    else:
                        st.success("Registration Successful, Login to start creating your wishlist")
            else:
                st.error("Passwords do not match")
        else:
            st.warning("Please enter all details")


render_register()
