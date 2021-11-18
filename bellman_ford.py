from graph_method import split_graph


def bellman_ford(G, s):
    V, _ = split_graph(G)
    num_vertices = len(V)
    dist, pred = initialization(num_vertices, s)
    for _ in range(num_vertices-1):
        for u, v, w in G:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
    return dist, pred


def initialization(num_vertices, s):
    dist = [float('inf') for i in range(num_vertices)]
    pred = [None for i in range(num_vertices)]
    dist[s] = 0
    return dist, pred
