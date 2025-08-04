import streamlit as st
from app.ui import main_ui, editable_output, feedback_form, show_feedback
from app.reply_generator import generate_reply
from app.feedback_manager import save_feedback

def main():
    email, tone, intent, generate = main_ui()
    reply = ""
    error = None
    if generate and email and intent:
        reply, error = generate_reply(email, tone, intent)
        if error:
            st.error(error)
    if reply:
        edited_reply = editable_output(reply)
        thumbs, category, suggestion, submitted = feedback_form()
        if submitted:
            save_feedback(email, edited_reply, thumbs, category, suggestion)
            st.success("Feedback submitted!")

if __name__ == "__main__":
    main()
