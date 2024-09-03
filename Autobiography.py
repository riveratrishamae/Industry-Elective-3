import streamlit as st
import pandas as pd


about_page = st.Page(
    page="Streamlit/pages/about_me.py",
    title="About Me",
    icon="🤍",
    default=True,
)


page_1 = st.Page(
    page="Streamlit/pages/games.py",
    title="Games",
    icon="🎮",
)

page_2 = st.Page(
    page="Streamlit/pages/music.py",
    title="Music",
    icon="🎧",
)

pg = st.navigation(
 {
     "Info": [about_page],
     "Hobbies": [page_1, page_2],
 }   
)

st.logo("Streamlit/assets/logo.png")
st.sidebar.text("made by Trish")

pg.run()