def main(interface_chosen, problem_chosen, algorithm_chosen):
    if problem_chosen == "1":
        from Maze import Maze as Problem
        if interface_chosen == "1":
            from Maze_CLI import CLI as interface
        elif interface_chosen == "2":
            from Maze_GUI import GUI as interface

    elif problem_chosen == "2":
        from Eight_Queens import EightQueens as Problem
        if interface_chosen == "1":
            from Eight_Queens_CLI import CLI as interface
        elif interface_chosen == "2":
            from Eight_Queens_GUI import GUI as interface
    
    Problem.generate_problem()

    if algorithm_chosen == "1":
        from DLS import dls
        depth_limit = int(input("Enter the depth limit: "))
        path = dls(Problem, Problem.start, depth_limit, set())
        extra_text = f"Depth limit: {depth_limit}"
        interface(Problem, path, extra_text)
    elif algorithm_chosen == "2":
        from IDS import ids
        path, max_depth = ids(Problem)
        extra_text = f"Max depth reached: {max_depth}"
        interface(Problem, path, extra_text)
    elif algorithm_chosen == "3":
        from BestFirstSearch import best_first_search
        path = best_first_search(Problem)
        interface(Problem, path)
    elif algorithm_chosen == "4":
        from HillClimbing import hill_climbing
        path, extra_text = hill_climbing(Problem)
        interface(Problem, path, extra_text)
    elif algorithm_chosen == "5":
        from BidirectionalSearch import bidirectional_search
        path_from_start, path_from_goal, full_path = bidirectional_search(Problem)
        extra_text = f"""Path from start: {path_from_start}\nPath from goal: {path_from_goal}\nFull path: {full_path}"""
        interface(Problem, full_path, extra_text)
    elif algorithm_chosen == "6":
        from Minimax import minimax
        from math import log2
        print("Minimax algorithm can't be used for pathfinding so you will have to enter a custom list of scores.")
        scores = list(map(int, input("Enter the space-separated scores at the leaf nodes of the binary tree.\nThe number of scores must be a power of 2 (e.g., 2, 4, 8, 16, etc.): ").split()))
        tree_depth = int(log2(len(scores)))
        print("The optimal value is: ", minimax(0, 0, True, scores, tree_depth))
    elif algorithm_chosen == "7":
        from Alpha_Beta import alpha_beta
        from math import log2
        print("Minimax algorithm can't be used for pathfinding so you will have to enter a custom list of scores.")
        scores = list(map(int, input("Enter the space-separated scores at the leaf nodes of the binary tree.\nThe number of scores must be a power of 2 (e.g., 2, 4, 8, 16, etc.): ").split()))
        tree_depth = int(log2(len(scores)))
        print("The optimal value is: ", alpha_beta(0, 0, True, scores, tree_depth))

interface_chosen = input("""Interfaces:
1)CLI
2)GUI
Choose Interface: """)

problem_chosen = input("""
Problems:
1)Maze
2)8 Queens
Choose Problem: """)

algorithm_chosen = input("""
Algorithms:
1)Depth Limited Search
2)Iterative Deepening Search
3)Best First Search
4)Hill Climbing
5)Bidirectional Search
6)MinMax
7)Alpha-Beta
Choose Algorithm: """)

main(interface_chosen, problem_chosen, algorithm_chosen)