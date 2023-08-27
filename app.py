import streamlit as st

# Add a custom CSS style for the background video and centered button
st.markdown(
    """
    <html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  body {
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  video {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -1;
  }
</style>
<title>Fullscreen Video Example</title>
</head>
<body>
<video autoplay loop muted playsinline>
  <source src="universe.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</body>
</html>
    """,
    unsafe_allow_html=True
)
