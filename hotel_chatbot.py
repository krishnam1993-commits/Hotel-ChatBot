import streamlit as st
from datetime import datetime, timedelta

# -----------------------------
# Reset function
# -----------------------------
def reset_chat():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state.step = 0

# -----------------------------
# Initialize session state
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""
if "selected_hotel" not in st.session_state:
    st.session_state.selected_hotel = None
if "activity_choice" not in st.session_state:
    st.session_state.activity_choice = ""
if "final_price" not in st.session_state:
    st.session_state.final_price = 0
if "checkin" not in st.session_state:
    st.session_state.checkin = None
if "checkout" not in st.session_state:
    st.session_state.checkout = None

# -----------------------------
# Data
# -----------------------------
preferences = {
    "Hawaii": "Deluxe room, balcony with sea view, non-smoking, breakfast included, accessibility near the beach.",
    "Vail": "Deluxe room, balcony with snow view, non-smoking, breakfast included, accessibility near the mountains.",
    "New York": "Deluxe room, balcony with city view, non-smoking, breakfast included, accessibility near the subway."
}

hotel_options = {
    "Hawaii": [
        {"name": "Mauna Kea Beach Hotel, Autograph Collection",
         "rating": "4.6⭐ (1,563 reviews)",
         "desc": "Upscale, beachfront resort featuring airy rooms, many with balconies and sea views.",
         "phone": "(808) 882-7222",
         "price": 632},
        {"name": "Hilton Hawaiian Village Waikiki Beach Resort",
         "rating": "4.2⭐ (25,213 reviews)",
         "desc": "Sprawling oceanfront resort on Waikiki Beach; high-rise rooms with sea-view balconies.",
         "phone": "(808) 949-4321",
         "price": 714},
    ],
    "Vail": [
        {"name": "The Arrabelle at Vail Square",
         "rating": "4.6⭐ (697 reviews)",
         "desc": "Elegant hotel with mountain-view rooms, rooftop pool, fine dining, cozy lounge.",
         "phone": "(888) 688-8055",
         "price": 399},
        {"name": "The Ritz-Carlton Club, Vail",
         "rating": "4.7⭐ (377 reviews)",
         "desc": "Sophisticated villas with mountain/snow views; premium service, outdoor pool.",
         "phone": "(970) 477-3700",
         "price": 1799},
    ],
    "New York": [
        {"name": "Hotel Mulberry",
         "rating": "4.3⭐ (439 reviews)",
         "desc": "Contemporary rooms with terraces, free breakfast & Wi-Fi. Chinatown, subway nearby.",
         "phone": "(212) 385-4633",
         "price": 499},
        {"name": "Hampton Inn Brooklyn/Downtown",
         "rating": "4.4⭐ (2,551 reviews)",
         "desc": "Suites with balconies, free hot breakfast, easy subway access, non-smoking.",
         "phone": "(718) 875-8800",
         "price": 399},
    ]
}

activities = {
    "Hawaii": [
        "Sailing with private Yacht (11AM-6:30PM, sunset & whale watching)",
        "Scuba diving (2 dives with instructor)",
        "Beach day & The Beach Bar Club night party",
        "Jet Skiing"
    ],
    "Vail": [
        "4 hr Skiing activity with lunch",
        "Snowshoeing at Lost Lake Trail",
        "Bonfire night party at the hotel",
        "Leisure Day"
    ],
    "New York": [
        "Concert Day",
        "Guided city tour (Statue of Liberty, Empire State Building, Madison Square)",
        "Lunch at Bungalow (Michelin Star restaurant)",
        "Leisure Day"
    ]
}

# -----------------------------
# Helper function
# -----------------------------
def get_activity_dates(checkin_str, acts):
    try:
        start = datetime.strptime(checkin_str, "%Y-%m-%d")
        return [f"{(start + timedelta(days=i)).strftime('%d %b')} - {acts[i]}" for i in range(len(acts))]
    except:
        return acts

# -----------------------------
# UI
# -----------------------------
st.title("🏨 Hotel Booking Assistant")

# 🔄 Restart always available
if st.button("🔄 Restart Chat"):
    reset_chat()

# Step 0: Greet
if st.session_state.step == 0:
    st.write("👋 Hello! Welcome to our Hotel Booking Assistant.")
    if st.button("Start Chat"):
        st.session_state.step = 1

# Step 1: Ask name
elif st.session_state.step == 1:
    st.write("May I know your name?")
    name = st.text_input("Enter your name", value=st.session_state.name)
    if st.button("Submit Name"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.step = 2

# Step 2: Destination
elif st.session_state.step == 2:
    st.write(f"Nice to meet you, **{st.session_state.name}**! 🌟 Where would you like to go?")
    dest = st.radio("Choose your destination:", ["Hawaii (Beach)", "Vail, Colorado (Skiing)", "New York City (Music Concerts)"])
    if st.button("Confirm Destination"):
        if "Hawaii" in dest:
            st.session_state.destination = "Hawaii"
        elif "Vail" in dest:
            st.session_state.destination = "Vail"
        else:
            st.session_state.destination = "New York"
        st.session_state.step = 21  # → new step for checkin/checkout

# Step 21: Checkin & Checkout
elif st.session_state.step == 21:
    st.write("📅 Please select your stay dates:")
    checkin = st.date_input("Check-in Date")
    checkout = st.date_input("Check-out Date")
    if st.button("Confirm Dates"):
        if checkin and checkout and checkin < checkout:
            st.session_state.checkin = str(checkin)
            st.session_state.checkout = str(checkout)
            st.session_state.step = 3
        else:
            st.error("⚠️ Please select valid check-in and check-out dates.")

# Step 3: Preferences
elif st.session_state.step == 3:
    dest = st.session_state.destination
    st.write(f"Based on your previous stay preferences for **{dest}**, we are considering:")
    st.info(preferences[dest])
    if st.button("Go for Hotel Options"):
        st.session_state.step = 4

# Step 4: Hotels
elif st.session_state.step == 4:
    dest = st.session_state.destination
    st.write(f"Here are some hotel options in **{dest}**:")
    for idx, hotel in enumerate(hotel_options[dest], 1):
        if st.button(f"🏨 Option {idx}: {hotel['name']}"):
            st.session_state.selected_hotel = hotel
            st.session_state.step = 5
    if st.session_state.selected_hotel:
        h = st.session_state.selected_hotel
        st.markdown(f"""
        ### {h['name']}
        ⭐ {h['rating']}  
        📝 {h['desc']}  
        📞 {h['phone']}  
        💲 {h['price']} per night
        """)

# Step 5: Activities option
elif st.session_state.step == 5:
    hotel = st.session_state.selected_hotel
    st.success(f"You selected **{hotel['name']}** (${hotel['price']} per night).")
    choice = st.radio("Would you like to see suggestions for activities?", ["Show suggestions", "Skip suggestion"])
    if st.button("Confirm Activity Choice"):
        st.session_state.activity_choice = choice
        if choice == "Show suggestions":
            st.session_state.step = 6
        else:
            st.session_state.step = 8

# Step 6: Show activities
elif st.session_state.step == 6:
    dest = st.session_state.destination
    acts = get_activity_dates(st.session_state.checkin, activities[dest])
    st.write("Here are some suggested activities for your trip:")
    for act in acts:
        st.markdown(f"- {act}")
    if st.button("Proceed with Activities"):
        st.session_state.step = 8

# Step 8: Price summary
elif st.session_state.step == 8:
    hotel = st.session_state.selected_hotel
    checkin = datetime.strptime(st.session_state.checkin, "%Y-%m-%d")
    checkout = datetime.strptime(st.session_state.checkout, "%Y-%m-%d")
    nights = (checkout - checkin).days
    base = hotel["price"] * nights
    if st.session_state.activity_choice == "Show suggestions":
        total = base + 2500
        st.session_state.final_price = total
        st.write(f"🏨 Hotel ({nights} nights): ${base}")
        st.write("🎉 Activities Package: $2500")
        st.success(f"💰 Total Price: ${total}")
    else:
        total = base
        st.session_state.final_price = total
        st.success(f"💰 Total Price for {nights} nights: ${total}")
    proceed = st.radio("Proceed to payment?", ["Yes", "No"])
    if proceed == "Yes":
        st.session_state.step = 9

# Step 9: Payment
elif st.session_state.step == 9:
    st.info("💳 A payment link has been sent via SMS to your mobile number. Please pay within 10 minutes to confirm booking.")
    if st.button("Yay!!!"):
        st.session_state.step = 10



























































# Step 11: Price summary - SAFELY access selected_hotel
elif st.session_state.step == 9:
    # ensure selected_hotel exists (recover from index if possible)
    if not st.session_state.selected_hotel:
        idx = st.session_state.selected_hotel_index
        dest = st.session_state.destination
        if idx is not None and dest and dest in hotel_options:
            try:
                st.session_state.selected_hotel = hotel_options[dest][idx]
            except Exception:
                st.warning("Selected hotel not found. Please re-select a hotel.")
                if st.button("Go back to hotel options"):
                    st.session_state.step = 4
                st.stop()
        else:
            st.warning("No hotel selected. Please select a hotel first.")
            if st.button("Go to hotel options"):
                st.session_state.step = 4
            st.stop()

    base = st.session_state.selected_hotel.get("price", 0)
    st.session_state.total_price = base
    if st.session_state.activities_confirmed:
        st.session_state.total_price = base + st.session_state.activity_price

    st.write("### Price Summary")
    st.write(f"Hotel stay: ${base} per night")
    if st.session_state.activities_confirmed:
        st.write("Activities: $2500")
    else:
        st.write("Activities: Skipped")
    st.write(f"**Total: ${st.session_state.total_price}**")

    proceed_radio = st.radio("Do you want to proceed with the payment?", ("Proceed to Payment", "Cancel"))
    if st.button("Confirm Payment Option"):
        if proceed_radio == "Proceed to Payment":
            st.session_state.payment_proceed = True
            st.session_state.step = 10
        else:
            st.info("You chose not to proceed with payment right now. You can Restart Chat or go back.")
            if st.button("Restart Chat"):
                reset_chat()

# Step 13: On proceed, display payment link message
elif st.session_state.step == 10:
    st.write("A payment link has been sent via sms to your mobile number. Please make the payment in 10 minutes and proceed with the booking")
    st.write("Thanks for booking with us. We are excited to host you for a wonderful stay experience")
    if st.button("Yay!!!"):
        st.session_state.step = 15
    else:
        st.info("Click 'Yay!!!' when you have completed payment to continue.")

# Step 15: Welcome and pre-arrival reminders
elif st.session_state.step == 15:
    st.write(f"Hi, Welcome {st.session_state.name}")
    hotel_name = st.session_state.selected_hotel["name"] if st.session_state.selected_hotel else ""
    st.write(f"We are excited to host you for your upcoming stay with us at {hotel_name}")
    st.write("Before you arrive, we just want to remind you to keep the following documents handy with you for smooth experience")
    st.markdown("- a) Identity card\n- b) Health issues related documents\n- c) Travel insurance\n- d) Booking confirmation receipt")
    st.write("We would ask you to spend a minute with us to personalize your experience during the stay.")
    if st.button("Okay"):
        st.session_state.step = 18

# Step 18: Personalization inputs (allergy, gym time)
elif st.session_state.step == 18:
    allergy_input = st.text_input("i) Please describe food allergy, if any. Type 'NA' in case of no allergy.", value=st.session_state.allergy)
    if st.button("Submit Allergy"):
        st.session_state.allergy = allergy_input.strip() if allergy_input else "NA"
        st.success("Thanks for your confirmation")
    gym_input = st.text_input("ii) Please confirm if you want to use gym during your stay in 24 hr time format (or type 'NA')", value=st.session_state.gym_time)
    if st.button("Submit Gym Time"):
        st.session_state.gym_time = gym_input.strip() if gym_input else "NA"
        st.success("Thanks for your confirmation")
    if st.button("Proceed Further"):
        st.session_state.step = 19

# Step 19: In-stay options (guest has checked-in)
elif st.session_state.step == 19:
    st.write(f"Hi {st.session_state.name}, We hope you are having a wonderful experience during your stay. As you have checked-in today, please select from below options")
    service_choice = st.selectbox("Select a service", ("Wake Up Call at 7AM", "Laundry", "Call cab", "Schedule breakfast in room"))
    if st.button("Confirm Service Request"):
        st.session_state.instay_service = service_choice
        st.session_state.step = 20

# Step 20: Service confirmation
elif st.session_state.step == 20:
    st.write(f"Thanks for the confirmation. We will {st.session_state.instay_service}")
    if st.button("Continue"):
        st.session_state.step = 21

# Step 21: Farewell message and feedback request
elif st.session_state.step == 21:
    hotel_name = st.session_state.selected_hotel["name"] if st.session_state.selected_hotel else ""
    st.write(f"Hi {st.session_state.name}, Thanks for choosing {hotel_name} for your stay. Hope you had a wonderful time staying with us. We would love to your back from you on your experience")
    if st.button("Provide Feedback / Finish"):
        st.session_state.step = 22

# Step 22: Loyalty offer message
elif st.session_state.step == 22:
    st.write("As you have been an esteemed member of [HotelChainName], we are happy to share 2 night & 3 day weekend space at any of our property at flat 50% discount. You can avail this offer in 365 days from you. Just login to our website with your registered email id to claim the offer.")
    st.success("Thank you! End of flow.")
    if st.button("Restart Chat"):
        reset_chat()
