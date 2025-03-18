from os import system

def print_board(board):
    for i in [["Q" if (i,j) in list(enumerate(board)) else 0 for j in range(8)] for i in range(8)]:
        print(*i)

def CLI(EightQueens, path, extra_text=""):
    system("cls")
    print("Start:")
    print_board(EightQueens.start.get_state())
    print("Goal:")
    print_board(EightQueens.goal.get_state())
    if extra_text:
        print(extra_text)
    print("Board:")
    print_board(EightQueens.start.get_state())
    if path:
        print("Path:", [])
        system("cls")
        temp_board = EightQueens.start.get_state().copy()
        temp_path = []
        for board in path:
            system("cls")
            temp_board = board
            temp_path.append(board)
            print("Start:")
            print_board(EightQueens.start.get_state())
            print("Goal:")
            print_board(EightQueens.goal.get_state())
            if extra_text:
                print(extra_text)
            print("Board:")
            print_board(temp_board)
            print("Path:", temp_path)
            if len(temp_path) != len(path):
                input("Press enter for next move...")
    else:
        print("No path found")