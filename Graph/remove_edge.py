class Graph:
    def __init__(self):
        self.adjacency_list={}

    def addVertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
        return False
    
    def printGraph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex,":",self.adjacency_list[vertex])


custom_graph=Graph()
custom_graph.addVertex('A')
custom_graph.addVertex('B')
custom_graph.addVertex('C')
custom_graph.addEdge('A','B')
custom_graph.addEdge('A','C')
custom_graph.addEdge('B','C')
custom_graph.printGraph()
print('remove edge')
custom_graph.removeEdge('A','B')
custom_graph.printGraph()


