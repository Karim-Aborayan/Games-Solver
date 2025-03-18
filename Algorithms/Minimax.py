from math import log2

def minimax(depth, node_index, is_maximizing_player, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing_player:
        left_child = minimax(depth + 1, node_index * 2, False, scores, max_depth)
        right_child = minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        return max(left_child, right_child)
    else:
        left_child = minimax(depth + 1, node_index * 2, True, scores, max_depth)
        right_child = minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        return min(left_child, right_child)