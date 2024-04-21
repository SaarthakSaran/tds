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

# Option 1: Using a loop for user input handling (choose one option)

# while True:  # Introduce a loop for user input handling
#     num1 = get_number_input("Enter the first number:")
#     if num1 is not None:  # Check if valid input (not None)
#         break  # Exit the loop if valid input received

#     # Display error message (optional)

#     # Continue to the next iteration if invalid input entered

# Option 2: Using conditional logic (if statements)

num1 = get_number_input("Enter the first number:")
if num1 is None:
    st.error("Please enter a valid number.")

num2 = get_number_input("Enter the second number:")
if num2 is None:
    st.error("Please enter a valid number.")

num3 = get_number_input("Enter the third number:")
if num3 is None:
    st.error("Please enter a valid number.")

# ... (rest of the code to find and display the largest number)

# If using Option 1, uncomment the lines inside the loop and comment out
# the lines below this point.

# Call the function to find the largest number (assuming valid inputs now)
largest_number = find_largest(num1, num2, num3)

# Display the result
st.write("The largest number is:", largest_number)
