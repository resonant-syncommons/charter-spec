import streamlit as st
import json

def load_faqs(path="data/faqs_en.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def find_answer(question, faqs):
    q_lower = question.lower()
    for faq in faqs:
        if any(kw in q_lower for kw in faq["keywords"]):
            return faq["answer"]
    return "Sorry, I couldn't find an answer to your question. Please ask something else or check official tourism sites."

st.title("Japan Tourism Info Bot (Alpha)")

faqs = load_faqs()

user_input = st.text_input("Ask any question about traveling in Japan (in English):")

if user_input:
    answer = find_answer(user_input, faqs)
    st.markdown(f"**A:** {answer}")

st.caption("Powered by Streamlit. Data: Japan Tourism FAQ (English)")
