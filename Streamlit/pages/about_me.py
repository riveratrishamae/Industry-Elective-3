import streamlit as st
import pandas as pd

col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpg", width=230)
with col2:
    st.title(":blue[Trisha Mae Rivera]", anchor=False, )
    st.write("**An :red[Information Technology] student at Cebu Institute of Technology University (CIT-U)**")

st.write("\n")

tab1, tab2, tab3, tab4 = st.tabs(["🦆Self Introduction","📎Academic Experiences", "👩‍💻Skills", "📱Socials"])

with tab1:
    st.subheader(":violet[Self Introduction]")
    st.write(
    """
    **Hello! My name is Trisha Mae Rivera, 22 years old born on July 31,2002. I am currently studying in
    CIT-U for my Bachelors Degree in Information Technology. I have always found technology very intriguing
    and intimidating. Studying it so far has made me understand that it is fast evolving and in no time we'll
    slowly enter a world that is technology dependent. That is why I choose this course, to deepen my perception
    about the world we're making.**
    """
         )
    
with tab2:
    st.subheader(":violet[Academic Experiences]")
    expander = st.expander("See Academic Experiences")
    expander.write('''
    - Learned backend through Information Management using SQL
    - Learned frontend through ReactJS
    - Assisted on  frontend  
    - Managed documents for Capstone Project 1 & 2
    - Networking 
''')
    # expander.image("https://static.streamlit.io/examples/dice.jpg")
    
with tab3:
    st.subheader(":violet[Skills]")
    data_df = pd.DataFrame(
    {
        "Language": ["Java", "C", "React", "Python", "SQL"],
        "Mastery": [40, 20, 10, 30, 50],
    }
)

    st.data_editor(
    data_df,
    column_config={
        "Mastery": st.column_config.ProgressColumn(
            "Mastery",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)

with tab4:
    st.subheader(":violet[Socials]")

    col1, col2, col3 = st.columns(3, gap="small",vertical_alignment="center")
    with col1:
        st.link_button( "Github", "https://github.com/riveratrishamae")
        st.link_button( "Facebook", "https://www.facebook.com/trishamae.rivera.526")
    with col2:
        st.link_button( "Youtube", "https://www.youtube.com/@skykid31")
        st.link_button( "Pinterest", "https://ph.pinterest.com/exinsanity/")
    with col3:
        st.link_button( "Instagram", "https://www.instagram.com/trishhmae31/")
        st.link_button( "Steam", "https://steamcommunity.com/profiles/76561199534001066/")
    
