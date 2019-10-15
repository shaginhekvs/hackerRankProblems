from heapq import heappush, heappop
from typing import TypeVar, Generic,List,Dict
import itertools
from functools import total_ordering

T = TypeVar('T')

# slower due to using total ordering, define lt, lte , gt , ge too for faster. 
@total_ordering
class PQTask(Generic[T]):
    def __init__(self,task:T )-> None:
        self.task : T  = task
        self.removed:bool = False
    def remove(self)-> None:
        self.removed = True
    def __hash__(self)-> int :
        return self.task.__hash__()
    def __eq__(self,other) -> bool:
        return ( self.__class__ == other.__class__ and \
                    self.task == other.task and \
                        self.removed == other.removed)
    def __lt__(self,other)-> bool:
        return self.__lt__(other)


class PriorityQueue(Generic[T]):
    def __init__(self):
        self.pq: List[List[float,int,PQTask[T]]] = []                         # list of entries arranged in a heap
        self.entry_finder:Dict[PQTask,List[float,int,PQTask[T]]] = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count
        self.length = 0

    def add(self,task:PQTask[T], priority=0.0)-> None:
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)
        self.length += 1

    def remove(self,task:PQTask[T])-> None:
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1].remove()
    
    def pop(self)->PQTask[T]:
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if not task.removed :
                del self.entry_finder[task]
                return task
            self.length -= 1
        #raise KeyError('pop from an empty priority queue')


import unittest

class TestPQ(unittest.TestCase):

    def testModuleTest(self):
        pq1 = PriorityQueue[str]()
        pq1.add(PQTask[str]('hello'),1.0)
        pq1.add(PQTask[str]('hello2'),2.0)
        pq1.add(PQTask[str]('hello3'),2.0)
        pq1.remove(PQTask[str]('hello'))
        getTop: PQTask[str] = pq1.pop()
        self.assertEqual(getTop.task , 'hello2')
        getTop = pq1.pop()

        self.assertEqual(getTop.task , 'hello3')


if __name__ == '__main__':
    TestPQ().testModuleTest()
    unittest.main()
