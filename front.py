import streamlit as st
import requests

st.title("Web Scraper via Flask API")

# Input field
url = st.text_input("Enter a website URL:", "https://www.hdfcbank.com/")

# Button to trigger API
if st.button("Get API Data"):
    try:
        api_url = "http://localhost:5000/api/getdata"
        params = {"url": url}
        response = requests.get(api_url, params=params)
        data = response.json()

        if "text" in data:
            st.subheader("Extracted Text")
            st.text_area("Webpage Text", data["text"], height=500)
        else:
            st.error(f" Error: {data.get('error', 'Unknown error')}")

    except Exception as e:
        st.error(f" Request failed: {e}")
