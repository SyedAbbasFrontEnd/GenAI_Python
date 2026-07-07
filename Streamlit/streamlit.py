import streamlit as st
import pandas as pd
import numpy as np
#first streamlit app
# st.title("My First StreamlitApp")
# st.write("Hello, Welcome to my first strreamlit application")
# st.write("Streamlit allow is to build a=data apps using only python!")


#Test & Markdown Display
# st.title("Text display in Streamlit")
# st.header("This is a Header")
# st.subheader("this is a plain text")
# st.text("This is a plain text.")

# st.markdown("""
# ###Markdown Support

# You can write ***bold-text***, *italic-text*, and create list:

# - Item 1
# - Item 2
# - Item 3
# """)


#User inpu - text input
# st.title("User Input Example")
# name = st.text_input("Enter your name")
# if name:
#     st.write(f"Hello {name}, Welcome to my streamlit App.")

# #Sliders & Number Input
# st.title("Interractive Sliders")
# age = st.slider("Select your age", 0, 100, 25)
# st.write("Your age is: ", age)
# number = st.number_input("Enter a number", min_value=0, max_value=100)
# st.write(f"Youentered: {number}")

#Select & Actions
# st.title("Button Example")
# if st.button("Click Me"):
#     st.success("You clicked the button!!")

#Select Box & Dropdown
# st.title("Select Box example")
# language = st.selectbox("Choose yu fav programming language", ["Python", "JAVA", "C++", "JAVASCRIPT"])
# st.write("You selected: ", language)

#Sidebar Layout
# st.title("Main Page")
# st.sidebar.title("Sidebar Memu")

# st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

#Column Layout
# st.title("Column layout")

# col1, col2 =st.columns(2)
# with col1:
#     st.header("Column2")
#     st.write("This is first colum")
# with col2:
#     st.header("Column2")
#     st.write("This is first colum")

# Dsiplat Data
# st.title("Dispaying Data")
# data = {
#     "Name": ["Syed", "Saqib", "Abbas"],
#     "city": ["Kolkata", "Patna", "Himachal"]
# }

# df = pd.DataFrame(data)
# st.dataframe(df)

#Charts in streamlit
# st.title("Charts Example")
# data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=["A", "B", "C"]
# )
# st.line_chart(data)

# File Upload

# st.title("File upload example")
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv", "xlsx"])
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df.head())

#Containers

# st.title("Containers Example")
# with st.container():
#     st.write("This is inside container")
#     st.write("useful for grouping")

# st.write("outside container")

#Session State(important)

st.title("Session state example")
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increate Counter"):
    st.session_state.counter +=1

st.write("Container value:", st.session_state.counter)