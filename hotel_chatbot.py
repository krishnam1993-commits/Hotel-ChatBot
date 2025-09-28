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
            "desc": "Upscale beachfront resort with airy rooms, balconies, and sea views.",
            "phone": "(808) 882-7222",
            "price": "$632 per night (all taxes included)"
        },
        {
            "name": "Hilton Hawaiian Village Waikiki Beach Resort",
            "rating": "4.2⭐ (25,213 reviews)",
            "desc": "Large oceanfront resort with sea-view rooms and breakfast options.",
            "phone": "(808) 949-4321",
            "price": "$714 per night (all taxes included)"
        },
        {
            "name": "Waikoloa Beach Marriott Resort & Spa",
            "rating": "4.4⭐ (3,743 reviews)",
            "desc": "Modern beachfront hotel with deluxe rooms and easy beach access.",
            "phone": "(808) 886-6789",
            "price": "$578 per night (all taxes included)"
        },
        {
            "name": "Castle Kona Bali Kai",
            "rating": "4⭐ (485 reviews)",
            "desc": "Oceanfront condos with balconies, pool, and breakfast available.",
            "phone": "(808) 329-9381",
            "price": "$540 per night (all taxes included)"
        }
    ],
    "Vail": [
        {
            "name": "The Arrabelle at Vail Square",
            "rating": "4.6⭐ (697 reviews)",
            "desc": "Elegant hotel with mountain views, rooftop pool, and fine dining.",
            "phone": "(888) 688-8055",
            "price": "$399 per night (all taxes included)"
        },
        {
            "name": "The Ritz-Carlton Club, Vail",
            "rating": "4.7⭐ (377 reviews)",
            "desc": "Luxury villas with snow views, outdoor pool, and premium service.",
            "phone": "(970) 477-3700",
            "price": "$1799 per night (all taxes included)"
        },
        {
            "name": "Highline Vail - a DoubleTree by Hilton",
            "rating": "4.2⭐ (944 reviews)",
            "desc": "Refined rooms with mountain views, onsite dining, and free shuttle.",
            "phone": "(970) 476-2739",
            "price": "$662 per night (all taxes included)"
        },
        {
            "name": "Vail's Mountain Haus",
            "rating": "4.4⭐ (252 reviews)",
            "desc": "Resort with breakfast, Wi-Fi, pool, and hot tubs.",
            "phone": "(970) 476-2434",
            "price": "$662 per night (all taxes included)"
        }
    ],
    "New York": [
        {
            "name": "The Standard, High Line",
            "rating": "4.4⭐ (5,321 reviews)",
            "desc": "Trendy hotel with city views and close to music venues.",
            "phone": "(212) 645-4646",
            "price": "$550 per night (all taxes included)"
        },
        {
            "name": "The Plaza Hotel",
            "rating": "4.6⭐ (8,743 reviews)",
            "desc": "Iconic luxury hotel with central location and fine dining.",
            "phone": "(212) 759-3000",
            "price": "$899 per night (all taxes included)"
        },
        {
            "name": "CitizenM New York Times Square",
            "rating": "4.5⭐ (2,198 reviews)",
            "desc": "Modern boutique hotel with non-smoking rooms and breakfast.",
            "phone": "(212) 461-3638",
            "price": "$420 per night (all taxes included)"
        },
        {
            "name": "Arlo Midtown",
            "rating": "4.3⭐ (3,045 reviews)",
            "desc": "Stylish hotel with subway access and breakfast available.",
            "phone": "(212) 343-7000",
            "price": "$380 per night (all taxes included)"
        }
    ]
}

# ---- Preferences ----
preferences = {
    "Hawaii": "Deluxe room, balcony with sea view, non-smoking, breakfast included, accessibility near the beach.",
    "Vail": "Deluxe room, balcony with snow view, non-smoking, breakfast included, accessibility near the mountains.",
    "New York": "Deluxe room, balcony with city view, non-smoking, breakfast included, accessibility near the subway."
}

# ---- Chatbot Flow ----
st.title("🏨 Hotel Booking Assistant"
