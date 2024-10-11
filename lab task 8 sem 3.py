def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    """
    Recursively calculates the best move using the Minimax algorithm.

    Args:
    - depth (int): Current depth of the tree.
    - node_index (int): Index of the current node.
    - maximizing_player (bool): Whether it's the maximizing player's turn.
    - values (list): List of values for each node.
    - alpha (float): Best possible score for the maximizing player.
    - beta (float): Best possible score for the minimizing player.

    Returns:
    - The best possible score for the current player.
    """

    # Base case: If the depth is 3, return the value of the current node.
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        # Initialize max_eval to negative infinity.
        max_eval = float('-inf')

        # Iterate over the child nodes.
        for i in range(2):
            # Recursively call minimax for the child node.
            eval = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)

            # Update max_eval and alpha.
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            # Prune the tree if beta is less than or equal to alpha.
            if beta <= alpha:
                break

        return max_eval
    else:
        # Initialize min_eval to positive infinity.
        min_eval = float('inf')

        # Iterate over the child nodes.
        for i in range(2):
            # Recursively call minimax for the child node.
            eval = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)

            # Update min_eval and beta.
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            # Prune the tree if beta is less than or equal to alpha.
            if beta <= alpha:
                break

        return min_eval


# Example usage:
values = [3, 5, 6, 9, 1, 2, 0, -1]
result = minimax(0, 0, True, values, float('-inf'), float('inf'))
print("Best possible score:", result)