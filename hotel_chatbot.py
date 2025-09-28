import streamlit as st
from datetime import datetime, timedelta

# -----------------------------
# Reset function
# -----------------------------
def reset_chat():
    for key in list(st.session_state.keys()):
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
if "checkin" not in st.session_state:
    st.session_state.checkin = None
if "checkout" not in st.session_state:
    st.session_state.checkout = None
if "selected_hotel" not in st.session_state:
    st.session_state.selected_hotel = None
if "activity_choice" not in st.session_state:
    st.session_state.activity_choice = ""
if "final_price" not in st.session_state:
    st.session_state.final_price = 0
if "allergy" not in st.session_state:
    st.session_state.allergy = ""
if "gym_use" not in st.session_state:
    st.session_state.gym_use = ""
if "wake_up_call" not in st.session_state:
    st.session_state.wake_up_call = False
if "laundry_request" not in st.session_state:
    st.session_state.laundry_request = False
if "cab_request" not in st.session_state:
    st.session_state.cab_request = False
if "breakfast_request" not in st.session_state:
    st.session_state.breakfast_request = False

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
        {
            "name": "Mauna Kea Beach Hotel, Autograph Collection",
            "rating": "4.6⭐ (1,563 reviews)",
            "desc": "Upscale, beachfront resort featuring airy rooms, many with balconies and sea views.",
            "phone": "(808) 882-7222",
            "price": 632,
        },
        {
            "name": "Hilton Hawaiian Village Waikiki Beach Resort",
            "rating": "4.2⭐ (25,213 reviews)",
            "desc": "Sprawling oceanfront resort on Waikiki Beach; high-rise rooms with sea view balconies.",
            "phone": "(808) 949-4321",
            "price": 714,
        },
        {
            "name": "Waikoloa Beach Marriott Resort & Spa",
            "rating": "4.4⭐ (3,743 reviews)",
            "desc": "Classy beachfront hotel with modern deluxe rooms, breakfast included, close to surf.",
            "phone": "(808) 886-6789",
            "price": 578,
        },
        {
            "name": "Castle Kona Bali Kai",
            "rating": "4.0⭐ (485 reviews)",
            "desc": "Oceanfront condos featuring lanais (balconies), some with sea views, pool & breakfast.",
            "phone": "(808) 329-9381",
            "price": 540,
        },
    ],
    "Vail": [
        {
            "name": "The Arrabelle at Vail Square",
            "rating": "4.6⭐ (697 reviews)",
            "desc": "Elegant hotel with mountain views, rooftop pool, fine dining, central Vail location.",
            "phone": "(888) 688-8055",
            "price": 399,
        },
        {
            "name": "The Ritz-Carlton Club, Vail",
            "rating": "4.7⭐ (377 reviews)",
            "desc": "Sophisticated villas with balconies, snow views, premium service near ski lifts.",
            "phone": "(970) 477-3700",
            "price": 1799,
        },
        {
            "name": "Highline Vail - a DoubleTree by Hilton",
            "rating": "4.2⭐ (944 reviews)",
            "desc": "Refined rooms & suites, mountain views, breakfast option, free shuttle to lifts.",
            "phone": "(970) 476-2739",
            "price": 662,
        },
        {
            "name": "Vail's Mountain Haus",
            "rating": "4.4⭐ (252 reviews)",
            "desc": "Polished resort, free breakfast, outdoor pool, hot tubs, walking distance to lifts.",
            "phone": "(970) 476-2434",
            "price": 662,
        },
    ],
    "New York": [
        {
            "name": "Hotel Mulberry",
            "rating": "4.3⭐ (439 reviews)",
            "desc": "Contemporary rooms with terraces/city views, free breakfast, near subways.",
            "phone": "(212) 385-4633",
            "price": 499,
        },
        {
            "name": "Hampton Inn Brooklyn/Downtown",
            "rating": "4.4⭐ (2,551 reviews)",
            "desc": "Modern suites, free breakfast, easy subway access at Jay St-MetroTech.",
            "phone": "(718) 875-8800",
            "price": 399,
        },
        {
            "name": "The Washington Hotel NYC",
            "rating": "3.8⭐ (2,057 reviews)",
            "desc": "Premium hotel with terraces, breakfast available, close to Wall St & Rector St.",
            "phone": "(646) 826-8600",
            "price": 399,
        },
        {
            "name": "Madison LES Hotel",
            "rating": "4.0⭐ (819 reviews)",
            "desc": "Informal hotel, free breakfast buffet, rooftop terrace, near East Broadway subway.",
            "phone": "(212) 390-1533",
            "price": 399,
        },
    ]
}



activities = {
    "Hawaii": ["Sailing", "Scuba diving", "Beach & Night party", "Jet Skiing"],
    "Vail": ["Skiing", "Snowshoeing", "Bonfire", "Leisure Day"],
    "New York": ["Concert", "City tour", "Lunch at Michelin Star", "Leisure Day"]
}

# -----------------------------
# Helper
# -----------------------------
def get_activity_dates(checkin_str, acts):
    try:
        start = datetime.strptime(checkin_str, "%Y-%m-%d")
        return [f"{(start + timedelta(days=i)).strftime('%d %b')} - {acts[i]}" for i in range(len(acts))]
    except:
        return acts

# -----------------------------
# UI Flow
# -----------------------------
st.title("🏨 Hotel Booking Assistant")
if st.button("🔄 Restart Chat"):
    reset_chat()
    st.rerun()

# Step 0: Greet
if st.session_state.step == 0:
    st.write("👋 Hello! Welcome to our Hotel Booking Assistant.")
    if st.button("Start Chat"):
        st.session_state.step = 1
        st.rerun()

# Step 1: Ask Name
elif st.session_state.step == 1:
    name = st.text_input("May I know your name?")
    if st.button("Submit Name"):
        if name.strip():
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()

# Step 2: Destination
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
        st.rerun()

# Step 3: Check-in/out
elif st.session_state.step == 3:
    st.write("📅 Please select your stay dates:")
    checkin = st.date_input("Check-in Date")
    checkout = st.date_input("Check-out Date")
    if st.button("Confirm Dates"):
        if checkin and checkout and checkin < checkout:
            st.session_state.checkin = str(checkin)
            st.session_state.checkout = str(checkout)
            st.session_state.step = 4
            st.rerun()
        else:
            st.error("⚠️ Invalid dates")

# Step 4: Preferences
elif st.session_state.step == 4:
    dest = st.session_state.destination
    st.info(preferences[dest])
    if st.button("Go for Hotel Options"):
        st.session_state.step = 5
        st.rerun()

# Step 5: Hotels
elif st.session_state.step == 5:
    dest = st.session_state.destination
    for idx, h in enumerate(hotel_options[dest], 1):
        if st.button(f"🏨 {h['name']}"):
            st.session_state.selected_hotel = h
            st.session_state.step = 6
            st.rerun()

# Step 6: Activity Option
elif st.session_state.step == 6:
    hotel = st.session_state.selected_hotel
    st.success(f"You selected {hotel['name']} (${hotel['price']}/night)")
    choice = st.radio("Would you like to see activity suggestions?", ["Show", "Skip"])
    if st.button("Confirm Choice"):
        st.session_state.activity_choice = choice
        st.session_state.step = 7 if choice == "Show" else 8
        st.rerun()

# Step 7: Show Activities
elif st.session_state.step == 7:
    acts = get_activity_dates(st.session_state.checkin, activities[st.session_state.destination])
    for a in acts: st.write(f"- {a}")
    if st.button("Proceed with Activities"):
        st.session_state.step = 8
        st.rerun()

# Step 8: Price Summary
elif st.session_state.step == 8:
    hotel = st.session_state.selected_hotel
    nights = (datetime.strptime(st.session_state.checkout, "%Y-%m-%d") - datetime.strptime(st.session_state.checkin, "%Y-%m-%d")).days
    base = hotel["price"] * nights
    total = base + (2500 if st.session_state.activity_choice == "Show" else 0)
    st.session_state.final_price = total
    st.write(f"🏨 Hotel ({nights} nights): ${base}")
    if st.session_state.activity_choice == "Show":
        st.write("🎉 Activities Package: $2500")
    st.success(f"💰 Total: ${total}")
    if st.button("Proceed to Payment"):
        st.session_state.step = 9
        st.rerun()

# Step 9: Payment
elif st.session_state.step == 9:
    st.info("💳 A payment link has been sent to your mobile. Pay within 10 minutes.")
    if st.button("Yay!!!"):
        st.session_state.step = 10
        st.rerun()

# Step 10: Pre-arrival Docs
elif st.session_state.step == 10:
    st.write(f"Hi {st.session_state.name}, before you arrive keep ready:")
    st.markdown("- ID Card\n- Health documents\n- Travel insurance\n- Booking receipt")
    if st.button("Okay"):
        st.session_state.step = 18
        st.rerun()

# Step 18: Personalization
elif st.session_state.step == 18:
    allergy = st.text_input("Food allergy? Type 'NA' if none:", value=st.session_state.allergy)
    gym = st.text_input("Gym time (24hr format)?", value=st.session_state.gym_use)
    if st.button("Proceed"):
        st.session_state.allergy = allergy
        st.session_state.gym_use = gym
        st.session_state.step = 19
        st.rerun()

# Step 19: In-stay services
elif st.session_state.step == 19:
    options = ["Wake Up Call at 7AM", "Laundry", "Call cab", "Schedule breakfast in room"]
    selected = st.multiselect("Select services:", options)
    if st.button("Confirm Services"):
        st.session_state.wake_up_call = "Wake Up Call at 7AM" in selected
        st.session_state.laundry_request = "Laundry" in selected
        st.session_state.cab_request = "Call cab" in selected
        st.session_state.breakfast_request = "Schedule breakfast in room" in selected
        st.session_state.step = 20
        st.rerun()

# Step 20: Service confirmation
elif st.session_state.step == 20:
    hname = st.session_state.selected_hotel["name"] if st.session_state.selected_hotel else "your hotel"
    st.write(f"Hi {st.session_state.name}, thanks for choosing {hname}.")
    st.write("Services confirmed:")
    if st.session_state.wake_up_call: st.write("✅ Wake Up Call")
    if st.session_state.laundry_request: st.write("✅ Laundry")
    if st.session_state.cab_request: st.write("✅ Cab")
    if st.session_state.breakfast_request: st.write("✅ Breakfast in room")
    if st.button("Proceed Further"):
        st.session_state.step = 21
        st.rerun()

# Step 21: Feedback
elif st.session_state.step == 21:
    hname = st.session_state.selected_hotel["name"] if st.session_state.selected_hotel else "your hotel"
    st.write(f"Hi {st.session_state.name}, thanks for staying at {hname}. Hope you had a great time!")
    if st.button("Provide Feedback / Proceed"):
        st.session_state.step = 22
        st.rerun()

# Step 22: Loyalty offer
elif st.session_state.step == 22:
    st.write("🎉 As an esteemed member, you get 2 nights & 3 days at 50% off at any property within 365 days.")
    if st.button("Finish"):
        st.success("Thank you! We hope to see you again soon.")
        st.session_state.step = 23
