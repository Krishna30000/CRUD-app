import streamlit as st
from login import render_login

if 'page' not in st.session_state:
    st.session_state.page = render_login

st.session_state.page()


