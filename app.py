import streamlit as st
import os
from openai import OpenAI

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
        prompt = f"Du er en dygtig social media manager. Skriv et {tone.lower()} opslag på maks 100 ord om: {emne}"

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )

            # Sikrer, at teksten altid er ren unicode
            opslag = str(response.choices[0].message.content)

            st.success("Dit opslag er klar:")
            st.write(opslag)

        except UnicodeEncodeError as ue:
            st.error(f"Tegnkodningsfejl: {ue}. Sørg for at appen kører i et miljø med UTF-8 understøttelse.")
        except Exception as e:
            st.error(f"Der opstod en fejl: {e}")
