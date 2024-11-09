import streamlit as st

def main():
    st.title("Hello, from Streamlit")
    if st.button("Click me!!"):
        st.write("Button clicked")
    if st.checkbox("check me"):
        st.write("You're seeing this tag because you checked this checkbox")
    user_imput_text=st.text_input("Enter text","Sample")
    st.write("You entered ", user_imput_text)
    user_imput_number=st.number_input("Enter your age", min_value=0,max_value=100)
    st.write("You input", user_imput_number)
    user_input_textarea=st.text_area("Enter your message")
    st.write(f"Message:", {user_input_textarea})
    user_input_radio=st.radio("Pick one",["Opsioni1","Opsioni2","Opsioni3"])
    st.write(f"You Chose:{user_input_radio}")
    if st.button("Success"):
        st.success("Operation was succesful")
    # try:
    #     1/0
    # except Exception as e:
    #     st.exception(e)

if __name__ == "__stream__":
    main()