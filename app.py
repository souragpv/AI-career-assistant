import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.pdf_parser import extract_text_from_pdf
from utils.prompts import *

st.set_page_config(page_title="AI Career Assistant", page_icon="🚀")
st.title("🚀 AI Career Assistant Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

with st.sidebar:
    st.header("⚙️ Options")
    feature = st.selectbox("Choose Feature", [
        "💬 General Chat",
        "📄 Resume Review",
        "🎯 Interview Prep",
        "🗺️ Career Roadmap",
        "🔍 JD Analysis"
    ])
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    if uploaded_file:
        st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Resume uploaded!")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything about your career...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if feature == "📄 Resume Review" and st.session_state.resume_text:
        prompt = resume_review_prompt(st.session_state.resume_text)
    elif feature == "🎯 Interview Prep":
        prompt = interview_prep_prompt(user_input)
    elif feature == "🗺️ Career Roadmap":
        prompt = roadmap_prompt(user_input)
    elif feature == "🔍 JD Analysis" and st.session_state.resume_text:
        prompt = job_description_prompt(user_input, st.session_state.resume_text)
    else:
        prompt = user_input

    response = get_gemini_response(prompt)

    if user_input:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt)
                if "quota exceeded" in response.lower() or "⚠️" in response:
                    st.warning("⚠️ API quota exceeded. Please wait a minute and try again.")
                else:
                    st.markdown(response)