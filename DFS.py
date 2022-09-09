graph = {
    'F' : ['B' , 'G'],
    'B' : ['A' , 'D'],
    'G' : ['I'],
    'A' : [],
    'D' : ['C' , 'E'],
    'I' : ['H'],
    'C' : [],
    'E' : [],
    'H' : []
}
visited = []
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'F')