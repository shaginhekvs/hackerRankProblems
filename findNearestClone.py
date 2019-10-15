
from pq import PriorityQueue,PQTask
from itertools import combinations

def run_dikstra(num_vertices,graph,source_id, destination_id):
    pq_dikstra = PriorityQueue[int]()
    inf = float('inf')
    graph_nodes = num_vertices
    dist = [inf]*graph_nodes
    dist[source_id] = 0.0
    pq_dikstra.add(PQTask[int](source_id),dist[source_id])
    
    while(pq_dikstra.length>0):
        source = pq_dikstra.pop()
        if(source):
            source = source.task
        else:
            break
        if(source == destination_id):
            break
        for neighbour,weight in graph[source]:
            updated_weight = dist[source]+weight
            if( updated_weight< dist[neighbour]):
                dist [neighbour ] = updated_weight
                pq_dikstra.add(PQTask[int](neighbour),updated_weight)
        
    return dist[destination_id]

    

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here

    graph = {}
    inf = float('inf')
    dist = [0.0]*graph_nodes

    for i,j in zip(graph_from,graph_to):
        if( i-1 not in graph):
            graph[i-1] = set()
        if(j-1 not in graph):
            graph[j-1] = set()        
        graph[i-1].add((j-1,1))
        graph[j-1].add((i-1,1))


    same_color_indexes = [index for index,id in enumerate(ids) if id == val ]
    print(graph)
    if(len(same_color_indexes)<=1):
        return -1
    print(same_color_indexes)
    pq_dikstra = PriorityQueue[int]()
    min_dist = inf
    for index1,index2 in combinations(same_color_indexes,2):
        cur_dist = run_dikstra(graph_nodes,graph,index1,index2)
        if(cur_dist < min_dist): min_dist = cur_dist
    return int(min_dist)



    
    

def read_input ( filename):
    with open(filename) as f:
        graph_nodes, edge_numbers = map(lambda x: int(x),f.readline().split())
        edges_to = []
        edges_from = []
        for i in range(edge_numbers) :
            from_,to_ =  map(lambda x: int(x),f.readline().split())
            edges_to.append(to_)
            edges_from.append(from_)
        ids = list(map(lambda x: int(x),f.readline().split()))
        val = int(f.readline())
    return [graph_nodes, edges_to, edges_from, ids, val]


import unittest

class TestFNC(unittest.TestCase):

    
    def testModuleTest(self):
        graph_nodes = 5 
        graph_from = [1,1,4]
        graph_to = [2,3,2]
        ids = [1,2,3,4]
        val = 2
        vals = [graph_nodes, graph_to, graph_from, ids, val]
        ans = findShortest(*vals)
        self.assertEqual(ans,-1)


if __name__ == '__main__':
    unittest.main()

