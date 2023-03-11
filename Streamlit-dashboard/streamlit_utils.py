import streamlit as st
from streamlit_elements import elements, mui, html, sync

def card(title, img_url):
    with elements("style_mui_sx"):
                
        with mui.Card(key="ocp", sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            
            mui.CardHeader(
                title=title,
                avatar=mui.Avatar(title[0], sx={"bgcolor": "cyan"}),
                action=mui.IconButton(mui.icon.MoreVert),
            )

            mui.CardMedia(
                component="img",
                image=img_url,
                alt="Paella dish",
                height=150
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Button("Edit Profile", variant="contained", sx={"borderRadius":5, "textTransform": "none", "margin":0.5})