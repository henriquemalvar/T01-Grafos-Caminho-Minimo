def file_to_graph(file_name):
    file = open(file_name, 'r')
    graph_line, graph = list(), list()
    file.readline()
    for line in file:
        for value in line.split():
            graph_line.append(int(value))
        graph.append(graph_line.copy())
        graph_line.clear()
    file.close()
    return graph


def split_graph(graph):
    edges = [(i, j) for i, j, _ in graph]
    vertices = set()
    for i, j, in edges:
        vertices.update([i, j])
    return vertices, edges


def path_graph(pred, target):
    path = [target]
    current = pred[target]
    while current is not None:
        path.append(current)
        current = pred[current]
    return path[::-1]
