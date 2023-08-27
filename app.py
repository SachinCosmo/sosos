import streamlit as st

# Add a custom CSS style for the background video and centered button
st.markdown(
    """
    <style>
    .fullscreen-bg {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        overflow: hidden;
        z-index: -1;
    }
    .fullscreen-bg video,
    .fullscreen-bg img {
        width: 100%;
        height: auto;
    }
    .centered-button {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the background video or GIF
st.markdown(
    """
    <div class="fullscreen-bg">
        <video loop muted autoplay playsinline>
            <source src="universe.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <button class="centered-button">Explore Infinite</button>
    </div>
    """,
    unsafe_allow_html=True
)