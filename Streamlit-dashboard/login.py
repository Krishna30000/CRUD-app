import streamlit as st
from profile import render_profile
def render_login():
    st.header("Please login to proceed")
    username = st.text_input("Username")
    password = st.text_input("Password")

    if st.button("Login"):
        st.session_state.username = username
        st.session_state.password = password
        st.session_state.page = render_profile

