import streamlit as st


# Streamlit app code
def main():
    st.title("Simple Streamlit App")
    name = st.text_input("Enter your name:", "")
    age = st.slider("Select your age:", 0, 100, 25)

    if st.button("Submit"):
        st.write(f"Hello, {name}! You are {age} years old.")

        # Exit after the button click (simulate one-time run)
        st.write("Exiting the app now...")
        st.stop()
    else:
        st.write("Please enter your details.")

    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.write("You have agreed!")


if __name__ == "__main__":
    main()
