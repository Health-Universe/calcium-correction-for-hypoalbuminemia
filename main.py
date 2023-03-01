import streamlit as st

def calculate_corrected_calcium(total_calcium, albumin):
    """
    Calculate corrected calcium based on total calcium and albumin levels using the formula:
    Corrected calcium = total calcium + 0.8 * (4 - albumin)
    """
    corrected_calcium = total_calcium + 0.8 * (4 - albumin)
    return corrected_calcium

st.title("Calcium Correction for Hypoalbuminemia")

# User input for total calcium level
total_calcium = st.number_input("Enter total calcium level (mg/dL)")

# User input for albumin level
albumin = st.number_input("Enter albumin level (g/dL)")

# Calculate corrected calcium and display the result
corrected_calcium = calculate_corrected_calcium(total_calcium, albumin)
st.write("Corrected calcium level: ", corrected_calcium, "mg/dL")
