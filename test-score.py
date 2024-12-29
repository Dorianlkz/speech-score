import streamlit as st

st.title('Candidate Text-Based Scoring System')

# Accept video file input
uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

# Display the uploaded video
if uploaded_video is not None:
    st.video(uploaded_video)
    st.success("Video uploaded successfully!")
else:
    st.warning("Please upload a video file.")