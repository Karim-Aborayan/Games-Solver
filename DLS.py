def dls(Problem, node, depth_limit, visited):
    if node.get_state_tuple() not in visited:
      visited.add(node.get_state_tuple())
    if node.get_state() == Problem.goal.get_state():
      return [node.get_state()]
    elif depth_limit == 0:
      return False
    else:
      for neighbour in node.generate_neighbours():
        if neighbour.get_state_tuple() not in visited:
          result = dls(Problem, neighbour, depth_limit - 1, visited)
          if result:
              return [node.get_state()] + result
      return False