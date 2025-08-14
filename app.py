# app.py
import streamlit as st
import os
from openai import OpenAI

# Hent API-nøgle fra miljøvariabel
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Social Media Post Generator", page_icon="📝")

st.title("📝 Social Media Post Generator")
st.write("Lav hurtigt et opslag til sociale medier – selv uden IT-erfaring.")

# Inputfelter
emne = st.text_input("Hvad skal opslaget handle om?")
tone = st.selectbox("Vælg tone", ["Professionel", "Humoristisk", "Inspirerende", "Personlig"])

if st.button("Generer opslag"):
    if emne.strip() == "":
        st.warning("Skriv venligst et emne først.")
    else:
        with st.spinner("Genererer opslag..."):
            prompt = f"Du er en dygtig social media manager. Skriv et {tone.lower()} opslag på maks 100 ord om: {emne}"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )

            opslag = response.choices[0].message.content

            st.success("Dit opslag er klar:")
            st.write(opslag)
            st.code(opslag, language="text")
