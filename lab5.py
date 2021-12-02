import sys

source = 1
sink = 6

class Edge:
    def __init__(self, source, sink, weight, visited):
        self.source = source
        self.sink = sink
        self.weight = weight
        self.visited = visited

graph = []

def extract_data():
    edge = Edge(1,2,16, False)
    graph.append(edge)
    edge = Edge(2,4,12, False)
    graph.append(edge)
    edge = Edge(4,6,20, False)
    graph.append(edge)
    edge = Edge(1,3,13, False)
    graph.append(edge)
    edge = Edge(3,2,4, False)
    graph.append(edge)
    edge = Edge(3,5,14, False)
    graph.append(edge)
    edge = Edge(5,6,4, False)
    graph.append(edge)
    edge = Edge(4,3,9, False)
    graph.append(edge)
    edge = Edge(5,4,7, False)
    graph.append(edge)
        

class Route:
    def __init__(self, min_weight, found):
        self.min_weight = min_weight
        self.found = found


def dfs(source, sink, graph, route):

    if source == sink:
        route.found = True
    else:
        for edge in graph:
            if source == edge.source and not edge.visited:
                edge.visited = True 
                current_weight = route.min_weight
                route.min_weight = min(route.min_weight, edge.weight)
                dfs(edge.sink, sink, graph, route)
                if route.found:
                    edge.weight -= route.min_weight
                    if edge.weight == 0:
                        graph.remove(edge)
                    return
                else:
                    route.min_weight = current_weight



def main():

    extract_data()
    max_capacity = 0

    while True:
        route = Route(sys.maxsize, False)
        for edge in graph:
            edge.visited = False

        dfs(source, sink, graph, route)
        if route.found:
            max_capacity += route.min_weight
            print(route.min_weight)
        else:
            break
    
    print(max_capacity)


if __name__ == "__main__":
    main()