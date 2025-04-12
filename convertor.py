# Unit Convertor:
#Build a google unit convertor using python and streamlit

import streamlit as st
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: #f0f2f6;
    }
    .stApp{
        background: linear-gradient(#135deg, #bcbcbc ,#cfe2f3)
        padding:30px;
        border-radius:15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3) 
    }
    h1{
        color: white;
        text-align: center;
        margin-bottom: 20px;
        font-size:36px;
        margin-top:0px
    }
    .stButton>button{
        background: linear-gradient(#45deg, #0b5394 ,#351c75);
        color: black;
        #border: none;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-size: 18px;
        font-weight: bold;
        letter-spacing: 1px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
        
    }
    .stButton>button:hover{
        background: linear-gradient(#45deg, #92fe9d ,#00c9ff);
        transform: translateY(1.05);
        box-shadow: 0px 8px 20px rgba(0,201,255,0.6);
        color: #000000;
    }
    .result-box{
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
        margin-top: 20px;
        color:rgb(13, 45, 54);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
        opacity: 0.7;
    }
    </style>
    """,
     unsafe_allow_html=True
)

st.markdown("<h1>Unit Convertor</h1>", unsafe_allow_html=True)
st.write("""
    <div style="text-align: center; color :white ">
        <p style = "font-weight:bold; background-color:rgb(220, 107, 173)">Convert between different units of Length, Weight, and Temperature.</p>
    </div>
    """, unsafe_allow_html=True)
#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value =0.0 , min_value=0.0 ,step=0.1)
col1, col2 = st.columns(2)

#length conversion
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches","Feet"])
    
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches","Feet"])
    
elif conversion_type == "Weight":
    with col1:        
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celcius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celcius", "Fahrenheit", "Kelvin"])

def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters' : 1 , 'Kilometers' : 0.001, 'Centimeters' : 100, 'Millimeters' : 1000,
        'Miles' : 0.000621371, 'Yards': 1.09361 , 'Feet': 3.28084, 'Inches' : 39.3701
        }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit): 
    weight_units = {
        'Kilograms' : 1 , 'Grams' : 1000, 'Milligrams' : 1000000, 'Pounds' : 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit): 
    if from_unit == "Celcius" : 
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value+273.15 if to_unit =="Kelvin" else value
    elif from_unit == "Fahrenheit": 
        return (value -32) * 5/9 if to_unit == "Celcius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit =="Kelvin": 
        return value - 273.15 if to_unit == "Celsius" else (value-273.15)*9/5+32 if to_unit == "Fahrenheit" else value
    return value

if st.button("Convert"): 
    if conversion_type == "Length": 
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight": 
        result =weight_convertor(value,from_unit,to_unit)
    elif conversion_type == "Temperature" : 
        result = temp_convertor(value,from_unit,to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit} </div>", unsafe_allow_html = True)
st.markdown("<div class='footer'> Created with love by Habiba Khan </div>", unsafe_allow_html = True)




