import streamlit as st
from oenologics_functions import add_acid

st.info("Spezifische Säure auswählen", icon="ℹ️")
st.header("Ansäuerung")


liter_of_wine_for_acidification = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000, key="liter_of_wine_for_acidification")
additonal_acid = st.number_input("Ansäuerung (berechnet als Weinsäure in g/l)", min_value=0.00, max_value=3.00)
type_of_acid = st.selectbox("Art der Säure", ("Weinsäure", "Äpfelsäure", "Milchsäure", "Zitronensäure"), index = None, placeholder="Säure auswählen...")
acid_quantity = add_acid(liter_of_wine_for_acidification, additonal_acid, type_of_acid)
acid_quantity_in_kg = acid_quantity[0] / 1000
acid_quantity_in_l = acid_quantity[1] / 1000


st.write("######")


if type_of_acid == "Weinsäure":
    st.metric(label="Weinsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
    #1.00 g/l WS = + 1 g/l GS ber. als WS

elif type_of_acid == "Äpfelsäure":
    st.metric(label="Äpfelsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
    #0.89 g/l ÄS = + 1 g/l GS ber. als WS
    
elif type_of_acid == "Milchsäure":
    
    result_lactic_acid1, result_lactic_acid2 = st.columns(2)
    
    result_lactic_acid1.metric(label="Milchsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
    result_lactic_acid2.metric(label="Milchsäure (in Liter)", value=f"{acid_quantity_in_l:.1f}")
    #1.25 ml/l MS = + 1 g/l GS ber. als WS
    #1.50 g/l  MS = + 1 g/l GS ber. als WS
    
elif type_of_acid == "Zitronensäure":
        st.metric(label="Zitronensäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
    #0.85 g/l ZS = + 1 g/l GS ber. als WS