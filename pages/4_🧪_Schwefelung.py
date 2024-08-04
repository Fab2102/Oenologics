import streamlit as st
from oenologics_functions import add_SO2

st.info("Schwefelung mit KPS", icon="ℹ️")
st.header("Schwefelung")

liter_of_wine_for_SO2 = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000, key="liter_of_wine_for_SO2")
additional_SO2 = st.number_input("zusätzliches SO2 (in mg/l)", min_value=0, max_value=100)
KPS_quantity_in_g = add_SO2(liter_of_wine_for_SO2, additional_SO2)
KPS_quantity_in_kg = KPS_quantity_in_g / 1000

st.write("######")

if KPS_quantity_in_g > 0:
    st.metric(label="KPS (in g)", value=f"{KPS_quantity_in_g:.1f}")
