import streamlit as st

st.title("Wanderly")
st.subheader("Let AI generate your travel plan!")
st.caption("Provide us with  your destination, budget, how many days and your interest and your whole concerns will disapear instantly")

city = st.text_input("City")
days = st.selectbox("Amount of days", ['1','2','3','4','5'])
interests = st.multiselect('Interests', ['Musuems', 'Churches','Pubs','Cafes','Local Cusine', 'Beaches', 'Viewpoints'])