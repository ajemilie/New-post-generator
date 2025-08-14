import streamlit as st
import os
from openai import OpenAI

# Hent API-nøgle fra Secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Instagram Post Generator", page_icon="📸")

st.title("📸 Instagram Post Generator")
st.write("Skriv et emne og vælg en tone, så får du et færdigt opslag klar til Instagram.")

# Input fra brugeren
emne = st.text_input("Hvad skal opslaget handle om?")
tone = st.selectbox("Vælg tone", ["Professionel", "Humoristisk", "Inspirerende", "Personlig"])

if st.button("Generer opslag"):
    if not emne.strip():
        st.warning("Skriv venligst et emne først.")
    else:
        with st.spinner("Genererer opslag..."):
            prompt = f"Du er en social media ekspert. Skriv et kort, fængende Instagram-opslag i en {tone.lower()} tone om: {emne}. Brug emojis og hashtags."

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.8
                )

                opslag = response.choices[0].message.content
                st.success("Her er dit opslag:")
                st.write(opslag)

            except Exception as e:
                st.error(f"Fejl: {str(e)}")
