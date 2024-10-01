from binary_heap import BinaryHeap
from node import Node
import time

class EarlyAstar:
    def __init__(self, initial_state, heuristic, weight=1):
        self.expansions = 0
        self.generated = 0
        self.initial_state = initial_state
        self.weight = weight
        self.heuristic = heuristic
        self.solution = None
        self.U = float('inf')  # Valor de U inicial (infinito)

    def search(self):
        self.start_time = time.process_time()
        '''
        COMPLETAR
        '''        
        self.end_time = time.process_time()
        return None