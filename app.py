import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator App")

# Input fields
st.subheader("Enter Numbers")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.radio("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("❌ Cannot divide by zero!")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit")
