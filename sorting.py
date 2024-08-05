#remember graphs have different characteristics
# Cyclic/Acylic- Cylic contains at least one cycle
# Acylic - contains no cycles 
#Example- A DAG(Directed Acylic Grpah) is a special graph where no vertex can reach itself
    
# Weighted / Unweighted 
# A weighted graph usually has value asscoiated to it 
#such as the famous DJistrka graph to findin the least cost path 
#usually used for airlines or anything related in terms of cost
#UNWEIGHTED graph has no cost to when spanning a graph
#graphs like dfs and bfs can be unweighted since sometimes it doesnt have cost assciated to it only how close it is or shotest path possible

#DIRECTED AND UNDIRECTED !!!
#DIRECTED graphs are graphs that only allow one path from node to node 
#Undirected graphs allow you to go from node to node from anywhere usually allowing cycles to happen

#Graph introduction

# Making a graph class

class Graph():
    
    #init the constructor for the graph 
    def _init_(self):
        #init the number of nodes to zero
        self.number_of_nodes = 0
        #use a dictionary to help with adjaceny list
        #this is to show the nodes that are near each other 
        self.adjancey_list = {}

    def insert_node (self,data):
        #condtional check if data is in adjancey list 
        if data not in self.adjancey_list:
            #if true it will add to the list and increment the number of nodes
            self.adjaceny_list[data] = []
            self.number_of_nodes += 1
            return
        
        #method that takes self and check for edges or existing edges
    def insert_edge (self,vertex1,vertex2):
        if vertex2 not in self.adjancey_list[vertex1]:
            self.adjancey_list[vertex1].append(vertex2)
            self.adjaceny_list[vertex2].append(vertex1)
            return
        return "Edge already exists"
    
    #Printing all the nodes 
    
    #make a method 
    def show_connections(self):
        #make a for loop that iterates through the whol adjaceny list
        for node in self.adjacency_list:
            print(f'{node}) -->> {"".join(map(str,self.adjacency_list[node]))}')
            
    
 
 
 
 
my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2,1)