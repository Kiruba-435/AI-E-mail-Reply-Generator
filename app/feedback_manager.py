import csv
import os

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedback.csv")

def save_feedback(email, reply, thumbs, category, suggestion):
    header = ["email", "reply", "thumbs", "category", "suggestion"]
    file_exists = os.path.isfile(FEEDBACK_FILE)
    with open(FEEDBACK_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([email, reply, thumbs, category, suggestion])
