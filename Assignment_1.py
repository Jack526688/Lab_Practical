def bfsd(graph, root):
    visited = set()
    queue = []
    queue.append(root)
    queue.extend(graph[root])
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, "", end="")
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)


def dfs(visited, graph, node):

    if node not in visited:
        print (node, "", end="")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


visited = set()
graph = {0: [1, 2, 3], 1: [0], 2: [0, 3, 4, 5], 3: [0, 2], 4: [2, 5], 5: [2, 4]}
print('bfs')
bfsd(graph, 3)
print("\n\ndfs")
dfs(visited, graph, 2)