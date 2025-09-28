import streamlit as st

st.set_page_config(page_title="Hotel Booking Chatbot", page_icon="🏨")

# ---------------- INIT SESSION ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""
if "hotel" not in st.session_state:
    st.session_state.hotel = {}
if "activity_choice" not in st.session_state:
    st.session_state.activity_choice = "Skip"
if "activity_price" not in st.session_state:
    st.session_state.activity_price = 0
if "price" not in st.session_state:
    st.session_state.price = 0
if "selected_option" not in st.session_state:
    st.session_state.selected_option = ""

# ---------------- HOTEL DATA ----------------
hotel_options = {
    "Hawaii": [
        {"name": "Mauna Kea Beach Hotel, Autograph Collection",
         "rating": "4.6⭐ (1,563 reviews)",
         "desc": "Upscale, beachfront resort featuring airy rooms, many with balconies and sea views.",
         "phone": "(808) 882-7222", "price": 632},
        {"name": "Hilton Hawaiian Village Waikiki Beach Resort",
         "rating": "4.2⭐ (25,213 reviews)",
         "desc": "Sprawling oceanfront resort on Waikiki Beach; high-rise rooms with sea view balconies available.",
         "phone": "(808) 949-4321", "price": 714},
        {"name": "Waikoloa Beach Marriott Resort & Spa",
         "rating": "4.4⭐ (3,743 reviews)",
         "desc": "Classy beachfront hotel with deluxe rooms and suites, often with sea-view balconies.",
         "phone": "(808) 886-6789", "price": 578},
        {"name": "Castle Kona Bali Kai",
         "rating": "4⭐ (485 reviews)",
         "desc": "Oceanfront condos featuring lanais, select units with sea views, breakfast offered.",
         "phone": "(808) 329-9381", "price": 540}
    ],
    "Vail": [
        {"name": "The Arrabelle at Vail Square",
         "rating": "4.6⭐ (697 reviews)",
         "desc": "Elegant hotel with mountain views, rooftop pool, and cozy lounge.",
         "phone": "(888) 688-8055", "price": 399},
        {"name": "The Ritz-Carlton Club, Vail",
         "rating": "4.7⭐ (377 reviews)",
         "desc": "Sophisticated villas with snow views, premium service, and outdoor pool.",
         "phone": "(970) 477-3700", "price": 1799},
        {"name": "Highline Vail - a DoubleTree by Hilton",
         "rating": "4.2⭐ (944 reviews)",
         "desc": "Refined rooms, some with mountain views, onsite dining, breakfast option.",
         "phone": "(970) 476-2739", "price": 662},
        {"name": "Vail's Mountain Haus",
         "rating": "4.4⭐ (252 reviews)",
         "desc": "Polished resort with free breakfast, pool, hot tubs, balcony mountain views.",
         "phone": "(970) 476-2434", "price": 662}
    ],
    "New York": [
        {"name": "Hotel Mulberry",
         "rating": "4.3⭐ (439 reviews)",
         "desc": "Contemporary rooms with city views, free breakfast & WiFi.",
         "phone": "(212) 385-4633", "price": 499},
        {"name": "Hampton Inn Brooklyn/Downtown",
         "rating": "4.4⭐ (2,551 reviews)",
         "desc": "Hotel with suites, balconies, free breakfast, easy subway access.",
         "phone": "(718) 875-8800", "price": 399},
        {"name": "The Washington Hotel NYC",
         "rating": "3.8⭐ (2,057 reviews)",
         "desc": "Premium hotel with terraces, city views, convenient subway access.",
         "phone": "(646) 826-8600", "price": 399},
        {"name": "Madison LES Hotel",
         "rating": "4⭐ (819 reviews)",
         "desc": "Informal hotel with free breakfast, rooftop terrace, close to subway.",
         "phone": "(212) 390-1533", "price": 399}
    ]
}

preferences = {
    "Hawaii": "Deluxe room, balcony with sea view, non-smoking, breakfast included, near beach.",
    "Vail": "Deluxe room, balcony with snow view, non-smoking, breakfast included, near mountains.",
    "New York": "Deluxe room, balcony with city view, non-smoking, breakfast included, near subway."
}

activities = {
    "Hawaii": [
        "6th Dec - Sailing with private Yacht (11AM–6:30PM, sunset sailing, whale watching)",
        "7th Dec - Scuba diving with 2 dives + instructor session",
        "8th Dec - Beach day + The Beach Bar Club party at night",
        "9th Dec - Jet Skiing"
    ],
    "Vail": [
        "6th Dec - 4 hr Skiing activity with lunch",
        "7th Dec - Snowshoeing at Lost Lake Trail",
        "8th Dec - Bonfire night party at the hotel",
        "9th Dec - Leisure Day"
    ],
    "New York": [
        "6th Dec - Concert Day",
        "7th Dec - Guided city tour (Statue of Liberty, Empire State, etc.)",
        "8th Dec - Lunch at Bungalow (Michelin Star)",
        "9th Dec - Leisure Day"
    ]
}

# ---------------- CHAT FLOW ----------------
st.title("🏨 Hotel Booking Assistant")

# 1. Greeting
if st.session_state.step == 0:
    st.write("👋 Hello! Welcome to our Hotel Booking Assistant.")
    if st.button("Start Chat"):
        st.session_state.step = 1

# 2. Ask Guest Name
elif st.session_state.step == 1:
    name = st.text_input("May I know your name?", value=st.session_state.name)
    if st.button("Submit Name"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.step = 2

# 3. Ask Destination
elif st.session_state.step == 2:
    dest = st.radio("Where would you like to go?", ["Hawaii (Beach)", "Vail, Colorado (Skiing)", "New York City (Music Concerts)"])
    if st.button("Confirm Destination"):
        if "Hawaii" in dest:
            st.session_state.destination = "Hawaii"
        elif "Vail" in dest:
            st.session_state.destination = "Vail"
        else:
            st.session_state.destination = "New York"
        st.session_state.step = 3

# 4. Show Preferences
elif st.session_state.step == 3:
    dest = st.session_state.destination
    st.write(f"Based on your stay preferences for **{dest}**, we recommend:")
    st.info(preferences[dest])
    if st.button("Go for Hotel Options"):
        st.session_state.step = 4

# 5-7. Show Hotels
elif st.session_state.step == 4:
    dest = st.session_state.destination
    st.write(f"Here are hotel options in **{dest}**:")
    for i, h in enumerate(hotel_options[dest], start=1):
        st.markdown(f"**Option {i}: {h['name']}**  \n{h['rating']}  \n{h['desc']}  \n📞 {h['phone']}  \n💰 ${h['price']} per night (all taxes included)")
        st.divider()
    choice = st.number_input("Enter the option number of the hotel you want to book:", min_value=1, max_value=4, step=1)
    if st.button("Confirm Hotel"):
        st.session_state.hotel = hotel_options[dest][choice - 1]
        st.session_state.price = st.session_state.hotel["price"]
        st.session_state.step = 5

# 8. Activities Option
elif st.session_state.step == 5:
    choice = st.radio("Would you like to book other activities?", ["Show suggestions", "Skip suggestion"])
    if st.button("Confirm Choice"):
        st.session_state.activity_choice = choice
        if choice == "Show suggestions":
            st.session_state.step = 6
        else:
            st.session_state.step = 9

# 9. Show Suggestions
elif st.session_state.step == 6:
    dest = st.session_state.destination
    st.write("Here are activity suggestions for your trip:")
    for act in activities[dest]:
        st.markdown(f"- {act}")
    if st.button("Proceed with these activities"):
        st.session_state.activity_price = 2500
        st.session_state.step = 9

# 11. Price Summary
elif st.session_state.step == 9:
    total = st.session_state.price
    if st.session_state.activity_choice == "Show suggestions":
        total += st.session_state.activity_price
        st.write("### Price Summary")
        st.write(f"Hotel: ${st.session_state.price} per night")
        st.write("Activities: $2500 (all inclusive)")
    else:
        st.write("### Price Summary")
        st.write(f"Hotel: ${st.session_state.price} per night")
    st.write(f"**Total: ${total}**")
    pay = st.radio("Would you like to proceed with the payment?", ["Yes", "No"])
    if st.button("Confirm Payment"):
        if pay == "Yes":
            st.session_state.step = 10

# 13-14. Payment and Confirmation
elif st.session_state.step == 10:
    st.success("A payment link has been sent via SMS. Please make the payment in 10 minutes.")
    if st.button("Yay!!!"):
        st.session_state.step = 11

# 15-17. Pre-arrival Info
elif st.session_state.step == 11:
    st.write(f"Hi, Welcome {st.session_state.name} 👋")
    st.write(f"We are excited to host you at **{st.session_state.hotel['name']}**.")
    st.write("Please keep the following documents handy:")
    st.markdown("- Identity card\n- Health related documents\n- Travel insurance\n- Booking confirmation receipt")
    if st.button("Okay"):
        st.session_state.step = 12

# 18. Personalization
elif st.session_state.step == 12:
    allergy = st.text_input("Please describe any food allergy (type 'NA' if none):")
    gym = st.text_input("Please confirm if you want to use the gym (enter time in 24hr format, or NA):")
    if st.button("Submit Preferences"):
        st.write("Thanks for your confirmation!")
        st.session_state.step = 13

# 19. In-stay options
elif st.session_state.step == 13:
    choice = st.radio("Please select a service:", ["Wake Up Call at 7AM", "Laundry", "Call cab", "Schedule breakfast in room"])
    if st.button("Confirm Service"):
        st.session_state.selected_option = choice
        st.session_state.step = 14

# 20. Service confirmation
elif st.session_state.step == 14:
    st.success(f"Thanks for the confirmation. We will {st.session_state.selected_option}.")
    if st.button("Continue"):
        st.session_state.step = 15

# 21-22. Farewell + Offer
elif st.session_state.step == 15:
    st.write(f"Hi {st.session_state.name}, Thanks for choosing {st.session_state.hotel['name']} for your stay. Hope you had a wonderful time!")
    st.write("We would love to hear back from you on your experience.")
    st.info("As an esteemed member of our Hotel Chain, enjoy **2 nights & 3 days weekend stay at 50% discount** at any property within the next 365 days. Login with your registered email to claim this offer.")
    st.success("🎉 End of Chatbot Journey")
    if st.button("Restart Chat"):
        st.session_state.clear()
        st.session_state.step = 0
