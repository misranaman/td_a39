import streamlit as st

st.title("Welcome to Your AI Wedding Planner")

planning_list = ["catering", "decoration", "photography", "transportation", "hotel", "banquet"]

details_dict = {}
services_data = [
    {
        "category": "catering",
        "vendor": "Royal Feast Caterers",
        "cost": 150000,
        "status": "Confirmed"
    },
    {
        "category": "decoration",
        "vendor": "Bloom Floral & Themes",
        "cost": 75000,
        "status": "In Progress"
    },
    {
        "category": "photography",
        "vendor": "Candid Lens Studio",
        "cost": 60000,
        "status": "Confirmed"
    },
    {
        "category": "transportation",
        "vendor": "City Cabs & Bus Rentals",
        "cost": 25000,
        "status": "Pending"
    },
    {
        "category": "hotel",
        "vendor": "Grand Heritage Hotel",
        "cost": 120000,
        "status": "Confirmed"
    },
    {
        "category": "banquet",
        "vendor": "Crystal Ballroom",
        "cost": 200000,
        "status": "Confirmed"
    }
]

plan_item = st.selectbox("Select you planning item", planning_list)
for d in services_data:
    if d["category"] == plan_item:
        for key, value in d.items():
            st.write(key, value)
