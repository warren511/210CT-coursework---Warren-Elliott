class graph:
    
    def __init__(self):
        self.vertexDictionary={}
        
    def add_vertex(self,number):
        if number not in self.vertexDictionary:
            self.vertexDictionary[number]=[]
        
    def add_edge(self,number,edge):
        self.vertexDictionary[number].append(edge)
        self.vertexDictionary[edge].append(number)

    def display (self):
        for key in self.vertexDictionary:
            print(key, " is connected to ", self.vertexDictionary[key])

    def depth_first_search(self, vertex):
        self.visited = []
        self.stack= []
        self.stack.append(vertex)

        while self.stack != []:
            u = self.stack.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.vertexDictionary[u]:
                    self.stack.append(edge)
                    print(self.visited)
                
                file = open("Depthfirstresult.txt", "w")
                file.write(str(self.visited))
                file.close()
        return(self.visited)

    def breadth_first_search(self,vertex):
        self.queue = []
        self.visited = []
        self.queue.insert(0, vertex)

        while self.queue != []:
            u = self.queue.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.vertexDictionary[u]:
                    self.queue.insert(0, edge)
                    print (self.visited)

                file = open("breadthfirstresult.txt", "w")
                file.write(str(self.visited))
                file.close()
        return(self.visited)

if __name__=="__main__":
    g=graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
    g.add_vertex(8)
    g.add_vertex(9)
    g.add_vertex(10)

    g.add_edge(2,6)
    g.add_edge(4,6)
    g.add_edge(7,10)
    g.add_edge(7,9)
    g.add_edge(6,8)
    g.add_edge(10,3)
    g.add_edge(9,1)
    g.add_edge(5,7)
    g.add_edge(2,3)
    g.add_edge(3,5)
    g.DFS(4)
    g.BFS(4)
    g.display()

    
    
        
