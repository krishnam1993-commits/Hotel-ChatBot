# hotel_chatbot.py
import streamlit as st

st.set_page_config(page_title="Hotel Booking Chatbot", page_icon="🏨", layout="centered")

# ----------------- Session state init -----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""
if "selected_hotel_index" not in st.session_state:
    st.session_state.selected_hotel_index = None
if "selected_hotel" not in st.session_state:
    st.session_state.selected_hotel = None
if "activity_choice" not in st.session_state:
    st.session_state.activity_choice = None
if "activities_confirmed" not in st.session_state:
    st.session_state.activities_confirmed = False
if "activity_price" not in st.session_state:
    st.session_state.activity_price = 0
if "total_price" not in st.session_state:
    st.session_state.total_price = 0
if "payment_proceed" not in st.session_state:
    st.session_state.payment_proceed = False
if "allergy" not in st.session_state:
    st.session_state.allergy = ""
if "gym_time" not in st.session_state:
    st.session_state.gym_time = ""
if "instay_service" not in st.session_state:
    st.session_state.instay_service = ""
if "feedback_claim" not in st.session_state:
    st.session_state.feedback_claim = False

# ----------------- Hotel data -----------------
hotel_options = {
    "Hawaii": [
        {
            "name": "Mauna Kea Beach Hotel, Autograph Collection",
            "rating": "4.6 star rating (1,563 reviews)",
            "desc": "Upscale, beachfront resort featuring airy rooms, many with balconies and sea views. Highly rated for ocean access, luxury accommodations, accessibility, and on-site dining—including breakfast packages.",
            "phone": "(808) 882-7222",
            "price": 632
        },
        {
            "name": "Hilton Hawaiian Village Waikiki Beach Resort",
            "rating": "4.2 star rating (25,213 reviews)",
            "desc": "Sprawling oceanfront resort on Waikiki Beach; high-rise rooms with sea view balconies available. Wide range of amenities, breakfast options, and non-smoking room preference supported.",
            "phone": "(808) 949-4321",
            "price": 714
        },
        {
            "name": "Waikoloa Beach Marriott Resort & Spa",
            "rating": "4.4 star rating (3,743 reviews)",
            "desc": "Classy beachfront hotel with modern deluxe rooms and suites, often with sea-view balconies. Includes breakfast, accessible location, and close proximity to sand and surf.",
            "phone": "(808) 886-6789",
            "price": 578
        },
        {
            "name": "Castle Kona Bali Kai",
            "rating": "4 Star Rating (485 reviews)",
            "desc": "Oceanfront condos featuring lanais (balconies), select units with sea views, non-smoking available. Beachfront, pool, and breakfast offered.",
            "phone": "(808) 329-9381",
            "price": 540
        }
    ],
    "Vail": [
        {
            "name": "The Arrabelle at Vail Square",
            "rating": "4.6 star rating (697 reviews)",
            "desc": "Elegant hotel with rooms featuring balconies and mountain views, rooftop pool, fine dining, and cozy lounge. Central Vail location offers easy access to lifts and town.",
            "phone": "(888) 688-8055",
            "price": 399
        },
        {
            "name": "The Ritz-Carlton Club, Vail",
            "rating": "4.7 star rating (377 reviews)",
            "desc": "Sophisticated villas with balconies and mountain/snow views; premium service and outdoor pool. Check for breakfast package and non-smoking room when booking. Located near ski lifts and mountain activities.",
            "phone": "(970) 477-3700",
            "price": 1799
        },
        {
            "name": "Highline Vail - a DoubleTree by Hilton",
            "rating": "4.2 star rating (944 reviews)",
            "desc": "Refined rooms and suites, some with balcony and mountain views. Onsite dining, breakfast option, and free mountain shuttle. Confirm balcony/snow view room and breakfast inclusion at reservation.",
            "phone": "(970) 476-2739",
            "price": 662
        },
        {
            "name": "Vail's Mountain Haus",
            "rating": "4.4 star rating (252 reviews)",
            "desc": "Polished resort offering free breakfast and Wi-Fi, outdoor pool and hot tubs. Deluxe rooms available with balcony overlooking the mountains/snow. Walking distance to lifts and central Vail.",
            "phone": "(970) 476-2434",
            "price": 662
        }
    ],
    "New York": [
        {
            "name": "Hotel Mulberry",
            "rating": "4.3 star rating (439 reviews)",
            "desc": "Contemporary rooms & suites, some with terraces or city views, plus free breakfast & WiFi. Located in Chinatown, very close to multiple subway stations.",
            "phone": "(212) 385-4633",
            "price": 499
        },
        {
            "name": "Hampton Inn Brooklyn/Downtown",
            "rating": "4.4 star rating (2,551 reviews)",
            "desc": "Contemporary hotel with suites that include balconies, free hot breakfast, and easy subway access at Jay St-MetroTech. Non-smoking and accessibility included.",
            "phone": "(718) 875-8800",
            "price": 399
        },
        {
            "name": "The Washington Hotel NYC",
            "rating": "3.8 star rating (2,057 reviews)",
            "desc": "Premium hotel with terraces offering city views. Sleek rooms, breakfast available, convenient access to Wall St and Rector St subway stops.",
            "phone": "(646) 826-8600",
            "price": 399
        },
        {
            "name": "Madison LES Hotel",
            "rating": "4 star rating (819 reviews)",
            "desc": "Informal hotel offering a free hot breakfast buffet, rooftop terrace with views, and proximity to East Broadway subway.",
            "phone": "(212) 390-1533",
            "price": 399
        }
    ]
}

preferences = {
    "Hawaii": "deluxe room, balcony with sea view, no smoking room, breakfast included, accessibility- near to beach.",
    "Vail": "deluxe room, balcony with snow view, no smoking room, breakfast included, accessibility- near to mountains.",
    "New York": "deluxe room, balcony with city view, no smoking room, breakfast included, accessibility- near to subway."
}

activities = {
    "Hawaii": [
        "6th Dec- Indulge in a 6 hr Sailing with private Yacht from 11AM to 6:30 PM with sunset sailing and whale watching",
        "7th Dec- Scuba diving with 2 dives and instructor session",
        "8th Dec- Enjoy your day at beach & Seat at The Beach Bar Club for night party",
        "9th Dec- Jet Skiing"
    ],
    "Vail": [
        "6th Dec- Indulge in a 4 hr Skiing activity with lunch",
        "7th Dec- Snowshoeing (Winter Walk) at Lost Lake Trail",
        "8th Dec- Enjoy a bonfire night party at the hotel",
        "9th Dec- Leisure Day"
    ],
    "New York": [
        "6th Dec- Concert Day",
        "7th Dec- Guided city tour for NYC including locations like Madison Square, Statue of Liberty, Empire State Building",
        "8th Dec- Enjoy lunch at Bungalow ( a Michelin Star restaurant)",
        "9th Dec- Leisure Day"
    ]
}

# ----------------- Helper functions -----------------
def reset_chat():
    st.session_state.clear()
    st.session_state.step = 0

# ----------------- Chat flow UI -----------------
st.title("🏨 Hotel Booking Assistant")

# Step 1: Bot greets the Guest first
if st.session_state.step == 0:
    st.write("👋 Hello! Welcome to our Hotel Booking Assistant.")
    if st.button("Start Chat"):
        st.session_state.step = 1

# Step 2: Ask Guest name
elif st.session_state.step == 1:
    st.write("May I know your name?")
    name_input = st.text_input("Guest name", value=st.session_state.name)
    if st.button("Submit Name"):
        if name_input and name_input.strip():
            st.session_state.name = name_input.strip()
            st.session_state.step = 2
        else:
            st.warning("Please enter a name to proceed.")

# Step 3: Ask destination with options
elif st.session_state.step == 2:
    st.write(f"Nice to meet you, **{st.session_state.name}**!")
    st.write("Where does the Guest want to go?")
    dest_choice = st.radio(
        "Choose a destination:",
        ("Hawaii for beach", "Vail, Colorado for skiing", "NYC for music concert")
    )
    if st.button("Confirm Destination"):
        if "Hawaii" in dest_choice:
            st.session_state.destination = "Hawaii"
        elif "Vail" in dest_choice:
            st.session_state.destination = "Vail"
        else:
            st.session_state.destination = "New York"
        st.session_state.step = 3

# Step 4: Show preferences based on previous stay (listed)
elif st.session_state.step == 3:
    d = st.session_state.destination
    st.write("Based on your previous stay preferences, we are considering:")
    if d == "Hawaii":
        st.markdown(f"- **Preference:** {preferences['Hawaii']}")
    elif d == "Vail":
        st.markdown(f"- **Preference:** {preferences['Vail']}")
    elif d == "New York":
        st.markdown(f"- **Preference:** {preferences['New York']}")
    if st.button("Go for Hotel Options"):
        st.session_state.step = 4

# Step 5: Show hotel options for chosen destination
elif st.session_state.step == 4:
    d = st.session_state.destination
    st.write(f"Stay options for **{d}**")
    hotels = hotel_options[d]
    for idx, h in enumerate(hotels, start=1):
        st.markdown(f"**Option-{idx}**  \n**{h['name']}**  \n{h['rating']}  \n{h['desc']}  \n**Directions** {h['phone']}  \n**Price- ${h['price']} per night (inclusive of all taxes)**")
        st.divider()
    chosen = st.radio("Select hotel option:", [f"Option-{i}" for i in range(1, len(hotels)+1)])
    if st.button("Confirm Hotel Selection"):
        sel_idx = int(chosen.split("-")[1]) - 1
        st.session_state.selected_hotel_index = sel_idx
        st.session_state.selected_hotel = hotels[sel_idx]
        st.session_state.total_price = st.session_state.selected_hotel["price"]
        st.session_state.step = 5

# Step 8: Ask guest if interested in booking other activities and give two options
elif st.session_state.step == 5:
    st.write("Would you like to book other activities?")
    act_choice = st.radio("Choose:", ("Show suggestions", "Skip suggestion"))
    if st.button("Confirm"):
        st.session_state.activity_choice = act_choice
        if act_choice == "Show suggestions":
            st.session_state.step = 6
        else:
            st.session_state.activities_confirmed = False
            st.session_state.step = 9

# Step 9 (if Show suggestions chosen): display activities and allow proceed
elif st.session_state.step == 6:
    d = st.session_state.destination
    st.write("Here are suggestions:")
    for a in activities[d]:
        st.markdown(f"- {a}")
    if st.button("Proceed with suggestions"):
        st.session_state.activity_price = 2500
        st.session_state.activities_confirmed = True
        st.session_state.step = 9
    if st.button("Cancel suggestions and skip"):
        st.session_state.activity_price = 0
        st.session_state.activities_confirmed = False
        st.session_state.step = 9

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
