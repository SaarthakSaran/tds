import streamlit as st

def find_largest(num1, num2, num3):
    """Finds the largest number among three given numbers."""
    largest = max(num1, num2, num3)
    return largest

st.title("Find the Largest Number")

# Get user input for the three numbers
num1 = st.number_input("Enter the first number:", min_value=float('-inf'), max_value=float('inf'))
num2 = st.number_input("Enter the second number:", min_value=float('-inf'), max_value=float('inf'))
num3 = st.number_input("Enter the third number:", min_value=float('-inf'), max_value=float('inf'))

# Call the function to find the largest number
largest_number = find_largest(num1, num2, num3)

# Display the result
if st.button("Find Largest"):  # Add a button to trigger calculation on user action
    st.write("The largest number is:", largest_number)
