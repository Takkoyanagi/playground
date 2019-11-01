def djikstra(graph, start, goal):
    """ finds the minimal distance between two vertices
    graph = list/dict of initial vertices, edges, and weights
    """

    #Initialization of dictionaries/lists
    visited = {}
    pred = {}
    infin = int(99999)
    path = []
    unvisited = graph

    # set all verticies to inf and set 0 for start
    for i,_ in graph.items():
        visited[i] = infin
    
    visited['s'] = 0

    # traverse the graph
    while unvisited:
        min_node = None #initialize
        for node in unvisited:
            if min_node is None:
                min_node = node # only for first time
            elif visited[node] < visited[min_node]:
                print(node, visited[node], visited[min_node], min_node)
                min_node = node # update the vertex to min node value
        # update weights from graph
        for childnode, weight in graph[min_node].items():
            if weight + visited[min_node] < visited[childnode]:
                visited[childnode] = weight + visited[min_node]
                pred[childnode] = min_node
        unvisited.pop(min_node)

    # get the shortest path
    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = pred[current_node]
        except KeyError:
            print('path not reachable')
            break
    path.insert(0,start)
    if visited[goal] != infin:
        print('shortest distance ' + str(visited[goal]))
        print('And the path is ' + str(path))


graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
djikstra(graph, 's', 't')
