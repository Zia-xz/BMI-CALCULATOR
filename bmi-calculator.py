import json
import json
import pandas as pd
import math

BMI_CHART = {
    "Underweight"            : {'lower' : 0.0, 'upper' : 18.49,    "risk" : 'Malnutrition Risk'},
    "Normal Weight"          : {'lower' : 18.50,     'upper' : 24.99,    "risk" : 'Low Risk'},
    "Overweight"             : {'lower' : 25,        'upper' : 29.99,    "risk" : 'Enhanced Risk'},
    "Moderately Obese"       : {'lower' : 30,        'upper' : 34.99,    'risk' : 'Medium Risk'},
    "Severely Obese"         : {'lower' : 35,        'upper' : 39.99,    'risk' : 'High Risk'},
    "Very Severly Obese"     : {'lower' : 40,        'upper' : 100.00, 'risk' : 'Very High Risk'}
    }

def calculate_bmi(height,weight):
    bmi = round(weight / (height**2), 2)
    return bmi


def category_and_risk(bmi_value):
    for category, range_risk in BMI_CHART.items():
        
        lower_limit = range_risk['lower']
        upper_limit = range_risk['upper']
        risk = range_risk['risk']
        
        if lower_limit <= bmi_value <= upper_limit:
            
            return category, risk


def generate_data(row):
    height_cm = row['HeightCm']
    weight_kg = row["WeightKg"]
    
    bmi = calculate_bmi(height_cm, weight_kg )
    
    category, risk = category_and_risk(bmi)
    
    row['BMI value'] = bmi
    row['BMI Category'] = category
    row['Health risk'] = risk
    
    return row


def main(json_file, result_file_type = 'csv'):
    with open(json_file, 'r') as fp:
        data = json.load(fp)
   
    df = pd.DataFrame(data)
    df = df.apply(generate_data, axis = 1)
    
    file_name = "result.csv"
    df.to_csv(file_name, index=False)
    print(f"data saved : {file_name}")
    

    
if __name__ == '__main__':
    json_file = r"C:\Users\ZIA\Videos\BMI_DATA.json"
    result_file_type = 'csv'
    main(json_file, result_file_type = result_file_type ) 
