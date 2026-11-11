
import streamlit as st

st.set_page_config(
    page_title="AI Virtual Lab",
    page_icon="🤖",
    layout="wide"
)

# ---------- AI GAME FUNCTIONS ----------

def check_winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def minimax(board, depth, is_ai):
    result = check_winner(board)

    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if result == "Draw":
        return 0

    if is_ai:
        best_score = -1000

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(best_score, score)

        return best_score


def ai_move(board):
    best_score = -1000
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"


def play_turn(index):
    board = st.session_state.board

    if board[index] == "" and check_winner(board) is None:
        board[index] = "X"

        if check_winner(board) is None:
            ai_move(board)


# ---------- MAIN WEBSITE ----------

st.title("🤖 AI VIRTUAL LAB")
st.subheader("Artificial Intelligence – Problem Solving Laboratory")

st.write(
    "Welcome! Explore classical Artificial Intelligence "
    "problems through interactive experiments."
)

experiments = [
    "Tic-Tac-Toe",
    "8-Queen Problem",
    "Chess Problem",
    "Tower of Hanoi",
    "Travelling Salesperson",
    "Monkey and Banana",
    "Cryptarithmetic",
    "Block World"
]

choice = st.sidebar.selectbox(
    "Select an AI Experiment",
    experiments
)

st.markdown("---")

# ---------- TIC TAC TOE ----------

if choice == "Tic-Tac-Toe":

    st.header("⭕ Tic-Tac-Toe: Play Against AI")

    st.write("You are X. The computer is O.")
    st.write("Try to win against the AI!")

    if "board" not in st.session_state:
        st.session_state.board = [""] * 9

    board = st.session_state.board
    result = check_winner(board)

    if result is None:
        st.info("Your turn: Select an empty square.")

    elif result == "X":
        st.success("Congratulations! You won!")

    elif result == "O":
        st.error("AI wins! Try again.")

    else:
        st.warning("The game is a draw!")

    for row in range(3):
        cols = st.columns(3)

        for col in range(3):
            index = row * 3 + col

            label = board[index] if board[index] else "⬜"

            cols[col].button(
                label,
                key=f"cell_{index}",
                use_container_width=True,
                disabled=(board[index] != "" or result is not None),
                on_click=play_turn,
                args=(index,)
            )

    if st.button("🔄 Restart Game"):
        st.session_state.board = [""] * 9
        st.rerun()

    st.markdown("---")
    st.subheader("AI Concept")

    st.write("""
    This game uses the Minimax algorithm.

    - X represents the human player.
    - O represents the AI player.
    - The AI searches possible future moves.
    - It selects the move with the best outcome.
    """)

# ---------- OTHER EXPERIMENTS ----------

else:
    st.header(choice)

    descriptions = {
        "8-Queen Problem": "Place eight queens on a chessboard without attacking each other.",
        "Chess Problem": "Explore legal moves and AI game search.",
        "Tower of Hanoi": "Move disks between rods using recursion.",
        "Travelling Salesperson": "Find the shortest route connecting cities.",
        "Monkey and Banana": "Plan actions to help a monkey reach a banana.",
        "Cryptarithmetic": "Solve arithmetic puzzles using letters as digits.",
        "Block World": "Rearrange blocks to achieve a target arrangement."
    }

    st.info(descriptions[choice])
    st.write("Interactive experiment will be added in the next development stage.")

st.markdown("---")
st.caption("EEE Department | AI Virtual Laboratory")
