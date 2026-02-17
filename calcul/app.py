import streamlit as st

st.title("Simple Calculator 💻")

x = st.number_input("Enter first number")
y = st.number_input("Enter second number")


op = st.selectbox("Select operation", ["+", "-", "*", "/"])


if st.button("Calculate"):
    if op == "+":
        st.success(f"Result: {x + y}")
    elif op == "-":
        st.success(f"Result: {x - y}")
    elif op == "*":
        st.success(f"Result: {x * y}")
    elif op == "/":
        if y != 0:
            st.success(f"Result: {x / y}")
        else:
            st.error("Cannot divide by zero ❌")
