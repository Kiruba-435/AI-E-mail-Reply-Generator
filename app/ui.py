import streamlit as st

def main_ui():
    st.markdown(
        """
        <style>
        .main-title {color: #2e7dff; font-size: 2.5em; font-weight: bold;}
        .subtitle {color: #555; font-size: 1.2em; margin-bottom: 20px;}
        .stTextArea textarea {background-color: #f0f6ff;}
        .stButton button {background-color: #2e7dff; color: white; font-weight: bold;}
        .stSelectbox div {background-color: #e3f2fd;}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="main-title">📧 AI-Powered Email Reply Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paste a received email, select the tone, describe your reply, and generate a context-aware response.</div>', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/561/561127.png", width=80)
    st.markdown("---")
    email_text = st.text_area("✉️ Received Email", height=200)
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("🎨 Select Tone", ["Formal", "Friendly", "Assertive"])
    with col2:
        intent = st.text_input("📝 Describe the intended message of your reply")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Generate Reply"):
        return email_text, tone, intent, True
    return email_text, tone, intent, False

def editable_output(reply):
    st.markdown("<h4 style='color:#2e7dff;'>🧠 AI Generated Reply (Editable)</h4>", unsafe_allow_html=True)
    edited = st.text_area("", value=reply, height=200)
    st.markdown("<br>", unsafe_allow_html=True)
    copy_code = f"""
    <button onclick=\"navigator.clipboard.writeText('{edited.replace("'", "\\'").replace('\\n', '\\n')}')\" style='background:#2e7dff;color:white;font-weight:bold;border:none;padding:8px 16px;border-radius:5px;cursor:pointer;'>📋 Copy Reply</button>
    """
    st.markdown(copy_code, unsafe_allow_html=True)
    return edited

def feedback_form():
    st.markdown("<h4 style='color:#2e7dff;'>💬 Feedback</h4>", unsafe_allow_html=True)
    thumbs = st.radio("Was this reply helpful?", ["👍 Yes", "👎 No"], horizontal=True)
    category = st.selectbox("Feedback Category", ["Accuracy", "Tone", "Relevance", "Other"])
    suggestion = st.text_area("Suggestions for improvement")
    if st.button("✅ Submit Feedback"):
        return thumbs, category, suggestion, True
    return thumbs, category, suggestion, False

def show_feedback():
    import pandas as pd
    import os
    feedback_path = os.path.join(os.path.dirname(__file__), "feedback.csv")
    if os.path.exists(feedback_path):
        df = pd.read_csv(feedback_path)
        st.subheader("User Feedback")
        st.dataframe(df)
    else:
        st.info("No feedback submitted yet.")
