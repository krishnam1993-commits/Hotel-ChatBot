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
            "desc": "Classy beachfront hotel with deluxe rooms and suites. Includes breakfast, sea-view balconies, and easy beach access.",
            "phone": "(808) 886-6789",
            "price": "$578 per night (inclusive of all taxes)"
        },
        {
            "name": "Castle Kona Bali Kai",
            "rating": "4⭐ (485 reviews)",
            "desc": "Oceanfront condos with balconies, non-smoking rooms, breakfast, and pool. Beachfront location.",
            "phone": "(808) 329-9381",
            "price": "$540 per night (inclusive of all taxes)"
        }
    ],
    "Vail": [
        {
            "name": "The Arrabelle at Vail Square",
            "rating": "4.6⭐ (697 reviews)",
            "desc": "Elegant hotel with mountain-view balconies, rooftop pool, and fine dining. Central Vail, near ski lifts.",
            "phone": "(888) 688-8055",
            "price": "$399 per night (inclusive of all taxes)"
        },
        {
            "name": "The Ritz-Carlton Club, Vail",
            "rating": "4.7⭐ (377 reviews)",
            "desc": "Luxury villas with snow-view balconies, outdoor pool, premium service. Near ski lifts and mountain activities.",
            "phone": "(970) 477-3700",
            "price": "$1799 per night (inclusive of all taxes)"
        },
        {
            "name": "Highline Vail - a DoubleTree by Hilton",
            "rating": "4.2⭐ (944 reviews)",
            "desc": "Refined rooms, balcony with mountain views. Onsite dining, breakfast, free shuttle.",
            "phone": "(970) 476-2739",
            "price": "$662 per night (inclusive of all taxes)"
        },
        {
            "name": "Vail's Mountain Haus",
            "rating": "4.4⭐ (252 reviews)",
            "desc": "Resort with breakfast, Wi-Fi, pool, hot tubs. Deluxe rooms with mountain/snow views, near ski lifts.",
            "phone": "(970) 476-2434",
            "price": "$662 per night (inclusive of all taxes)"
        }
    ],
    "New York": [
        {
            "name": "The Standard, High Line",
            "rating": "4.4⭐ (5,321 reviews)",
            "desc": "Trendy hotel with city-view balconies, br
