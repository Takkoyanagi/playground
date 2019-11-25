graph = [[1, 0], [0, 1]]


def numIslands(graph):
    count = 0
    if not graph:
        return count

    for rows in range(len(graph)):
        for cols in range(len(graph[0])):
            if graph[rows][cols] == 1:
                count += 1
                dfs(graph, rows, cols)
    return count


def dfs(graph, rows, cols):
    if (rows < 0) or (cols < 0) or (rows >= len(graph)) or (cols >= len(graph[0])) or (graph[rows][cols] != 1):
        return
    else:
        graph[rows][cols] = '#'
        dfs(graph, rows+1, cols)
        dfs(graph, rows-1, cols)
        dfs(graph, rows, cols+1)
        dfs(graph, rows, cols-1)


print(numIslands(graph))
