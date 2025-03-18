from collections import deque

def bidirectional_search(Problem):
    if Problem.start.get_state() == Problem.goal.get_state():
        return [Problem.start.get_state()]

    forward_queue = deque([Problem.start])
    backward_queue = deque([Problem.goal])

    forward_parents = {Problem.start.get_state_tuple(): None}
    backward_parents = {Problem.goal.get_state_tuple(): None}

    forward_visited = {Problem.start.get_state_tuple()}
    backward_visited = {Problem.goal.get_state_tuple()}

    while forward_queue and backward_queue:
        if forward_queue:
            current_node = forward_queue.popleft()
            for neighbor in current_node.generate_neighbours():
                if neighbor.get_state_tuple() not in forward_visited:
                    forward_visited.add(neighbor.get_state_tuple())
                    forward_parents[neighbor.get_state_tuple()] = current_node
                    forward_queue.append(neighbor)
                    if neighbor.get_state_tuple() in backward_visited:
                        return reconstruct_path(forward_parents, backward_parents, neighbor)

        if backward_queue:
            current_node = backward_queue.popleft()
            for neighbor in current_node.generate_neighbours():
                if neighbor.get_state_tuple() not in backward_visited:
                    backward_visited.add(neighbor.get_state_tuple())
                    backward_parents[neighbor.get_state_tuple()] = current_node
                    backward_queue.append(neighbor)
                    if neighbor.get_state_tuple() in forward_visited:
                        return reconstruct_path(forward_parents, backward_parents, neighbor)

    return None

def reconstruct_path(forward_parents, backward_parents, meeting_node):
    path_from_start = []
    current = meeting_node
    while current is not None:
        path_from_start.append(current.get_state())
        current = forward_parents.get(current.get_state_tuple())

    path_from_start.reverse()

    path_from_goal = []
    current = meeting_node
    while current is not None:
        path_from_goal.append(current.get_state())
        current = backward_parents.get(current.get_state_tuple())

    full_path = path_from_start[:-1] + path_from_goal
    return path_from_start, path_from_goal, full_path