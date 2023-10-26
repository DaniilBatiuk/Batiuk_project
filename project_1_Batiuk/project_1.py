import random

def display_board(board):
    for i, row in enumerate(board):
        formatted_row = '| '.join(row)
        print(f' {formatted_row}')
        if i < 2:
            print('-' * 8)
    print("\n")

def enter_move(board):
    while True:
        try:
            user_move = int(input("Enter your move (choose a free cell from 1 to 9): "))
            if 1 <= user_move <= 9:
                row, col = divmod(user_move - 1, 3)
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("This cell is already occupied. Try another one.")
            else:
                print("Invalid choice. Enter a cell number from 1 to 9.")
        except ValueError:
            print("Invalid input. Enter a cell number from 1 to 9.")


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'
        
def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

board = init_board()
display_board(board)
draw_move(board)
while True:
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You win!")
        break

    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        print("It's a draw!")
        break

    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("Computer wins!")
        break
