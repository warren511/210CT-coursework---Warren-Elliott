"""
CLASS VERTEX
  INITIALISE(number)
  name<-number
  adjacent<-empty list
  
  ADD_ADJACENT(value)
  IF value not in adjacent
     append value to adjacent
  ENDIF

CLASS GRAPH
  INITIALISE
    vertexDictionary<-{}
    list=[]

  ADD_VERTEX(number)
  IF number not in vertexDictionary
     vertexDictionary[number]=[]
  ENDIF

  ADD_EDGE(number,edge)
    append edge to vertexDictionary[number]
    append number to vertexDictionary[edge]
 DISPLAY
    FOR KEY in vertexDictionary
       OUTPUT(key is connected to key from vertexDictionary

 INITIALISE PROGRAM
 g<-graph()
 add vertex
 add edge
 display()

"""
class vertex:
    def __init__(self, number):
        self.name=number
        self.adjacent=list()

    def add_adjacent(self, value):
        if value not in self.adjacent:
            self.adjacent.append(value)
            
class graph:

    def __init__(self):
        self.vertexDictionary={}
        self.list=[]

    def add_vertex(self,number):
        if number not in self.vertexDictionary:
            self.vertexDictionary[number]=[]
        
    def add_edge(self,number,edge):
        self.vertexDictionary[number].append(edge)
        self.vertexDictionary[edge].append(number)

    def display (self):
        for key in self.vertexDictionary:
            print(key, " is connected to ", self.vertexDictionary[key])

    
        
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
    g.display()

    
        
