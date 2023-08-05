import streamlit as st
import pandas as pd

def main():
  # Create a title for the dashboard
  st.title("Dashboard")

  # Create a sidebar with a dropdown menu
  with st.sidebar:
    options = ["Profile", "Statistics", "About"]
    option = st.selectbox("Select an option", options)

  # Display the profile information if the user selects "Profile"
  if option == "Profile":
    profile = pd.DataFrame({
      "Name": ["Hennifer Doe"],
      "Email": ["hennifer.doe@email.com"],
      "Location": ["San Francisco, CA"],
    })
    st.dataframe(profile)

  # Display the statistics if the user selects "Statistics"
  elif option == "Statistics":
    statistics = pd.DataFrame({
      "Number of Visitors": 1000,
      "Average Time Spent on Page": 2,
      "Bounce Rate": 10%,
    })
    st.dataframe(statistics)

  # Display the about information if the user selects "About"
  else:
    about = """
    This is a simple dashboard created with Streamlit.
    You can select an option from the sidebar to display different information.
    """
    st.write(about)

if __name__ == "__main__":
  main()
