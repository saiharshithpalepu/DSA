from collections import deque
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
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for otherVertex in self.adjacency_list[vertex]:
                self.adjacency_list[otherVertex].remove(vertex)
            del self.adjacency_list[vertex]

    def printGraph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex,':',self.adjacency_list[vertex])

    def dfs(self,vertex):
        visited=set()
        stack=[vertex]
        while stack:
            current_vertex=stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)





custom_graph=Graph()
custom_graph.addVertex('A')
custom_graph.addVertex('B')
custom_graph.addVertex('C')
custom_graph.addVertex('D')
custom_graph.addVertex('E')
custom_graph.addEdge('A','B')
custom_graph.addEdge('B','E')
custom_graph.addEdge('A','C')
custom_graph.addEdge('C','D')
custom_graph.addEdge('D','E')
custom_graph.printGraph()
custom_graph.dfs('A')

        