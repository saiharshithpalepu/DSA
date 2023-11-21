class Graph:
    def __init__(self):
        self.adjacency_list={}

    def addVertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex,":",self.adjacency_list[vertex])

custom_graph=Graph()
custom_graph.addVertex('a')
custom_graph.printGraph()