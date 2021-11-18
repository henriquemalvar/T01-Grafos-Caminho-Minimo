from graph_method import split_graph


def dijkstra(G, s):
    V, _ = split_graph(G)
    dist, pred = initialization(s, V)
    Q = V.copy()
    while len(Q) != 0:
        u = extract_minimum(dist, Q)
        Q.remove(u)
        adjacent = contains(G, u)
        for v, w in adjacent:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u

    return dist, pred


def extract_minimum(dist: list, Q):
    minimo = min([dist[i] for i in Q])
    for i in Q:
        if dist[i] == minimo:
            return i


def contains(G, u):
    adjacent = list()
    for i, j, w in G:
        if i == u:
            adjacent.append([j, w])
        elif j == u:
            adjacent.append([i, w])
    return adjacent


def initialization(s, V):
    number_vertices = len(V)
    dist = [float('inf') for i in range(number_vertices)]
    pred = [None for i in range(number_vertices)]
    dist[s] = 0
    return dist, pred
