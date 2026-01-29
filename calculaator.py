import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# Calculate result
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("❌ Division by zero is not allowed")
