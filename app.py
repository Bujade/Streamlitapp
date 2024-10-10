import streamlit as st

# Title of the Dashboard
st.title("Hello World Streamlit Dashboard")

# Adding a simple text
st.write("Welcome to your first Streamlit dashboard!")

# Adding a button
if st.button('Say hello'):
  
    st.write('Hello, World!')
else:
    st.write('Goodbye, World!')
