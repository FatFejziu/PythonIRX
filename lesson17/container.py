import streamlit as st
# with st.container():
#     st.header("This is a container")
#     st.write("This is inside the container")
# st.write("Outside the container")


# st.sidebar.header("Sidebar")
# st.sidebar.write("This is sidebar")
# st.sidebar.selectbox("Chose an option",["Option1","Option2","Option3"])
# st.sidebar.radio("Go to",["Home","Data","Settings"])
#
# with st.form("my_form", clear_on_submit=True):
#     name=st.text_input("Name")
#     age=st.slider("Age", min_value=0, max_value=100)
#     email=st.text_input("Email")
#     biography=st.text_area("Short Bio")
#     terms=st.checkbox("I agree to the terms and conditions")
#     submit_button=st.form_submit_button(label="Submit")
# if submit_button:
#     st.write(f"Name{name}")
#     st.write(f"Age{age}")
#     if terms:
#         st.write("You have agreed to the terms and conditions")
#     else:
#         st.write("You did not agree to the terms and conditions")

tab1,tab2,tab3=st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.header("Tab1")
    st.write("content")

with tab1:
    st.header("Tab2")
    st.write("content")

with tab1:
    st.header("Tab3")
    st.write("content")