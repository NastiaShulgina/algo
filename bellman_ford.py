class Graph:

    def __init__(self, vertexes_amount):
        self.vertexes_amount = vertexes_amount
        self.graph = []

    def add_vertex(self, first_node, second_node, distance_between):
        self.graph.append([first_node, second_node, distance_between])

    def print_solution(self, distance):
        print("Vertex distance from origin")

        for i in range(self.vertexes_amount):
            print("{0}\t\t{1}".format(i, distance[i]))

    def bellman_ford(self, origin):
        distance = [float("Inf")] * self.vertexes_amount
        distance[origin] = 0

        for _ in range(self.vertexes_amount - 1):
            for first_node, second_node, distance_between in self.graph:
                if distance[first_node] != float("Inf") and distance[first_node] + distance_between < distance[second_node]:
                    distance[second_node] = distance[first_node] + distance_between
        for first_node, second_node, distance_between in self.graph:

            if distance[first_node] != float("Inf") and distance[first_node] + distance_between < distance[second_node]:
                print("Graph contains a negative weight cycle")
                return None

        self.print_solution(distance)
        return distance