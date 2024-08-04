import streamlit as st
from oenologics_functions import kmw_to_vol
from oenologics_functions import vol_to_kmw



st.info("Formel der Landesreg. NÖ", icon="ℹ️")
switch_calc = st.toggle("Berechnung umkehren")
    
st.write("######")
    
if switch_calc:
    
    st.header("°KMW ← vol.%")
    
    vol_input_value = st.number_input("vol.%", min_value=0.00, max_value=30.00)    
    kmw_output_value = vol_to_kmw(vol_input_value)
    
    st.write("######")
    if kmw_output_value > 4:
        st.metric(label="°KMW", value=f"{kmw_output_value:.2f}")
    
else:
    
    st.header("°KMW → vol.%")

    
    kmw_input_value = st.number_input("°KMW", min_value=0.00, max_value=60.00)
    vol_output_value = kmw_to_vol(kmw_input_value)
    
    st.write("######")
    
    if vol_output_value > 0:
        st.metric(label="vol.%", value=f"{vol_output_value:.2f}")