import streamlit as st

st.title("KMW zu vol.%")

st.write("### °KMW eingeben")
col1 = st.columns(1)[0]
kmw_value = col1.number_input("°KMW", min_value=0.00, max_value=50.00, format="%.2f")


vol_percent = ((1.267 * (0.71173 * kmw_value - 2.55)) / (0.267 * (0.71173 * kmw_value - 2.55) + 100)) * 100

st.write("######")

col2 = st.columns(1)[0]
col2.metric(label="vol.%", value=f"{vol_percent:.2f}")  