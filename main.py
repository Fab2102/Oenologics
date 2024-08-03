import streamlit as st
import pandas as pd
from datetime import date
from datetime import time



st.set_page_config(page_title="Oenologics", layout="centered", page_icon="🍷")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍇Alkoholausbeute", "🍬Anreicherung", "🧪Schwefelung", "🍋Ansäuerung", "📖Kellerbuch"])



### calculastions for metrics

def kmw_to_vol(kmw_input_value):
    result_vol = ((1.267 * (0.71173 * kmw_input_value - 2.55)) / (0.267 * (0.71173 * kmw_input_value - 2.55) + 100)) * 100
    return result_vol

def vol_to_kmw(vol_input_value):
    result_kmw = (-0.9931915 * vol_input_value - 3.23085) / (0.0019003191 * vol_input_value - 0.901761191)
    return result_kmw

def add_sugar(liter_of_wine, additonal_vol):
    sugar_quant_g = liter_of_wine * (additonal_vol * 17)
    ### multiplied by 17 because 1 vol.% = 17 g/l sugar
    return sugar_quant_g
    
def add_SO2(liter_of_wine_for_SO2, additional_SO2):
    KPS_quant_g = (liter_of_wine_for_SO2 * additional_SO2 * 2) / 1000
    ### multiplied by 2 because of KPS
    return KPS_quant_g
 
def add_acid(liter_of_wine_for_acidification, additonal_acid, type_of_acid):
    
    acid_quant_g = 0
    acid_quant_ml = 0
    
    if type_of_acid == "Weinsäure":
        acid_quant_g = liter_of_wine_for_acidification * additonal_acid * 1
        #1.00 g/l WS = + 1 g/l GS ber. als WS
        
    elif type_of_acid == "Äpfelsäure": 
        acid_quant_g = liter_of_wine_for_acidification * additonal_acid * 0.89
        #0.89 g/l ÄS = + 1 g/l GS ber. als WS
        
    elif type_of_acid == "Milchsäure":
        acid_quant_g = liter_of_wine_for_acidification * additonal_acid * 1.50
        acid_quant_ml = liter_of_wine_for_acidification * additonal_acid * 1.25
        #1.25 ml/l MS = + 1 g/l GS ber. als WS
        #1.50 g/l  MS = + 1 g/l GS ber. als WS
        
    elif type_of_acid == "Zitronensäure":
        acid_quant_g = liter_of_wine_for_acidification * additonal_acid * 0.85
        #0.85 g/l ZS = + 1 g/l GS ber. als WS
    
    return acid_quant_g, acid_quant_ml
 
 
 
### displaying tabs

with tab1:
    st.info("Offizielle Formel der Landesregierung NÖ", icon="ℹ️")
    st.write("######")
    switch_calc = st.toggle("Berechnung umkehren")
    
    if switch_calc:
        
        st.header("vol.% zu °KMW")
        
        vol_input_value = st.number_input("vol.%", min_value=0.00, max_value=30.00)    
        kmw_output_value = vol_to_kmw(vol_input_value)
        
        st.write("######")
        if kmw_output_value > 4:
            st.metric(label="°KMW", value=f"{kmw_output_value:.2f}")
        
    else:
        
        st.header("KMW zu vol.%")
    
        
        kmw_input_value = st.number_input("°KMW", min_value=0.00, max_value=60.00)
        vol_output_value = kmw_to_vol(kmw_input_value)
        
        st.write("######")
        
        if vol_output_value > 0:
            st.metric(label="vol.%", value=f"{vol_output_value:.2f}")


      
with tab2:
    st.info("Anreicherung auf Basis von vol.%", icon="ℹ️")
    st.header("Anreicherung")

    liter_of_wine = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000)
    additonal_vol = st.number_input("Anreicherung (in vol.%)", min_value=0.00, max_value=3.00)
    sugar_quantity_in_g = add_sugar(liter_of_wine, additonal_vol)
    sugar_quantity_in_kg = sugar_quantity_in_g / 1000
    
    st.write("######")
    
    if sugar_quantity_in_kg > 0:
        st.metric(label="Zucker (in kg)", value=f"{sugar_quantity_in_kg:.1f}")
    
    
    
with tab3:
    st.info("Schwefelung mit KPS", icon="ℹ️")
    st.header("Schwefelung")
    
    liter_of_wine_for_SO2 = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000, key="liter_of_wine_for_SO2")
    additional_SO2 = st.number_input("zusätzliches SO2 (in mg/l)", min_value=0, max_value=100)
    KPS_quantity_in_g = add_SO2(liter_of_wine_for_SO2, additional_SO2)
    KPS_quantity_in_kg = KPS_quantity_in_g / 1000
    
    st.write("######")
    
    if KPS_quantity_in_g > 0:
        st.metric(label="KPS (in g)", value=f"{KPS_quantity_in_g:.1f}")



with tab4:
    st.info("Spezifische Säure auswählen", icon="ℹ️")
    st.header("Ansäuerung")
    
    liter_of_wine_for_acidification = st.number_input("Weinmenge (in Liter)", min_value=0, max_value=200000, key="liter_of_wine_for_acidification")
    additonal_acid = st.number_input("Ansäuerung der titrierbaren Gesamtsäure berechnet als Weinsäure (in g/l)", min_value=0.00, max_value=3.00)
    type_of_acid = st.selectbox("Art der Säure", ("Weinsäure", "Äpfelsäure", "Milchsäure", "Zitronensäure"), index = None, placeholder="Säure auswählen...")
    acid_quantity = add_acid(liter_of_wine_for_acidification, additonal_acid, type_of_acid)
    acid_quantity_in_g = acid_quantity[0]
    acid_quantity_in_kg = acid_quantity[0] / 1000
    acid_quantity_in_ml = acid_quantity[1]
    acid_quantity_in_l = acid_quantity[1] / 1000
    
    st.write("######")
    
    if type_of_acid == "Weinsäure":
        st.metric(label="Weinsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
        #1.00 g/l WS = + 1 g/l GS ber. als WS
    
    elif type_of_acid == "Äpfelsäure":
        st.metric(label="Äpfelsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
        #0.89 g/l ÄS = + 1 g/l GS ber. als WS
        
    elif type_of_acid == "Milchsäure":
        st.metric(label="Milchsäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
        st.metric(label="Milchsäure (in Liter)", value=f"{acid_quantity_in_l:.1f}")
        #1.25 ml/l MS = + 1 g/l GS ber. als WS
        #1.50 g/l  MS = + 1 g/l GS ber. als WS
        
    elif type_of_acid == "Zitronensäure":
         st.metric(label="Zitronensäure (in kg)", value=f"{acid_quantity_in_kg:.1f}")
        #0.85 g/l ZS = + 1 g/l GS ber. als WS



with tab5:
    st.write("######")
    st.header("Kellermaßnahmen")
    st.write("######")
    
    
    data_df = pd.DataFrame(
        {"Tank_ID": [None], "Procedure": [None], "Date": [pd.NaT], "Time" : [pd.NaT]}
    )

    edited_df = st.data_editor(
        data_df,
        column_config={
            "Tank_ID": st.column_config.NumberColumn("Tank Nr."),
            "Procedure": st.column_config.TextColumn("Maßnahme"),
            "Date": st.column_config.DateColumn("Datum", format="DD.MM.YYYY"),
            "Time": st.column_config.TimeColumn("Uhrzeit", format="HH:mm")   
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic"
    )
    
    
    st.write("######")
    # st.button("Download Excel File")
