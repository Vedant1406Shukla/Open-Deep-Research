import streamlit as st
import google.generativeai as genai
import os

# ---------------- CONFIGURATION ----------------
# 1️⃣  Set your API key
#    (Option A) Read from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#    (Option B) Ask user in sidebar if not set
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = st.sidebar.text_input("Enter your Google API Key", type="password")

# Configure the SDK
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    st.warning("⚠️ Please provide a valid Google API key to use the app.")
    st.stop()

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="AI Research Agent", layout="wide")
st.title("🤖 AI Research Agent (Google Generative AI)")
st.markdown("Enter a prompt below and let the agent generate an intelligent response using **Gemini**.")

# ---------------- PROMPT INPUT ----------------
prompt = st.text_area("Your Prompt:", height=150, placeholder="e.g. Write a story about a magic backpack...")

# ---------------- GENERATE BUTTON ----------------
if st.button("Generate Response 🚀"):
    if not prompt.strip():
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(prompt)
                output = response.text if response and response.text else "No response received."
                st.success("✅ Response generated successfully!")
                st.markdown("### 🧠 AI Output")
                st.write(output)
            except Exception as e:
                st.error(f"Error: {e}")

# ---------------- SIDEBAR INFO ----------------
st.sidebar.markdown("### ⚙️ Configuration")
st.sidebar.markdown("- **Model:** gemini-2.5-flash\n- **Provider:** Google Generative AI\n- **UI:** Streamlit")
