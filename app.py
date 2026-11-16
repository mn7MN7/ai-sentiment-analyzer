import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🤖", layout="centered")

st.title("🤖 AI Sentiment Analysis Tool")
st.write("تطبيق ذكاء اصطناعي بسيط لتحليل النصوص ومعرفة ما إذا كانت إيجابية أو سلبية.")

user_input = st.text_area("أدخل النص هنا (باللغة الإنجليزية للحصول على أفضل دقة):", 
                          placeholder="Type something like: I love learning Artificial Engineering, it's amazing!")

if st.button("تحليل النص 🚀", type="primary"):
    if user_input.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص أولاً!")
    else:
        # تحليل المشاعر باستخدام TextBlob
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            st.success(f"نتيجة التحليل: **إيجابي (Positive)** 😊 (درجة الثقة: {round(abs(sentiment_score)*100, 1)}%)")
        elif sentiment_score < 0:
            st.error(f"نتيجة التحليل: **سلبي (Negative)** 😞 (درجة الثقة: {round(abs(sentiment_score)*100, 1)}%)")
        else:
            st.info("نتيجة التحليل: **محايد (Neutral)** 😐")

st.markdown("---")
st.markdown("✨ Developed with Python & Streamlit for University Portfolio.")