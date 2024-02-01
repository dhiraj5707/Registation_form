import streamlit as st
import datetime


st.title("Registation Form 😎")
name=st.text_input("Enter Your Name:")
fname=st.text_input("Enter Your Father Name:")
Ename=st.text_input("Enter Email Address:")
cname=st.text_input("Enter Your Contact Number:")
dob= st.date_input("Enter Your Date of Birth:", datetime.date(2000, 5, 3))
adr=st.text_area("Enter Your Address:")

button=st.button("Done")
if button:
    st.markdown(f"""
    Name : {name},
    Father Name : {fname},
    Email Address:{Ename},
    Contact Number:{cname},
    DOB:{dob}
    Address:-:{adr} """)