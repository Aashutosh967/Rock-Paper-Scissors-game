import streamlit as st
import random

# Page config
st.set_page_config(page_title="Rock Paper Scissors")

# Page title
st.title("Rock Paper Scissors Game")

# Initialize session state variables
if 'player_score' not in st.session_state:
    st.session_state['player_score'] = 0
if 'computer_score' not in st.session_state:
    st.session_state['computer_score'] = 0

# Scoreboard
col1, col2 = st.columns(2)
col1.metric("Player", st.session_state['player_score'])
col2.metric("Computer", st.session_state['computer_score'])

# Player name input
player_name = st.text_input("Enter your name", value="Player 1")

# Spacer
st.markdown("""<hr/>""", unsafe_allow_html=True)

# Player choice selection
player_choice = st.radio("Select your move", ["Rock 👊", "Paper 🖐", "Scissors ✌️"])

# Computer random choice
computer_choice = random.choice(["Rock", "Paper", "Scissors"])

# Display choices
st.write(f"{player_name} chose: {player_choice}")
st.write(f"Computer chose: {computer_choice}")

# Game logic
if player_choice == computer_choice:
    st.write("It's a tie!")
elif (player_choice == "Rock 👊" and computer_choice == "Scissors") or \
        (player_choice == "Paper 🖐" and computer_choice == "Rock") or \
        (player_choice == "Scissors ✌️" and computer_choice == "Paper"):
    st.session_state['player_score'] += 1
    st.success(f"You win {player_name}!")
else:
    st.session_state['computer_score'] += 1
    st.error("Oops, computer wins.")

# Play again button
if st.button("Play Again"):
    st.legacy_caching.clear_cache()