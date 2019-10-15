# problem at https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs
from typing import TypeVar, Generic,List,Dict,Set,Union,Tuple
T = TypeVar('T')
from queue import Queue
class Graph(Generic[T]):

    inf = float('inf')

    def __init__(self,n:int)-> None:
        self.n = n
        self.graph_dict:Dict[int,Set[Tuple[int,T]]] = {}
        self.dist = [-1]*n
        self.visited:List[bool] = [False]*n
        
    def connect(self,x:int,y:int,weight:T=6,undirected:bool=True)-> None:
        if(x not in self.graph_dict.keys()):
            self.graph_dict[x] = set()
        self.graph_dict[x].add((y,weight))

        if(undirected):
            if(y not in self.graph_dict.keys()):
                self.graph_dict[y] = set()
            self.graph_dict[y].add((x,weight))
        
    

    def find_all_distances(self,source:int)->None:
        
        q = Queue()
        zero_val:T = 0
        self.dist[source] = zero_val
        q.put(source)
        
        while(not q.empty()):
            element_top = q.get()
            self.visited[element_top]=True
            dist_until_ele_top:T = self.dist[element_top]
            for neighbour,weight in self.graph_dict[element_top]:
                if(self.visited[neighbour]):continue
                self.dist[neighbour] = dist_until_ele_top + weight
                q.put(neighbour)
        
        
        print(' '.join([str(dist) for dist in self.dist if dist != 0]).strip())


if __name__=="__main__":
    g = Graph[int](4)
    g.connect(0,1,6)
    g.connect(0,2,6)
    g.find_all_distances(0)
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1) 
        s = int(input())
        graph.find_all_distances(s-1)

