# hotel_chatbot.py
import streamlit as st

st.set_page_config(page_title="Hotel Contact Center Bot", page_icon="🏨", layout="centered")

st.title("🏨 Conversational Hotel AI Chatbot")

# Step tracker
if "step" not in st.session_state:
    st.session_state.step = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "destination" not in st.session_state:
    st.session_state.destination = ""

# Greeting
if st.session_state.step == 1:
    st.write("👋 Hello! Welcome to our hotel booking assistant.")
    st.write("May I know your name?")
    name = st.text_input("Your name:")
    if name:
        st.session_state.name = name
        st.session_state.step = 2
        st.experimental_rerun()

# Ask destination
elif st.session_state.step == 2:
    st.write(f"Nice to meet you, **{st.session_state.name}**! 🌟")
    st.write("Where would you like to go?")
    choice = st.radio(
        "Choose your destination:",
        ["Hawaii (Beaches)", "Vail, Colorado (Skiing)", "New York City (Music Concerts)"]
    )
    if st.button("Confirm Destination"):
        st.session_state.destination = choice
        st.session_state.step = 3
        st.experimental_rerun()

# Show preferences
elif st.session_state.step == 3:
    dest = st.session_state.destination
    st.write(f"Based on your previous stay preferences, here’s what we suggest for **{dest}**:")

    if "Hawaii" in dest:
        st.markdown("""
        - 🛏️ Deluxe Room  
        - 🌊 Balcony with Sea View  
        - 🚭 No Smoking Room  
        - 🥞 Breakfast Included  
        - 🏖️ Near to Beach  
        """)
    elif "Vail" in dest:
        st.markdown("""
        - 🛏️ Deluxe Room  
        - ❄️ Balcony with Snow View  
        - 🚭 No Smoking Room  
        - 🥞 Breakfast Included  
        - 🏔️ Near to Mountains  
        """)
    elif "New York" in dest:
        st.markdown("""
        - 🛏️ Deluxe Room  
        - 🌆 Balcony with City View  
        - 🚭 No Smoking Room  
        - 🥞 Breakfast Included  
        - 🚇 Near to Subway  
        """)

    if st.button("Go for Hotel Options"):
        st.session_state.step = 4
        st.experimental_rerun()

# Show hotel options
elif st.session_state.step == 4:
    dest = st.session_state.destination
    st.write(f"Here are some top hotel options for **{dest}**:")

    if "Hawaii" in dest:
        st.markdown("""
        **Option 1: Mauna Kea Beach Hotel, Autograph Collection**  
        ⭐ 4.6 (1,563 reviews) | Price: $632/night  
        📍 (808) 882-7222  

        **Option 2: Hilton Hawaiian Village Waikiki Beach Resort**  
        ⭐ 4.2 (25,213 reviews) | Price: $714/night  
        📍 (808) 949-4321  

        **Option 3: Waikoloa Beach Marriott Resort & Spa**  
        ⭐ 4.4 (3,743 reviews) | Price: $578/night  
        📍 (808) 886-6789  

        **Option 4: Castle Kona Bali Kai**  
        ⭐ 4.0 (485 reviews) | Price: $540/night  
        📍 (808) 329-9381  
        """)
    
    elif "Vail" in dest:
        st.markdown("""
        **Option 1: The Arrabelle at Vail Square**  
        ⭐ 4.6 (697 reviews) | Price: $399/night  
        📍 (888) 688-8055  

        **Option 2: The Ritz-Carlton Club, Vail**  
        ⭐ 4.7 (377 reviews) | Price: $1799/night  
        📍 (970) 477-3700  

        **Option 3: Highline Vail - a DoubleTree by Hilton**  
        ⭐ 4.2 (944 reviews) | Price: $662/night  
        📍 (970) 476-2739  

        **Option 4: Vail's Mountain Haus**  
        ⭐ 4.4 (252 reviews) | Price: $662/night  
        📍 (970) 476-2434  
        """)
    
    elif "New York" in dest:
        st.markdown("""
        **Option 1: The Plaza Hotel**  
        ⭐ 4.6 (3,142 reviews) | Price: $999/night  
        📍 (212) 759-3000  

        **Option 2: The Ritz-Carlton New York, Central Park**  
        ⭐ 4.7 (1,221 reviews) | Price: $1299/night  
        📍 (212) 308-9100  

        **Option 3: Arlo Midtown**  
        ⭐ 4.3 (2,341 reviews) | Price: $420/night  
        📍 (212) 343-7000  

        **Option 4: CitizenM New York Times Square**  
        ⭐ 4.5 (4,522 reviews) | Price: $390/night  
        📍 (212) 461-3638  
        """)
