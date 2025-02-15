from math import log2

def alpha_beta(depth, node_index, is_maximizing_player, scores, max_depth, alpha=float('-inf'), beta=float('inf')):
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing_player:
        left_child = alpha_beta(depth + 1, node_index * 2, False, scores, max_depth, alpha, beta)
        right_child = alpha_beta(depth + 1, node_index * 2 + 1, False, scores, max_depth, alpha, beta)

        best_value = max(left_child, right_child)

        alpha = max(alpha, best_value)

        if beta <= alpha:
            return best_value

        return best_value
    else:
        left_child = alpha_beta(depth + 1, node_index * 2, True, scores, max_depth, alpha, beta)
        right_child = alpha_beta(depth + 1, node_index * 2 + 1, True, scores, max_depth, alpha, beta)

        best_value = min(left_child, right_child)

        beta = min(beta, best_value)

        if beta <= alpha:
            return best_value

        return best_value