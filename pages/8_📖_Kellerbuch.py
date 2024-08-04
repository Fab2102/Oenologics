import streamlit as st
import pandas as pd

st.info("Aufzeichnungen eintragen", icon="ℹ️")
st.header("Kellermaßnahmen")


data_df = pd.DataFrame(
    {"Tank_ID": [None], "Procedure": [None], "Date": [pd.NaT]})

edited_df = st.data_editor(
    data_df,
    column_config={
        "Tank_ID": st.column_config.NumberColumn("Tank Nr.", width="small"),
        "Procedure": st.column_config.TextColumn("Maßnahme"),
        "Date": st.column_config.DateColumn("Datum", format="DD.MM.YYYY"),   
    },
    hide_index=True,
    use_container_width=True,
    num_rows="dynamic")