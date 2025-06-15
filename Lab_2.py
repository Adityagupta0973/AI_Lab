# Water Jug problem
def water_jug_dfs(capacity1, capacity2, target):
    visited = set() # To track visited states
    path = []       # To store the solution path

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        
        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        if jug1 == target or jug2 == target:
            return True

        # Fill Jug 1
        if dfs(capacity1, jug2):
            return True
        # Fill Jug 2
        if dfs(jug1, capacity2):
            return True
        # Empty Jug 1
        if dfs(0, jug2):
            return True
        # Empty Jug 2
        if dfs(jug1, 0):
            return True
        # Pour water from Jug 1 into Jug 2
        if dfs(max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)):
            return True
        # Pour water from Jug 2 into Jug 1
        if dfs(min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))):
            return True

        path.pop()
        return False
    dfs(0, 0)
    return path

capacity1 = 3  
capacity2 = 5  
target = 4     

solution = water_jug_dfs(capacity1, capacity2, target)
if solution:
    print("Solution:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")

import matplotlib.pyplot as plt
import networkx as nx

def visualize_dfs_solution(solution):
    G = nx.DiGraph()

    # Add the nodes and edges based on the DFS solution path
    for i in range(len(solution) - 1):
        G.add_edge(solution[i], solution[i + 1])

    pos = nx.spring_layout(G)  # Position the nodes for visualization

    plt.figure(figsize=(7, 5))

    # Draw the graph with nodes and labels
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color='black', width=2)

    plt.title("Water Jug Problem")
    plt.show()

if solution:
    visualize_dfs_solution(solution)