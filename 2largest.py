import streamlit as st

def get_number_input(prompt, default=0):
    """
    Gets a number input from the user with error handling for infinite values.

    Args:
        prompt (str): The text to display for the input field.
        default (float, optional): The default value to return if the user
            leaves the input blank. Defaults to 0.

    Returns:
        float: The user-entered number, or the default value if an error occurs.
    """

    value = st.number_input(prompt)
    if value is None:  # Handle case when user leaves input blank
        return default
    elif value == float('inf') or value == float('-inf'):
        st.error("Please enter a finite number.")
        return None  # Or return a specific value to indicate error (optional)
    else:
        return value

def find_largest(num1, num2, num3):
    """Finds the largest number among three given numbers."""
    largest = max(num1, num2, num3)
    return largest

st.title("Find the Largest Number")

# Get user input for the three numbers using the get_number_input function
num1 = get_number_input("Enter the first number:")
if num1 is None:  # Handle cases where user enters an invalid value
    continue  # Skip to the next input field if an error occurred

num2 = get_number_input("Enter the second number:")
if num2 is None:
    continue

num3 = get_number_input("Enter the third number:")
if num3 is None:
    continue

# Call the function to find the largest number
largest_number = find_largest(num1, num2, num3)

# Display the result
st.write("The largest number is:", largest_number)
