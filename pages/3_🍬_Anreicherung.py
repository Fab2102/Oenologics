import streamlit as st
from oenologics_functions import add_sugar

st.info("Basierend auf vol.%", icon="ℹ️")
st.header("Anreicherung")

liter_of_wine = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000)
additonal_vol = st.number_input("Anreicherung (in vol.%)", min_value=0.00, max_value=3.00)
sugar_quantity_in_g = add_sugar(liter_of_wine, additonal_vol)
sugar_quantity_in_kg = sugar_quantity_in_g / 1000

st.write("######")

if sugar_quantity_in_kg > 0:
    st.metric(label="Zucker (in kg)", value=f"{sugar_quantity_in_kg:.1f}")