import streamlit as st

st.title(":blue[Games I Play🎮]")

col1, col2, col3 = st.columns(3, gap="small",vertical_alignment="center")

with col1:
    st.image("Streamlit/assets/skylogo.png", caption="Sky: Children of the Light")
    st.image("Streamlit/assets/cookielogo.png", caption="CookieRun: Kingdom")

with col2:
    st.image("Streamlit/assets/valologo.png", caption="Valorant")
    st.image("Streamlit/assets/teklogo.jpg", caption="Tekken")

with col3:
    st.image("Streamlit/assets/mllogo.jpg", caption="Mobile Legends Bang Bang")
    st.image("Streamlit/assets/saulogo.jpg", caption="Sausage Man")

