import streamlit as st

st.title("Wanderly")
st.subheader("Let AI generate your travel plan!")
st.caption("Provide us with  your destination, budget, how many days and your interest and your whole concerns will disapear instantly")

city = st.text_input("City")
days = st.selectbox("Amount of days", ['1','2','3','4','5'])
interests = st.multiselect('Interests', ['Musuems', 'Churches','Pubs','Cafes','Local Cusine', 'Beaches', 'Viewpoints'])

budget = st.number_input("Estimated daily budget", min_value=0)

if budget < 50:
    budget = "low"
elif budget > 250:
    budget = "high"
else:
    budget = "medium"

pace = st.radio("Your travel space", ["relaxed", "balanced", 'intense'])

summary = st.caption(f"Your trip: Destination:{city} Duration: {days} days")

# Budget: medium
# Pace: balanced
# Interests: museums, food, architecture")

st.button("Confirm", on_click=summary)

