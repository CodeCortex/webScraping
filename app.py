import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Web Content Extraction - URL Parsing")

url = st.text_input("Enter the link here", "https://www.ysppayments.com/")

if(st.button("Get Content")):
    try:
        response= requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup= BeautifulSoup(response.content, "html.parser")
        text= soup.get_text(separator="\n\n", strip=True)
        
        st.subheader("Extracted content: ")
        st.text_area("Page Text", text, height=500)
        
    except requests.exceptions.RequestException as e:
        st.error(f"Request Failed: {e}")


    


