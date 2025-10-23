import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))  
        
       
        heap = [(-1.0, start)]
        maxProb = [0.0] * n
        maxProb[start] = 1.0
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob  
            
           
            if node == end:
                return prob
            
            for nei, edgeProb in graph[node]:
                newProb = prob * edgeProb
                if newProb > maxProb[nei]:
                    maxProb[nei] = newProb
                    heapq.heappush(heap, (-newProb, nei))
        
        return 0.0
