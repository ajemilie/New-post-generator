# app.py
import streamlit as st
import os
from openai import OpenAI

# Hent API-nøgle fra Streamlit Secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Social Media Post Generator", page_icon="📝")

st.title("📝 Social Media Post Generator")
st.write("Lav hurtigt et opslag til sociale medier – selv uden IT-erfaring.")

# Inputfelter
emne = st.text_input("Hvad skal opslaget handle om?")
tone = st.selectbox("Vælg tone", ["Professionel", "Humoristisk", "Inspirerende", "Personlig"])

if st.button("Generer opslag"):
    # Tjek for tomt input
    if not emne.strip():
        st.warning("Skriv venligst et emne først.")
        st.stop()
    else:
        with st.spinner("Genererer opslag..."):
            # Prompt til AI
            prompt = f"Du er en dygtig social media manager. Skriv et {tone.lower()} opslag på maks 100 ord om: {emne}"

            try:
                # Opdateret modelnavn til nyeste stabile version
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200,
                    temperature=0.7
                )

                # Hent tekst og sikre korrekt encoding
                opslag = response.choices[0].message.content
                opslag = opslag.encode("utf-8").decode()

                st.success("Dit opslag er klar:")
                st.write(opslag)
                st.code(opslag, language="text")

            except Exception as e:
                st.error(f"Der opstod en fejl: {str(e)}")
