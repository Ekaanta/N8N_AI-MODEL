import streamlit as st
import requests

st.title("Article AI Processor")

email = st.text_input("Email")
url = st.text_input("Article URL")

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/submit",
        json={
            "email": email,
            "article_url": url
        }
    )

    if response.status_code == 200:
        st.success("Submitted Successfully")
        st.json(response.json())
    else:
        st.error(response.text)