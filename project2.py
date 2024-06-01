import streamlit as st

name=st.text_input("enter your name: ")
fname=st.text_input("enter your father name: ")
booth=st.number_input("enter the booth_number")
address=st.text_area("enter your address: ")
status=st.selectbox("enter the status",("select option","vote casted","vote not casted"))

button=st.button("submit")
if button:
    st.markdown(f"""
    Name : {name}
    Father name : {fname}
    Booth : {booth}
    address : {address}
    status : {status}""")
