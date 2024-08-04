### calculations for metrics

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

def decrease_acid(liter_of_wine_for_deacidification, type_of_deacidification, total_acidity, desired_acidity):
    
    deacidification_quant_kg = 0
    deacidification_partial_quant_l = 0
    less_acid = total_acidity - desired_acidity
    
    if type_of_deacidification == "Entsäuerungskalk":
        deacidification_quant_kg = (liter_of_wine_for_deacidification * less_acid * 0.67) / 1000
        #0.67 g/l CaCO = - 1 g/l GS ber. als WS
        
    elif type_of_deacidification == "Doppelsalzentsäuerung":
        deacidification_quant_kg = (liter_of_wine_for_deacidification * less_acid * 0.67) / 1000
        deacidification_partial_quant_l = (liter_of_wine_for_deacidification * less_acid) / (total_acidity - 3)
        #0.67 g/l DS = - 1 g/l GS ber. als WS
        
    return deacidification_quant_kg, deacidification_partial_quant_l

def mixing_liquids(liquid1, liquid2, conc1, conc2):
    conc_quant = 0
    
    liquid_quant = liquid1 + liquid2
    
    if liquid_quant > 0:
        conc_quant = (liquid1 * conc1 + liquid2 * conc2) / (liquid1 + liquid2)
    
    return liquid_quant, conc_quant