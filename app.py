import os
import streamlit as st
from openai import OpenAI

# (Valgfrit, men hjælper i nogle miljøer)
os.environ.setdefault("PYTHONIOENCODING", "utf-8")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Social Media Post Generator", page_icon="📝")
st.title("📝 Social Media Post Generator")
st.write("Lav hurtigt et opslag til sociale medier – selv uden IT-erfaring.")

emne = st.text_input("Hvad skal opslaget handle om?")
tone = st.selectbox("Vælg tone", ["Professionel", "Humoristisk", "Inspirerende", "Personlig"])

if st.button("Generer opslag"):
    if not emne.strip():
        st.warning("Skriv venligst et emne først.")
        st.stop()

    with st.spinner("Genererer opslag..."):
        prompt = (
            f"Du er en dygtig social media manager. "
            f"Skriv et {tone.lower()} opslag på maks 100 ord om: {emne}"
        )

        try:
            resp = client.chat.completions.create(
                # skift til en model I har adgang til, hvis denne fejler
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7,
            )

            opslag = resp.choices[0].message.content or ""
            # Vis teksten direkte i UTF-8 (ingen ASCII-rens)
            st.success("Dit opslag er klar:")
            st.text_area("Output", value=opslag, height=200)

        except Exception as e:
            # Vis fuld fejl sikkert
            st.error(f"Der opstod en fejl: {e}")
