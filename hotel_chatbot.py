import streamlit as st
from datetime import datetime, timedelta, date

# ==============================
# Helpers
# ==============================
def reset_chat():
    """Clear all state and go to step 0."""
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.session_state.step = 0

def ensure_keys():
    """Initialize all session_state keys exactly once."""
    defaults = {
        "step": 0,
        "name": "",
        "destination": "",
        "checkin": None,          # datetime.date
        "checkout": None,         # datetime.date
        "selected_hotel": None,   # dict
        "activity_choice": "",    # "Show suggestions" | "Skip suggestion"
        "final_price": 0,
        "allergy": "",
        "gym_use": "",
        # in-stay services
        "wake_up_call": False,
        "laundry_request": False,
        "cab_request": False,
        "breakfast_request": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def schedule_activities(checkin_dt: date, acts: list[str]) -> list[str]:
    """Shift activities to consecutive days starting from check-in date."""
    if not isinstance(checkin_dt, date):
        return acts
    out = []
    for i, a in enumerate(acts):
        d = checkin_dt + timedelta(days=i)
        out.append(f"{d.strftime('%d %b')} - {a}")
        # cap at len(acts)
        if i == len(acts) - 1:
            break
    return out

# ==============================
# Static Data
# ==============================
preferences = {
    "Hawaii": "Deluxe room, balcony with sea view, non-smoking, breakfast included, accessibility- near to beach.",
    "Vail": "Deluxe room, balcony with snow view, non-smoking, breakfast included, accessibility- near to mountains.",
    "New York": "Deluxe room, balcony with city view, non-smoking, breakfast included, accessibility- near to subway.",
}

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
        },
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
            "phone": "(970) 476-2739)",
            "price": 662
        },
        {
            "name": "Vail's Mountain Haus",
            "rating": "4.4 star rating (252 reviews)",
            "desc": "Polished resort offering free breakfast and Wi-Fi, outdoor pool and hot tubs. Deluxe rooms available with balcony overlooking the mountains/snow. Walking distance to lifts and central Vail.",
            "phone": "(970) 476-2434",
            "price": 662
        },
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
        },
    ],
}

activities_catalog = {
    "Hawaii": [
        "Indulge in a 6 hr Sailing with private Yacht (11AM–6:30PM, sunset sailing & whale watching)",
        "Scuba diving with 2 dives and instructor session",
        "Enjoy your day at beach & seat at The Beach Bar Club for night party",
        "Jet Skiing",
    ],
    "Vail": [
        "4 hr Skiing activity with lunch",
        "Snowshoeing (Winter Walk) at Lost Lake Trail",
        "Bonfire night party at the hotel",
        "Leisure Day",
    ],
    "New York": [
        "Concert Day",
        "Guided city tour (Madison Square, Statue of Liberty, Empire State Building)",
        "Lunch at Bungalow (a Michelin Star restaurant)",
        "Leisure Day",
    ],
}

# ==============================
# App
# ==============================
st.set_page_config(page_title="Hotel Booking Chatbot", page_icon="🏨")
st.title("🏨 Hotel Booking Assistant")

# Always-on Restart
if st.button("🔄 Restart Chat"):
    reset_chat()
    st.experimental_rerun()

# Make sure we have all keys
ensure_keys()

# ==============================
# Step 0: Greeting
# ==============================
if st.session_state.step == 0:
    st.write("👋 Hello! Welcome to our Hotel Booking Assistant.")
    if st.button("Start Chat"):
        st.session_state.step = 1
        st.experimental_rerun()

# ==============================
# Step 1: Guest Name
# ==============================
elif st.session_state.step == 1:
    name_val = st.text_input("May I know your name?", value=st.session_state.name)
    if st.button("Submit Name"):
        if name_val.strip():
            st.session_state.name = name_val.strip()
            st.session_state.step = 2
            st.experimental_rerun()
        else:
            st.warning("Please enter a valid name to proceed.")

# ==============================
# Step 2: Destination
# ==============================
elif st.session_state.step == 2:
    dest = st.radio(
        f"Nice to meet you, **{st.session_state.name}**! Where would you like to go?",
        ["Hawaii (Beach)", "Vail, Colorado (Skiing)", "New York City (Music Concerts)"],
    )
    if st.button("Confirm Destination"):
        if "Hawaii" in dest:
            st.session_state.destination = "Hawaii"
        elif "Vail" in dest:
            st.session_state.destination = "Vail"
        else:
            st.session_state.destination = "New York"
        st.session_state.step = 21
        st.experimental_rerun()

# ==============================
# Step 21: Check-in / Check-out Dates
# ==============================
elif st.session_state.step == 21:
    st.write("📅 Please select your stay dates")
    checkin_dt = st.date_input("Check-in Date")
    checkout_dt = st.date_input("Check-out Date")
    if st.button("Confirm Dates"):
        if isinstance(checkin_dt, date) and isinstance(checkout_dt, date) and checkin_dt < checkout_dt:
            st.session_state.checkin = checkin_dt
            st.session_state.checkout = checkout_dt
            st.session_state.step = 3
            st.experimental_rerun()
        else:
            st.error("⚠️ Please pick a valid date range (check-in must be before check-out).")

# ==============================
# Step 3: Show Preferences (based on destination)
# ==============================
elif st.session_state.step == 3:
    d = st.session_state.destination
    st.write(f"Based on your previous stay preferences for **{d}**, we are considering:")
    st.info(preferences[d])
    if st.button("Go for Hotel Options"):
        st.session_state.step = 4
        st.experimental_rerun()

# ==============================
# Step 4: Hotel Options (with icons)
# ==============================
elif st.session_state.step == 4:
    d = st.session_state.destination
    st.write(f"Here are some hotel options in **{d}**:")

    # Choose via radio so only one is active, then Confirm
    labels = [f"Option {i+1}: {h['name']}" for i, h in enumerate(hotel_options[d])]
    choice = st.radio("Select a hotel:", labels, index=0, key="hotel_radio")

    # Show the chosen hotel details
    idx = labels.index(choice)
    h = hotel_options[d][idx]
    st.markdown(
        f"### 🏨 {h['name']}\n"
        f"⭐ **Rating:** {h['rating']}\n"
        f"📝 **Description:** {h['desc']}\n"
        f"📞 **Phone:** {h['phone']}\n"
        f"💲 **Price:** ${h['price']} per night (inclusive of all taxes)\n"
        f"📍 **Directions:** Available at property concierge"
    )

    if st.button("Proceed with this Hotel"):
        st.session_state.selected_hotel = h
        st.session_state.step = 5
        st.experimental_rerun()

# ==============================
# Step 5: Activities Option
# ==============================
elif st.session_state.step == 5:
    h = st.session_state.selected_hotel
    st.success(f"You selected **{h['name']}** (${h['price']} per night).")
    act_choice = st.radio("Would you like to book other activities?", ["Show suggestions", "Skip suggestion"], index=1)
    if st.button("Confirm Choice"):
        st.session_state.activity_choice = act_choice
        if act_choice == "Show suggestions":
            st.session_state.step = 6
        else:
            st.session_state.step = 8
        st.experimental_rerun()

# ==============================
# Step 6: Show Activities (dates derived from check-in)
# ==============================
elif st.session_state.step == 6:
    d = st.session_state.destination
    acts = schedule_activities(st.session_state.checkin, activities_catalog[d])
    st.write("Here are activity suggestions for your trip:")
    for a in acts:
        st.markdown(f"- {a}")
    if st.button("Proceed with these activities"):
        st.session_state.step = 8
        st.experimental_rerun()
    if st.button("Cancel suggestions and skip"):
        st.session_state.activity_choice = "Skip suggestion"
        st.session_state.step = 8
        st.experimental_rerun()

# ==============================
# Step 8: Price Summary
# ==============================
elif st.session_state.step == 8:
    h = st.session_state.selected_hotel
    checkin_dt = st.session_state.checkin
    checkout_dt = st.session_state.checkout
    try:
        nights = (checkout_dt - checkin_dt).days
        nights = max(nights, 1)
    except Exception:
        nights = 1

    base = h["price"] * nights
    total = base
    st.write(f"🏨 **Hotel** ({nights} night{'s' if nights != 1 else ''}): ${base}")

    if st.session_state.activity_choice == "Show suggestions":
        st.write("🎉 **Activities Package:** $2500")
        total += 2500
    else:
        st.write("🎉 **Activities Package:** Skipped")

    st.session_state.final_price = total
    st.success(f"💰 **Total Price:** ${total}")

    if st.button("Proceed to Payment"):
        st.session_state.step = 9
        st.experimental_rerun()

# ==============================
# Step 9: Payment
# ==============================
elif st.session_state.step == 9:
    st.info("💳 A payment link has been sent via SMS to your mobile number. Please make the payment in 10 minutes and proceed with the booking.")
    st.write("Thanks for booking with us. We are excited to host you for a wonderful stay experience.")
    if st.button("Yay!!!"):
        st.session_state.step = 10
        st.experimental_rerun()

# ==============================
# Step 10: Pre-arrival Documents & Personalization Prompt
# ==============================
elif st.session_state.step == 10:
    hotel_name = (st.session_state.selected_hotel or {}).get("name", "the hotel")
    st.write(f"Hi, Welcome {st.session_state.name}")
    st.write(f"We are excited to host you for your upcoming stay with us at **{hotel_name}**.")
    st.write("Before you arrive, please keep the following documents handy for a smooth experience:")
    st.markdown("- Identity card\n- Health issues related documents\n- Travel insurance\n- Booking confirmation receipt")
    st.write("We would ask you to spend a minute with us to personalize your experience during the stay.")
    if st.button("Okay"):
        st.session_state.step = 18
        st.experimental_rerun()

# ==============================
# Step 18: Personalization (Allergy, Gym)
# ==============================
elif st.session_state.step == 18:
    st.session_state.allergy = st.text_input(
        "i) Please describe food allergy, if any. Type 'NA' in case of no allergy.",
        value=st.session_state.allergy,
    )
    st.session_state.gym_use = st.text_input(
        "ii) Please confirm if you want to use gym during your stay in 24 hr time format. (Or type 'NA')",
        value=st.session_state.gym_use,
    )
    if st.button("Proceed"):
        st.success("Thanks for your confirmation!")
        st.session_state.step = 19
        st.experimental_rerun()

# ==============================
# Step 19: In-stay Services (Multi-select)
# ==============================
elif st.session_state.step == 19:
    st.write(f"Hi {st.session_state.name}, we hope you are having a wonderful experience during your stay.")
    st.write("Please select from the options below:")

    options = ["Wake Up Call at 7AM", "Laundry", "Call cab", "Schedule breakfast in room"]
    selected = st.multiselect("Select services you want:", options)

    if st.button("Confirm Services"):
        st.session_state.wake_up_call = "Wake Up Call at 7AM" in selected
        st.session_state.laundry_request = "Laundry" in selected
        st.session_state.cab_request = "Call cab" in selected
        st.session_state.breakfast_request = "Schedule breakfast in room" in selected

        for s in selected:
            st.success(f"Thanks for the confirmation. We will {s} ✅")

        st.session_state.step = 20
        st.experimental_rerun()

# ==============================
# Step 20: Service Confirmation
# ==============================
elif st.session_state.step == 20:
    hotel_name = (st.session_state.selected_hotel or {}).get("name", "your hotel")
    st.write(f"Hi {st.session_state.name}, thanks for choosing **{hotel_name}** for your stay.")
    st.write("Here’s a summary of the services you selected:")
    if st.session_state.wake_up_call:     st.write("✅ Wake Up Call at 7AM")
    if st.session_state.laundry_request:   st.write("✅ Laundry")
    if st.session_state.cab_request:       st.write("✅ Call cab")
    if st.session_state.breakfast_request: st.write("✅ Schedule breakfast in room")

    if st.button("Proceed Further"):
        st.session_state.step = 21
        st.experimental_rerun()

# ==============================
# Step 21 (post-stay): Thank You & Feedback Prompt
# ==============================
elif st.session_state.step == 21:
    hotel_name = (st.session_state.selected_hotel or {}).get("name", "your hotel")
    st.write(f"Hi {st.session_state.name}, Thanks for choosing **{hotel_name}** for your stay. Hope you had a wonderful time staying with us.")
    st.write("We would love to hear back from you on your experience.")
    if st.button("Provide Feedback / Proceed"):
        st.session_state.step = 22
        st.experimental_rerun()

# ==============================
# Step 22: Loyalty Offer
# ==============================
elif st.session_state.step == 22:
    st.write("As you have been an esteemed member of [HotelChainName], we are happy to share **2 night & 3 day weekend stay at any of our properties at flat 50% discount**.")
    st.write("You can avail this offer within 365 days. Just login to our website with your registered email id to claim the offer.")
    if st.button("Finish"):
        st.success("🎉 Thank you! We hope to welcome you back soon.")
        # Offer a restart at the end as well
        if st.button("Restart Chat"):
            reset_chat()
            st.experimental_rerun()
