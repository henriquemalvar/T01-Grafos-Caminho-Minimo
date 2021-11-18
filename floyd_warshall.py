from graph_method import split_graph


def floyd_warshall(G):
    V, _ = split_graph(G)
    number_vertices = len(V)
    dist, pred = initialization(G, number_vertices)
    for k in range(number_vertices):
        for i in range(number_vertices):
            for j in range(number_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    return dist, pred


def initialization(G, number_vertices):
    dist_line = [float('inf') for i in range(number_vertices)]
    dist = [dist_line.copy() for i in range(number_vertices)]
    pred_line = [None for i in range(number_vertices)]
    pred = [pred_line.copy() for i in range(number_vertices)]
    for i in range(number_vertices):
        dist[i][i] = 0
    for i, j, w in G:
        dist[i][j] = w
        pred[i][j] = i
    return dist, pred
