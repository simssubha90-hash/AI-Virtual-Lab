
import streamlit as st

st.set_page_config(
    page_title="AI Virtual Lab",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI VIRTUAL LAB")
st.subheader("Artificial Intelligence – Problem Solving Laboratory")

st.write(
    "Welcome to the AI Virtual Lab! "
    "Explore classical Artificial Intelligence problems "
    "through interactive experiments."
)

experiments = {
    "Tic-Tac-Toe": "Game playing and Minimax algorithm",
    "8-Queen Problem": "Constraint satisfaction and backtracking",
    "Chess Problem": "Game trees and search algorithms",
    "Tower of Hanoi": "Recursion and state-space representation",
    "Travelling Salesperson": "Combinatorial optimisation",
    "Monkey and Banana": "State-space search and planning",
    "Cryptarithmetic": "Constraint satisfaction",
    "Block World": "AI planning and goal-based problem solving"
}

choice = st.sidebar.selectbox(
    "Select an AI Experiment",
    list(experiments.keys())
)

st.header(choice)
st.info(experiments[choice])

st.markdown("---")
st.subheader("Experiment Instructions")

st.write("1. Understand the problem.")
st.write("2. Identify the initial state and goal state.")
st.write("3. Study the algorithm.")
st.write("4. Run the experiment.")
st.write("5. Observe and record the result.")

if choice == "Tic-Tac-Toe":
    st.write("Tic-Tac-Toe experiment will be developed here.")
elif choice == "8-Queen Problem":
    st.write("8-Queen visualisation will be developed here.")
elif choice == "Chess Problem":
    st.write("Chess experiment will be developed here.")
elif choice == "Tower of Hanoi":
    st.write("Tower of Hanoi simulation will be developed here.")
elif choice == "Travelling Salesperson":
    st.write("Travelling Salesperson simulation will be developed here.")
elif choice == "Monkey and Banana":
    st.write("Monkey and Banana problem will be developed here.")
elif choice == "Cryptarithmetic":
    st.write("Cryptarithmetic solver will be developed here.")
elif choice == "Block World":
    st.write("Block World simulation will be developed here.")

st.markdown("---")
st.caption("EEE Department | AI Virtual Laboratory")
