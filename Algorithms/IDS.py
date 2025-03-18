from Algorithms.DLS import dls

def ids(Problem):
    depth_limit = 0
    while True:
        result = dls(Problem, Problem.start, depth_limit, set())
        if result:
            return result, depth_limit
        depth_limit += 1