import streamlit as st
from oenologics_functions import decrease_acid

st.info("Entsäuerungsmethode wählen", icon="ℹ️")
st.header("Entsäuerung")

row1_col1, row1_col2 = st.columns(2)
liter_of_wine_for_deacidification = row1_col1.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000, key="liter_of_wine_for_deacidification")
type_of_deacidification = row1_col2.selectbox("Art der Entsäuerung", ("Entsäuerungskalk", "Doppelsalzentsäuerung"), index = None, placeholder="Entsäuerungsmethode auswählen...")


row2_col1, row2_col2 = st.columns(2)
total_acidity = row1_col1.number_input("Gesamtsäure (in g/l)", min_value=0.00, max_value=25.00)
desired_acidity = row1_col2.number_input("gewünschte Säure (in g/l)", min_value=0.00, max_value=25.00)


results_deacidification = decrease_acid(liter_of_wine_for_deacidification, type_of_deacidification, total_acidity, desired_acidity)
deacidification_quantity_in_kg = results_deacidification[0]
partial_quantity_in_l = results_deacidification[1]

st.write("######")


if type_of_deacidification == "Entsäuerungskalk" and deacidification_quantity_in_kg > 0 and desired_acidity > 0:
    st.metric(label="Entsäuerungskalk (in kg)", value=f"{deacidification_quantity_in_kg:.1f}")
    #0.67 g/l CaCO = - 1 g/l GS ber. als WS

elif type_of_deacidification == "Doppelsalzentsäuerung" and deacidification_quantity_in_kg > 0 and partial_quantity_in_l > 0 and desired_acidity > 0:
    
    result_deacidification1, result_deacidification2 = st.columns(2)
    
    result_deacidification1.metric(label="Doppelsalz (in kg)", value=f"{deacidification_quantity_in_kg:.1f}")
    result_deacidification2.metric(label="Teilmenge (in Liter)", value=f"{partial_quantity_in_l:.0f}")
    #0.67 g/l DS = - 1 g/l GS ber. als WS
