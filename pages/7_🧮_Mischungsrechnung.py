import streamlit as st
from oenologics_functions import mixing_liquids

st.info("Endkonzentration berechnen", icon="ℹ️")
st.header("Mischungsrechnung")

row1_col1, row1_col2 = st.columns(2)
liquid1 = row1_col1.number_input("Flüssigkeit 1 (in Liter)", min_value=0, max_value=200000)
conc1 = row1_col2.number_input("Konzentration 1", min_value=0.00, max_value=10000.00)

row2_col1, row2_col2 = st.columns(2)
liquid2 = row2_col1.number_input("Flüssigkeit 2 (in Liter)", min_value=0, max_value=200000)
conc2 = row2_col2.number_input("Konzentration 2", min_value=0.00, max_value=10000.00)


unit = st.selectbox("Einheit", ("g/l", "mg/l", "°KMW", "vol.%"))


results_mixing_liquids = mixing_liquids(liquid1, liquid2, conc1, conc2)
total_volume_l = results_mixing_liquids[0]
total_concentration = results_mixing_liquids[1]

st.write("######")


if liquid1 and conc1 and liquid2 and conc2 and total_volume_l and total_concentration > 0:
    results_col1, results_col2 = st.columns(2)

    results_col1.metric(label="Gesamtmenge (in Liter)", value=f"{total_volume_l:.0f}")
    results_col2.metric(label=f"Gesamtkonzentration (in {unit})", value=f"{total_concentration:.2f}")