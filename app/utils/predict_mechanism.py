import pandas as pd
import joblib
import json

def predict_mechanism(json_data):
    model = joblib.load('./best_model.joblib')
    target_encoder = joblib.load('./target_encoder.joblib')
    
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
        
    df = pd.DataFrame([data])
    
    binary_columns = [col for col in df.columns if col != 'sexo_' and col != 'area_' 
                     and col != 'edad_' and col != 'prob_consu']
    for col in binary_columns:
        df[col] = df[col].replace({1: 1, 2: 0}).astype(int)
    
    def get_age_group(age):
        if age <= 6: return '0-6'
        elif age <= 11: return '7-11'
        elif age <= 17: return '12-17'
        elif age <= 28: return '18-28'
        elif age <= 59: return '29-59'
        else: return '60+'
    
    df['edad_group'] = df['edad_'].apply(get_age_group)
    df = df.drop('edad_', axis=1)
    
    area_categories = [1, 2, 3] 
    for area in area_categories:
        df[f'area_{area}'] = (df['area_'] == area).astype(int)
    df = df.drop('area_', axis=1)
    
    age_categories = ['0-6', '7-11', '12-17', '18-28', '29-59', '60+']
    for age in age_categories:
        df[f'edad_{age}'] = (df['edad_group'] == age).astype(int)
    df = df.drop('edad_group', axis=1)
    
    df['sexo_'] = (df['sexo_'] == 'M').astype(int)
    
    df = df.drop('enfermedad_cronica', axis=1, errors='ignore')
    
    expected_columns = ['abuso_alco', 'antec_tran', 'antec_v_a', 'area_1', 'area_2', 'area_3', 
                       'esco_educ', 'hist_famil', 'idea_suici', 'inten_prev', 'maltr_fps', 
                       'muerte_fam', 'plan_suici', 'prob_consu', 'prob_econo', 'prob_famil', 
                       'prob_labor', 'prob_legal', 'prob_parej', 'sexo_', 'suici_fm_a', 
                       'tran_depre', 'trast_bipolaridad', 'trast_personalidad', 'edad_0-6', 
                       'edad_12-17', 'edad_18-28', 'edad_29-59', 'edad_60+', 'edad_7-11']
    
    df = df[expected_columns]
    
    prediction = model.predict(df)[0]
    mechanism = target_encoder.inverse_transform([prediction])[0]
    
    return mechanism