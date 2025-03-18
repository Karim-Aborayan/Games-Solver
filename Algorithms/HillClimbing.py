def hill_climbing(Problem):
    current = Problem.start
    path = [current.get_state()]
    while current.get_state() != Problem.goal.get_state():
        neighbours = list(current.generate_neighbours())
        if not neighbours:
            print("No more moves available, stuck at:", current.get_state())
            return path, f"No more moves available, stuck at: {current.get_state()}"

        next = min(neighbours, key=lambda neighbour: neighbour.manhattan_distance(Problem.goal))

        if next.manhattan_distance(Problem.goal) >= current.manhattan_distance(Problem.goal):
            print("No better moves available, stuck at:", current.get_state())
            return path, f"No better moves available, stuck at: {current.get_state()}"

        current = next
        path.append(current.get_state())

    return path, ""