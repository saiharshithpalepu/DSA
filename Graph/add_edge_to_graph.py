class Graph:
    def __init__(self):
        self.adjacency_list={}

    def addvertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex,':',self.adjacency_list[vertex])

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
custom_graph=Graph()
custom_graph.addvertex('A')
custom_graph.addvertex('B')
custom_graph.addEdge('A','B')
custom_graph.printGraph()