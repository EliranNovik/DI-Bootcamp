def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_input(player, board):
    while True:
        playermove = input(f"Player {player}, enter your move (1-9): ")
        try:
            playermove = int(playermove)
            if 1 <= playermove <= 9:
                row = (playermove - 1) // 3  
                col = (playermove - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = player
                    break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    current_player = "X"

    while True:
        display_board(board)
        player_input(current_player, board)
        
        result = check_win(board)

        if result == "Draw":
            display_board(board)
            print("It's a draw!")
            break
        elif result:
            display_board(board)
            print(f"Player {result} wins!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play()
