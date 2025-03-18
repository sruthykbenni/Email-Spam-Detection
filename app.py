import streamlit as st
import pickle
import re
import string

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Function to preprocess input text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text

st.title("📩 Spam Detection App")

user_input = st.text_area("Enter a message:")
if st.button("Predict"):
    cleaned_input = preprocess_text(user_input)
    vectorized_input = vectorizer.transform([cleaned_input])
    prediction = model.predict(vectorized_input)[0]
    st.write("🚨 **Spam**" if prediction == 1 else "✅ **Not Spam**")
