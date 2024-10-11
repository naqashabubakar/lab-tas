class Node:
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start to current node
        self.h = 0  # heuristic cost from current node to end
        self.f = 0  # total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    """
    A* pathfinding algorithm.

    Args:
    maze (list): A 2D list representing the maze.
    start (tuple): The starting position.
    end (tuple): The ending position.

    Returns:
    list: A list of positions representing the shortest path from start to end.
    """
    open_list = []
    closed_list = []
    start_node = Node(start, None)
    end_node = Node(end, None)
    open_list.append(start_node)

    while open_list:
        # Get the node with the lowest f score
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Check if we've reached the end
        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Check if the new position is within the maze boundaries
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) - 1) or node_position[1] < 0:
                continue

            # Check if the new position is not a wall
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        # Evaluate children
        for child in children:
            if child in closed_list:
                continue

            # Calculate the cost from start to child
            child.g = current_node.g + 1

            # Calculate the heuristic cost from child to end
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])  # Manhattan distance

            # Calculate the total cost
            child.f = child.g + child.h

            # Check if the child is already in the open list
            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            open_list.append(child)

    # If no path is found, return None
    return None

maze = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
start = (0, 0)  
end = (5, 6)   

path = astar(maze, start, end)
if path is not None:
    print("Path found:", path)
else:
    print("No path found.")