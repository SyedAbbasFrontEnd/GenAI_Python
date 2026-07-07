# 1️⃣ Your First Streamlit App
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! Welcome to my first Streamlit application.")
st.write("Streamlit allows us to build data apps using only Python!")


# 2️⃣ Text & Markdown Display
import streamlit as st

st.title("Text Display in Streamlit")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is plain text")

st.markdown("""
### Markdown Support

You can write **bold text**, *italic text*, and create lists:

- Item 1
- Item 2
- Item 3
""")


# 3️⃣ User Input — Text Input
import streamlit as st

st.title("User Input Example")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}! Welcome to Streamlit.")


# 4️⃣ Sliders & Number Inputs
import streamlit as st

st.title("Interactive Sliders")
age = st.slider("Select your age", 0, 100, 25)
st.write("Your age is:", age)
number = st.number_input("Enter a number", min_value=0, max_value=100)
st.write("You entered:", number)


# 5️⃣ Buttons & Actions
import streamlit as st

st.title("Button Example")

if st.button("Click Me"):
    st.success("You clicked the button!")


# 6️⃣ Select Box & Dropdowns
import streamlit as st

st.title("Select Box Example")

language = st.selectbox(
    "Choose your favorite programming language",
    ["Python", "Java", "C++", "JavaScript"]
)

st.write("You selected:", language)


# 7️⃣ Sidebar Layout
import streamlit as st

st.title("Main Page")

st.sidebar.title("Sidebar Menu")

option = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "About", "Contact"]
)

st.write("You selected:", option)


# 8️⃣ Columns Layout
import streamlit as st

st.title("Columns Layout")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first column.")

with col2:
    st.header("Column 2")
    st.write("This is the second column.")


# 9️⃣ Displaying Data
import streamlit as st
import pandas as pd

st.title("Displaying Data")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
st.dataframe(df)


# 🔟 Charts in Streamlit
import streamlit as st
import pandas as pd
import numpy as np

st.title("Charts Example")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)


# 1️⃣1️⃣ File Upload
import streamlit as st
import pandas as pd

st.title("File Upload Example")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data")
    st.dataframe(df.head())


# 1️⃣2️⃣ Containers
import streamlit as st

st.title("Containers Example")

with st.container():
    st.write("This is inside a container")
    st.write("Useful for grouping components")

st.write("Outside the container")


# 1️⃣3️⃣ Session State (Very Important)
import streamlit as st

st.title("Session State Example")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase Counter"):
    st.session_state.counter += 1

st.write("Counter Value:", st.session_state.counter)