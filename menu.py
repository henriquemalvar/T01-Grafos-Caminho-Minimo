import time as time_module
from bellman_ford import bellman_ford
from Dijkstra import dijkstra
from floyd_warshall import floyd_warshall
from graph_method import file_to_graph, path_graph


def menu():
    file_name = input('Informe o nome do arquivo contendo o grafo: ')
    graph = file_to_graph(file_name)
    menu_options(graph)


def get_target():
    target = int(input('Digite o vertice de destino: '))
    return target


def get_source():
    source = int(input('Digite o vertice de origem: '))
    return source


def menu_options(graph):
    options = ['Dijkstra', 'Bellman Ford', 'Floyd Warshall', 'Sair']
    for i, option in enumerate(options):
        print(f'{i+1} - {option}')

    option = int(input('Selecione o algoritmo: '))
    if option == 1:
        option1(graph)
    elif option == 2:
        option2(graph)
    elif option == 3:
        option3(graph)
    elif option == 4:
        print('Saindo...')
        exit()
    else:
        print('Erro. Digite um numero entre 1 e 4')


def option1(graph):
    print('Algorítimo Selecionado: Dijsktra')
    source = get_source()
    target = get_target()
    start = time_module.time()
    dist, pred = dijkstra(graph, source)
    print('Caminho: ', path_graph(pred, target))
    print('Custo: ', dist[target])
    end = time_module.time()
    print('Tempo gasto: ', end-start)


def option2(graph):
    print('Algorítimo Selecionado: Bellman-Ford')
    source = get_source()
    target = get_target()
    start = time_module.time()
    dist, pred = bellman_ford(graph, source)
    print('Caminho: ', path_graph(pred, target))
    print('Custo: ', dist[source][target])
    end = time_module.time()
    print('Tempo gasto: ', end-start)


def option3(graph):
    print('Algorítimo Selecionado: Floyd-Warshall')
    source = get_source()
    target = get_target()
    start = time_module.time()
    dist, pred = floyd_warshall(graph)
    print('Caminho: ', path_graph(pred[source], target))
    print('Custo: ', dist[target])
    end = time_module.time()
    print('Tempo gasto: ', end-start)


if __name__ == '__main__':
    menu()
