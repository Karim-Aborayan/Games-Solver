import heapq

def best_first_search(Problem):
    queue = []
    heapq.heappush(queue, (Problem.start.manhattan_distance(Problem.goal), Problem.start, [Problem.start.get_state()]))
    visited = set()
    
    while queue:
        _, current, path = heapq.heappop(queue)
        
        if current.get_state() == Problem.goal.get_state():
            return path
        
        visited.add(current.get_state_tuple())
        
        for neighbour in current.generate_neighbours():
            if neighbour.get_state_tuple() not in visited:
                heapq.heappush(queue, (neighbour.manhattan_distance(Problem.goal), neighbour, path+[neighbour.get_state()]))
    
    return None