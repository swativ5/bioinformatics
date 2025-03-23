"""
EulerianCycle(Graph)
    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
        Cycle ← Cycle’
    return Cycle

Code Challenge: Solve the Eulerian Cycle Problem.
         Input: The adjacency list of an Eulerian directed graph.
         Output: An Eulerian cycle in this graph.

Sample Input:
0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6

Sample Output:
6 8 7 9 6 5 4 2 1 0 3 2 6
"""

def formCycle(graph, node):
    cycle = []
    stack = [node]
    visited_edges = set()  # Track visited edges instead of just nodes

    while stack:
        cnode = stack[-1]

        if cnode not in graph or not graph[cnode]:
            # Dead end, backtrack
            stack.pop()
            continue

        next_node = graph[cnode].pop(0)  # Take one of its neighbors

        if (cnode, next_node) in visited_edges:
            continue  # Skip already visited edges

        visited_edges.add((cnode, next_node))
        stack.append(next_node)

        if next_node == node:
            cycle = stack[:]
            break  # Stop at cycle formation

    # Find unexplored edges
    unexplored = []
    for cnode in cycle:
        if cnode in graph:
            for neighbor in graph[cnode]:
                if (cnode, neighbor) not in visited_edges:
                    unexplored.append(neighbor)

    return cycle, unexplored

graph = {0: [3],
1: [0],
2: [1, 6],
3: [2],
4: [2],
5: [4],
6: [5, 8],
7: [9],
8: [7],
9: [6]}

print(formCycle(graph, 0))

# def EulerianCycle(graph):
#     stack = [0]
#     while len(stack) != 0:
#         node = stack.pop()
