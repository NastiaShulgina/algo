from bellman_ford import Graph
if __name__ == "__main__":
    new_graph = Graph(4)

    new_graph.add_vertex(0, 1, 4)
    new_graph.add_vertex(1, 2, 4)
    new_graph.add_vertex(2, 0, -3)
    new_graph.add_vertex(2, 3, 6)
    new_graph.add_vertex(1, 3, -2)


    print(new_graph.bellman_ford(0))