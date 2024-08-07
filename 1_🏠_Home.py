import streamlit as st

st.set_page_config(page_title="Oenologics", layout="centered", page_icon="🍷", )

st.title("Oenologics WebApp")


st.write("""Dieses Tool unterstützt dich bei der Durchführung wichtiger Berechnnungen im Weinkeller.""")

st.write("#####")

st.subheader("Übersicht", divider="grey")
st.page_link("1_🏠_Home.py", label="Home", icon="🏠")
st.page_link("pages/2_🍇_Alkoholausbeute.py", label="Alkoholausbeute", icon="🍇")
st.page_link("pages/3_🍬_Anreicherung.py", label="Anreicherung", icon="🍬")
st.page_link("pages/4_🧪_Schwefelung.py", label="Schwefelung", icon="🧪")
st.page_link("pages/5_🍋_Ansäuerung.py", label="Ansäuerung", icon="🍋")
st.page_link("pages/6_⚛️_Entsäuerung.py", label="Entsäuerung", icon="⚛️")
st.page_link("pages/7_🧮_Mischungsrechnung.py", label="Mischungsrechnung", icon="🧮")
st.page_link("pages/8_📖_Kellerbuch.py", label="Kellerbuch", icon="📖")