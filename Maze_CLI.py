from os import system

def print_maze(maze):
    for row in maze:
        print(*row)

def CLI(Maze, path, extra_text=""):
    system("cls")
    print("Start:", Maze.start.get_state())
    print("Goal:", Maze.goal.get_state())
    if extra_text:
        print(extra_text)
    print("Maze:")
    print_maze(Maze.maze)
    if path:
        print("Path:", [])
        system("cls")
        temp_maze = Maze.maze.copy()
        temp_path = []
        for i, j in path:
            system("cls")
            temp_maze[i][j] = "*"
            temp_path.append((i,j))
            print("Start:", Maze.start.get_state())
            print("Goal:", Maze.goal.get_state())
            if extra_text:
                print(extra_text)
            print("Maze:")
            print_maze(temp_maze)
            print("Path:", temp_path)
            if len(temp_path) != len(path):
                input("Press enter for next move...")
    else:
        print("No path found")