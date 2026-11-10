import streamlit as st
from transformers import pipeline

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Text Tool",
    layout="centered"
)

st.title("🤖 Day 1: AI Text Summarizer & Sentiment Analyzer")
st.write("Paste your English text below and get AI-powered Sentiment Analysis and Text Summarization.")

# ----------------------------
# Load Models
# ----------------------------
@st.cache_resource
def load_models():

    sentiment = pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-6-6"
    )

    return sentiment, summarizer

with st.spinner("🤖 Loading AI models... Please wait."):
    sentiment_model, summarizer_model = load_models()

# ----------------------------
# User Input
# ----------------------------
user_text = st.text_area(
    "Enter your English paragraph below (Minimum 3-4 lines):",
    height=220
)

# ----------------------------
# Buttons
# ----------------------------
col1, col2 = st.columns(2)

# ----------------------------
# Sentiment Analysis
# ----------------------------
with col1:

    if st.button("🎭 Analyze Sentiment"):

        if user_text.strip() == "":
            st.warning("Please enter some text.")
        else:

            with st.spinner("Analyzing Sentiment..."):

                result = sentiment_model(user_text)[0]

                label = result["label"]
                score = result["score"] * 100

                if label == "POSITIVE":
                    st.success(f"😊 Positive Sentiment ({score:.2f}%)")
                else:
                    st.error(f"😔 Negative Sentiment ({score:.2f}%)")

# ----------------------------
# Text Summarization
# ----------------------------
with col2:

    if st.button("📝 Summarize Text"):

        if len(user_text.split()) < 30:

            st.warning("Please enter at least 30 words.")

        else:

            with st.spinner("Generating Summary..."):

                summary = summarizer_model(
                    user_text,
                    max_length=120,
                    min_length=30,
                    do_sample=False
                )

                st.info("📌 Summary")

                st.write(summary[0]["summary_text"]) 