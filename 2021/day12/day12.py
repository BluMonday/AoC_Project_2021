def dfs(graph: dict, visited: set, vertex: str):
    global current_path
    if vertex == 'end':
        return
    if vertex not in visited:
        visited.add(vertex)
        for adj_ver in graph[vertex]:
            dfs(graph, visited, adj_ver)

if __name__ == '__main__':
    f = open('test.txt')
    puzzle_input = f.read().split('\n')

    graph = dict()

    for line in puzzle_input:
        c1, c2 = line.split('-')
        if c1 not in graph:
            graph[c1] = c2.split(' ')
        else:
            graph[c1] = graph[c1] + c2.split(' ')
        if c2 not in graph:
            graph[c2] = c1.split(' ')
        else:
            graph[c2] = graph[c2] + c1.split(' ')

    visited = set()
    paths = []
    current_path = ['start']
    dfs(graph, visited, 'start')

    print('done')