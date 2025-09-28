import streamlit as st

st.set_page_config(page_title="Hotel Concierge Bot", page_icon="🏨", layout="centered")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "guest_name" not in st.session_state:
    st.session_state.guest_name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""
if "hotel" not in st.session_state:
    st.session_state.hotel = ""
if "activities" not in st.session_state:
    st.session_state.activities = False
if "allergies" not in st.session_state:
    st.session_state.allergies = ""
if "gym_time" not in st.session_state:
    st.session_state.gym_time = ""
if "service" not in st.session_state:
    st.session_state.service = ""

# Hotel options
hotel_data = {
    "Hawaii": [
        ("Mauna Kea Beach Hotel, Autograph Collection", 632),
        ("Hilton Hawaiian Village Waikiki Beach Resort", 714),
        ("Waikoloa Beach Marriott Resort & Spa", 578),
        ("Castle Kona Bali Kai", 540)
    ],
    "Vail": [
        ("The Arrabelle at Vail Square", 399),
        ("The Ritz-Carlton Club, Vail", 1799),
        ("Highline Vail - a DoubleTree by Hilton", 662),
        ("Vail's Mountain Haus", 662)
    ],
    "NYC": [
        ("Hotel Mulberry", 499),
        ("Hampton Inn Brooklyn/Downtown", 399),
        ("The Washington Hotel NYC", 399),
        ("Madison LES Hotel", 399)
    ]
}

# Activity bundles
activity_data = {
    "Hawaii": ["6 Dec - Private Yacht Sailing & Whale Watching", 
               "7 Dec - Scuba Diving (2 dives)", 
               "8 Dec - Beach Party at Beach Bar Club", 
               "9 Dec - Jet Skiing"],
    "Vail": ["6 Dec - Skiing with lunch", 
             "7 Dec - Snowshoeing at Lost Lake Trail", 
             "8 Dec - Bonfire Night", 
             "9 Dec - Leisure Day"],
    "NYC": ["6 Dec - Concert Day", 
            "7 Dec - Guided City Tour", 
            "8 Dec - Lunch at Michelin Star Bungalow", 
            "9 Dec - Leisure Day"]
}

# Steps flow
if st.session_state.step == 0:
    st.write("👋 Hi there! Welcome to our Hotel Concierge Bot.")
    if st.button("Start"):
        st.session_state.step = 1

elif st.session_state.step == 1:
    st.write("May I have your name please?")
    name = st.text_input("Enter your name")
    if st.button("Submit Name"):
        if name:
            st.session_state.guest_name = name
            st.session_state.step = 2

elif st.session_state.step == 2:
    st.write(f"Nice to meet you, **{st.session_state.guest_name}**! Where would you like to go?")
    choice = st.radio("Select destination", ["Hawaii (Beaches)", "Vail (Skiing)", "NYC (Concerts)"])
    if st.button("Confirm Destination"):
        if "Hawaii" in choice:
            st.session_state.destination = "Hawaii"
        elif "Vail" in choice:
            st.session_state.destination = "Vail"
        else:
            st.session_state.destination = "NYC"
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.write(f"Based on your previous stay preferences in **{st.session_state.destination}**, we suggest:")
    if st.session_state.destination == "Hawaii":
        st.markdown("- Deluxe room, balcony with sea view, no smoking room, breakfast included, near the beach 🌊")
    elif st.session_state.destination == "Vail":
        st.markdown("- Deluxe room, balcony with snow view, no smoking room, breakfast included, near the mountains ⛰️")
    else:
        st.markdown("- Deluxe room, balcony with city view, no smoking room, breakfast included, near the subway 🚇")
    if st.button("Go for Hotel Options"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.write(f"Here are some hotel options in **{st.session_state.destination}**:")
    options = hotel_data[st.session_state.destination]
    hotel_choice = st.radio("Choose your hotel", [f"{h} - ${p}/night" for h, p in options])
    if st.button("Confirm Hotel"):
        st.session_state.hotel = hotel_choice
        st.session_state.step = 5

elif st.session_state.step == 5:
    st.write("Would you like to explore activities?")
    act_choice = st.radio("Select", ["Show Suggestions", "Skip"])
    if st.button("Confirm Activity Choice"):
        if act_choice == "Show Suggestions":
            st.session_state.activities = True
        st.session_state.step = 6

elif st.session_state.step == 6:
    if st.session_state.activities:
        st.write("Here are some activity suggestions:")
        for a in activity_data[st.session_state.destination]:
            st.markdown(f"- {a}")
    if st.button("Proceed with Options"):
        st.session_state.step = 7

elif st.session_state.step == 7:
    st.write("💰 Price Summary")
    hotel_price = int(st.session_state.hotel.split("$")[-1].split("/")[0])
    nights = 4  # Example stay duration
    total = hotel_price * nights
    if st.session_state.activities:
        total += 2500
        st.markdown(f"- Hotel stay: ${hotel_price} x {nights} nights = ${hotel_price * nights}")
        st.markdown("- Activities package = $2500")
    st.markdown(f"**Total = ${total}**")
    proceed = st.radio("Proceed with payment?", ["Yes", "No"])
    if proceed == "Yes":
        st.session_state.step = 8

elif st.session_state.step == 8:
    st.success("✅ A payment link has been sent via SMS. Please complete payment within 10 minutes.")
    st.write("Thanks for booking with us! We are excited to host you for a wonderful stay experience.")
    if st.button("Yay!!!"):
        st.session_state.step = 9

elif st.session_state.step == 9:
    st.write(f"Hi, Welcome **{st.session_state.guest_name}** 🎉")
    st.write(f"We are excited to host you at **{st.session_state.hotel.split('-')[0]}**.")
    st.write("Before you arrive, please keep handy:")
    st.markdown("- Identity Card\n- Health documents\n- Travel insurance\n- Booking confirmation receipt")
    if st.button("Okay"):
        st.session_state.step = 10

elif st.session_state.step == 10:
    st.write("We’d like to personalize your stay experience.")
    allergy = st.text_input("Please describe food allergy (type NA if none)")
    gym = st.text_input("Please confirm if you want to use gym (enter time in 24hr format, or NA)")
    if st.button("Submit Preferences"):
        st.session_state.allergies = allergy
        st.session_state.gym_time = gym
        st.session_state.step = 11

elif st.session_state.step == 11:
    st.write(f"Hi {st.session_state.guest_name}, please select from services available today:")
    service = st.radio("Select a service", ["Wake Up Call at 7AM", "Laundry", "Call cab", "Schedule breakfast in room"])
    if st.button("Confirm Service"):
        st.session_state.service = service
        st.session_state.step = 12

elif st.session_state.step == 12:
    st.success(f"Thanks for the confirmation. We will {st.session_state.service}.")
    st.write(f"Hi {st.session_state.guest_name}, thanks for choosing {st.session_state.hotel.split('-')[0]}. We hope you had a wonderful stay!")
    st.write("As a valued guest, enjoy a **2 nights & 3 days weekend stay at 50% discount** at any of ou
