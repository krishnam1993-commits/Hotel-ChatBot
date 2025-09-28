import streamlit as st

st.set_page_config(page_title="Hotel Booking Chatbot", page_icon="🏨")

# ---- Initialize Session State ----
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""

# ---- Hotel Options ----
hotel_options = {
    "Hawaii": [
        {
            "name": "Mauna Kea Beach Hotel, Autograph Collection",
            "rating": "4.6⭐ (1,563 reviews)",
            "desc": "Upscale, beachfront resort featuring airy rooms with balconies and sea views. Includes breakfast, accessibility, and luxury amenities.",
            "phone": "(808) 882-7222",
            "price": "$632 per night (inclusive of all taxes)"
        },
        {
            "name": "Hilton Hawaiian Village Waikiki Beach Resort",
            "rating": "4.2⭐ (25,213 reviews)",
            "desc": "Sprawling oceanfront resort on Waikiki Beach; rooms with sea view balconies. Non-smoking, breakfast included, wide range of amenities.",
            "phone": "(808) 949-4321",
            "price": "$714 per night (inclusive of all taxes)"
        },
        {
            "name": "Waikoloa Beach Marriott Resort & Spa",
            "rating": "4.4⭐ (3,743 reviews)",
            "desc": "Classy beachfront hotel with deluxe roo
