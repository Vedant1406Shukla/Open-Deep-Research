import streamlit as st
import requests
import json

st.title("Perplexity AI Research Agent")

API_KEY = "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"

user_input = st.text_area("Ask something:")

if st.button("Submit"):
    if not API_KEY:
        st.error("Please enter your API key.")
    elif not user_input:
        st.error("Please enter a question.")
    else:
        url = "https://api.perplexity.ai/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "sonar-pro",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        with st.spinner("Fetching response from Perplexity..."):
            response = requests.post(url, headers=headers, json=data)
            res_json = response.json()

        # Extract main content
        try:
            answer = res_json["choices"][0]["message"]["content"]
        except:
            answer = "Could not extract answer. Check API key or model name."

        st.subheader("Answer:")
        st.write(answer)


import streamlit as st
import requests
import json

st.title("Perplexity AI Research Agent")

API_KEY = "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"

user_input = st.text_area("Ask something:")

if st.button("Submit"):
    if not API_KEY:
        st.error("Please enter your API key.")
    elif not user_input:
        st.error("Please enter a question.")
    else:
        url = "https://api.perplexity.ai/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "sonar-pro",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        with st.spinner("Fetching response from Perplexity..."):
            response = requests.post(url, headers=headers, json=data)
            res_json = response.json()

        # Extract main content
        try:
            answer = res_json["choices"][0]["message"]["content"]
        except:
            answer = "Could not extract answer. Check API key or model name."

        st.subheader("Answer:")
        st.write(answer)

