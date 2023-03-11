import streamlit as st
from streamlit_utils import card
from backend_interactions.user import get_user, get_token
def render_profile():
    cols = st.columns(2)
    with cols[0]:
        token = get_token(username=st.session_state.username, password=st.session_state.password)
        st.session_state.token = token
        user = get_user(token=st.session_state.token)
        card(title=user["full_name"], img_url="https://cdn.britannica.com/50/182850-050-8B0F87B3/Robert-Downey-Jr-Iron-Man-film-Tony.jpg")
        
    

        