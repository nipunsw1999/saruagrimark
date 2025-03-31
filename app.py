import streamlit as st
from PIL import Image

# Inject CSS for custom title
st.markdown(
    """
    <style>
    /* Style specifically for the sidebar */
    .sidebar .sidebar-content {
        padding: 1rem;
    }
    .sidebar-title {
        color: #ff8700;
        font-size: 28px;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .sidebar-title-below {
        color: #ffe14d;
        font-size: 20px;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .title{
        color: #ffe14d;
        font-size: 40px;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    st.markdown('<div class="sidebar-title">Saru Agrimart</div>', unsafe_allow_html=True)
    st.image('images/main/back.jpg')
    # st.subheader("Welcome to Saru Agrimart!")
    st.markdown('<div class="sidebar-title-below">සරු ඇග්රිමාර්ට් වෙත සාදරයෙන් පිළිගනිමු</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2,6])
with col1:
    image = Image.open("images/main/logo.jpg")
    st.image(image, width=150)
with col2:
    st.markdown('<div class="title">Welcome to Saru Agrimart</div>', unsafe_allow_html=True)
    
st.divider()

# Read the video file as base64
import base64

video_file = open("video/intro.mp4", "rb")
video_bytes = video_file.read()
encoded = base64.b64encode(video_bytes).decode()

# Autoplay using HTML
video_html = f"""
    <video width="100%" autoplay muted loop>
        <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
"""

st.markdown(video_html, unsafe_allow_html=True)