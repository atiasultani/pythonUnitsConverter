import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit):
    # Length conversions
    if from_unit == "Meters" and to_unit == "Centimeters":
        return round(value * 100, 2)  # meters to centimeters
    elif from_unit == "Centimeters" and to_unit == "Meters":
        return round(value / 100, 2)  # centimeters to meters
    elif from_unit == "Meters" and to_unit == "Kilometers":
        return round(value / 1000, 2)  # meters to kilometers
    elif from_unit == "Kilometers" and to_unit == "Meters":
        return round(value * 1000, 2)  # kilometers to meters
    elif from_unit == "Kilometers" and to_unit == "Centimeters":
        return round(value * 100000, 2)  # kilometers to centimeters
    elif from_unit == "Centimeters" and to_unit == "Kilometers":
        return round(value / 100000, 2)  # centimeters to kilometers
    elif from_unit == "Feet" and to_unit == "Meters":
        return round(value * 0.3048, 2)  # feet to meters
    elif from_unit == "Meters" and to_unit == "Feet":
        return round(value / 0.3048, 2)  # meters to feet

    # Weight conversions
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return round(value * 0.453592, 2)  # pounds to kilograms
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        return round(value / 0.453592, 2)  # kilograms to pounds

    # Temperature conversions
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return round((value - 32) * 5.0/9.0, 2)  # Fahrenheit to Celsius
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return round((value * 9.0/5.0) + 32, 2)  # Celsius to Fahrenheit

    # Velocity conversions (m/s to km/h and vice versa)
    elif from_unit == "m/s" and to_unit == "km/h":
        return round(value * 3.6, 2)  # meters per second to kilometers per hour
    elif from_unit == "km/h" and to_unit == "m/s":
        return round(value / 3.6, 2)  # kilometers per hour to meters per second

    # Distance conversions
    elif from_unit == "Miles" and to_unit == "Kilometers":
        return round(value * 1.60934, 2)  # miles to kilometers
    elif from_unit == "Kilometers" and to_unit == "Miles":
        return round(value / 1.60934, 2)  # kilometers to miles

    # Liters and Gallons
    elif from_unit == "Liters" and to_unit == "Gallons":
        return round(value * 0.264172, 2)  # liters to gallons
    elif from_unit == "Gallons" and to_unit == "Liters":
        return round(value / 0.264172, 2)  # gallons to liters

    # Inches and Centimeters
    elif from_unit == "Inches" and to_unit == "Centimeters":
        return round(value * 2.54, 2)  # inches to centimeters
    elif from_unit == "Centimeters" and to_unit == "Inches":
        return round(value / 2.54, 2)  # centimeters to inches

    else:
        return value  # No conversion if same units

# Streamlit UI

# Set the title of the app
st.title("Unit Converter")

# Add description and instructions
st.markdown("""
    This is a simple unit converter. You can convert between different units like:
    - Length: Meters, Centimeters, Kilometers, and Feet
    - Weight: Kilograms and Pounds
    - Temperature: Celsius and Fahrenheit
    - Velocity: m/s and km/h
    - Distance: Miles and Kilometers
    - Volume: Liters and Gallons
    - Length: Inches and Centimeters
""")

# Create user input fields for conversion
value = st.number_input("Enter the value to convert", min_value=0.0, step=0.1)
category = st.selectbox("Select the category", ["Length", "Weight", "Temperature", "Velocity", "Distance", "Volume"])

# Based on category, show relevant units
if category == "Length":
    from_unit = st.selectbox("From Unit", ["Feet", "Meters", "Centimeters", "Kilometers"])
    to_unit = st.selectbox("To Unit", ["Feet", "Meters", "Centimeters", "Kilometers"])
elif category == "Weight":
    from_unit = st.selectbox("From Unit", ["Pounds", "Kilograms"])
    to_unit = st.selectbox("To Unit", ["Pounds", "Kilograms"])
elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Fahrenheit", "Celsius"])
    to_unit = st.selectbox("To Unit", ["Fahrenheit", "Celsius"])
elif category == "Velocity":
    from_unit = st.selectbox("From Unit", ["m/s", "km/h"])
    to_unit = st.selectbox("To Unit", ["m/s", "km/h"])
elif category == "Distance":
    from_unit = st.selectbox("From Unit", ["Miles", "Kilometers"])
    to_unit = st.selectbox("To Unit", ["Miles", "Kilometers"])
else:  # Volume
    from_unit = st.selectbox("From Unit", ["Liters", "Gallons"])
    to_unit = st.selectbox("To Unit", ["Liters", "Gallons"])

# Perform conversion
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

# Adding custom CSS to improve the design
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
