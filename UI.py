import streamlit as st
import requests


base_url = "http://127.0.0.1:8000" 

st.title("FOOTBALL COSMOS")



st.header("Football Clubs")

club_name = st.text_input("Enter Club Name:")

if st.button("Get Club info"):
    if club_name:
        url = f"{base_url}/club/{club_name}/" 
        response = requests.get(url)
        if response.status_code == 200:
            club_info = response.json()
            st.write(club_info)

            col1,col2 = st.columns(2)

            club_logo = club_info.get("Logo_URL")
            jersey_url = club_info.get("Jersey_URL")

            with col1:
                if club_logo:
                    st.image(club_logo, caption=f"{club_name} logo")
                else:
                    st.write("no logo found")

            with col2:
                if jersey_url:
                    st.image(jersey_url, caption=f"{club_name} jersey")
                else:
                    st.write("no jersey found")
        else:
            st.error("Club not found")
    else:
        st.error("Please enter a club name.")


st.header("Football Stars")

player_name = st.text_input("Enter Player Name:")

if st.button("Get Player info"):
    if player_name:
        url = f"{base_url}/players/{player_name}/" 
        response = requests.get(url)
        if response.status_code == 200:
            player_info = response.json()
            st.write(player_info)

            player_URL = player_info.get("Player_URL")
            if player_URL:
                st.image(player_URL,caption=f"Football Star {player_name}")
            else:
                st.write("no image found")

        else:
            st.error("Player not found or an error occurred.")
    else:
        st.error("Please enter a player name.")


st.header("Club Tactics")

tactics_name = st.text_input("Enter Tactics Name:")

if st.button("Get Club Tacticts"):
    if tactics_name:
        url = f"{base_url}/tactics/{tactics_name}/" 
        response = requests.get(url)
        if response.status_code == 200:
            tactics_info = response.json()
            st.write(tactics_info)
        else:
            st.error("Tactics not found or an error occurred.")
    else:
        st.error("Please enter tactics name.")


st.header("Fan Insights")

with st.form("fan_comment_form"):
    fan_name = st.text_input("Your Name")
    fav_club = st.text_input("Favorite Club")
    best_match = st.text_input("Best Match")
    comment = st.text_area("Your Comment")
    submitted = st.form_submit_button("Submit Comment")

    if submitted:
        data = {
            "fan_name": fan_name,
            "fav_club": fav_club,
            "best_match": best_match,
            "comment": comment
        }
        url = f"{base_url}/fans/"  
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success("submitted successfully!")
        else:
            st.error("Failed to submit comment.")
