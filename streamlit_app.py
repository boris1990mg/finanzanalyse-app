import streamlit as st
import pandas as pd
from io import BytesIO
from services.parser import parse_bwa_file
from services.analysis import analyze_bwa

st.set_page_config(page_title="Finanzanalyse Beta", layout="centered")

st.title("BWA Finanzanalyse App – Beta")
st.markdown("Lade eine BWA-Datei hoch (Excel oder CSV) und erhalte deine Auswertung.")

uploaded_file = st.file_uploader("Datei auswählen", type=["xlsx", "xls", "csv"])
if uploaded_file:
    try:
        data = uploaded_file.read()
        df = parse_bwa_file(BytesIO(data), uploaded_file.name)
        result = analyze_bwa(df)

        st.subheader("Auswertung")
        st.write("**Rohertrag:**", result.get("Rohertrag"))
        st.write("**Personalkosten:**", result.get("Personalkosten"))
        st.write("**Raumkosten:**", result.get("Raumkosten"))
        st.write("**Gewinn:**", result.get("Gewinn"))
        st.write("**Kapitaldienstfähigkeit:**", "Erfüllt" if result.get("Kapitaldienstfähig") else "Nicht erfüllt")
    except Exception as e:
        st.error(f"Fehler beim Verarbeiten der Datei: {e}")