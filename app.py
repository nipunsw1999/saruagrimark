import streamlit as st
from PIL import Image
import base64

# Inject CSS for custom title and button
st.markdown(
    """
    <style>
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

    .title {
        color: #ffe14d;
        font-size: 40px;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .custom-button {
        background-color: #ff8700;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        margin: 10px 0;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        transition-duration: 0.3s;
    }

    .custom-button:hover {
        background-color: #fff;
        color: #e66e00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    st.markdown('<div class="sidebar-title">Saru Agrimart</div>', unsafe_allow_html=True)
    st.image('images/main/back.jpg')
    st.markdown('<div class="sidebar-title-below">සරු ඇග්රිමාර්ට් වෙත සාදරයෙන් පිළිගනිමු</div>', unsafe_allow_html=True)

# Main Title
st.markdown('<div class="title">Welcome to Saru Agrimart</div>', unsafe_allow_html=True)
st.divider()

# Load and autoplay video
video_file = open("video/intro.mp4", "rb")
video_bytes = video_file.read()
encoded = base64.b64encode(video_bytes).decode()

video_html = f"""
    <video width="100%" autoplay muted loop>
        <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
"""

st.markdown(video_html, unsafe_allow_html=True)

# WhatsApp Chat Button (centered)
whatsapp_link = "https://chat.whatsapp.com/IB2swrp1xhYBLonRb4VL8C"  # Change this to your number/message
st.markdown(f"""
    <div style="text-align: center; margin-top: 30px;">
        <a href="{whatsapp_link}" target="_blank">
            <button class="custom-button">Join with us Today</button>
        </a>
    </div>
""", unsafe_allow_html=True)
