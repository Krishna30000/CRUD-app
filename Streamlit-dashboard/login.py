import streamlit as st
from profile import render_profile
from signup import render_signup
from streamlit_utils import *



def render_login():
    st.header("Please login to proceed")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    row_spaces(2)

    cols = st.columns(6)
    with cols[2]:
        if st.button("Login", use_container_width=True):
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.page = render_profile
    with cols[3]:
        if st.button("Signup", use_container_width=True):
            st.session_state.page = render_signup

def navigate_login():
    st.session_state.page = render_login
# st.session_state.page()
