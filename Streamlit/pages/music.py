import streamlit as st

st.title(":blue[My Music Playlist🎧]")

video_links = {
    "Lily": "https://www.youtube.com/watch?v=ox4tmEV6-QU&list=PLTHYDuaMjEUS_TnJ6IIUVQ_S0h0keZeZH&index=15",
    "The Secret Garden": "https://www.youtube.com/watch?v=Jc1EOTFT1zU&list=PLTHYDuaMjEUS_TnJ6IIUVQ_S0h0keZeZH&index=16",
    "Runaway": "https://www.youtube.com/watch?v=d_HlPboLRL8&list=PLTHYDuaMjEUS_TnJ6IIUVQ_S0h0keZeZH&index=17",
    "Animal": "https://youtu.be/3DIT8Y3LC6M?si=LP2Do5YfREnkUdgX",
    "Queendom": "https://youtu.be/ulSuxYUzmRQ?si=kCf1LpbfNzRpqKxb",
    "Running with the Wolves": "https://youtu.be/06ht9MyJLT4?si=hgFYH7zMuZ_taoEZ",
    "Warrior": "https://youtu.be/4CmcnWQ-754?si=-BPLLErZMoIqh1ZV"
}

option = st.selectbox(
    "Want to know what kind of music I like?",
    list(video_links.keys()),
    index=None,
    placeholder="Select music to play...",
)

# Display the video based on the selected option
if option in video_links:
    st.video(video_links[option])