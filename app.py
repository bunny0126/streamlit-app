import streamlit as st

# Setting page title and header
st.title("Welcome to My Basic Streamlit App")
st.header("A Simple Interactive Application")

# Adding a text input
user_name = st.text_input("Enter your name:", "Type here...")

# Displaying a greeting based on user input
if user_name and user_name != "Type here...":
    st.write(f"Hello, {user_name}! Welcome to the app!")

# Adding a slider for age
age = st.slider("Select your age:", min_value=0, max_value=100, value=25)
st.write(f"Your age is: {age}")

# Adding a button and showing a message when clicked
if st.button("Click Me!"):
    st.success("Button clicked! Great job!")

# Adding a simple checkbox
show_message = st.checkbox("Show a fun fact?")
if show_message:
    st.info("Fun Fact: Streamlit makes building web apps with Python super easy!")

# Adding a selectbox for favorite color
color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green", "Yellow"])
st.write(f"Your favorite color is: {color}")

# Displaying a sample dataframe
st.header("Sample Data")
data = {"Column 1": [1, 2, 3, 4], "Column 2": [10, 20, 30, 40]}
st.dataframe(data)

# Adding a simple line chart
st.header("Simple Line Chart")
chart_data = {"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]}
st.line_chart(chart_data)