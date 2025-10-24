class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for f, t, w in edges:
            graph[f].append((t, w))
            graph[t].append((f, w))

        def bfs(node):
            dist = [float('inf')] * n
            dist[node] = 0
            heap = [(0, node)]  
            while heap:
                curr_dis, city = heapq.heappop(heap)
                if curr_dis > dist[city]:
                    continue
                for neighbour, w in graph[city]:
                    new_dist = curr_dis + w
                    if new_dist < dist[neighbour] and new_dist <= distanceThreshold:
                        dist[neighbour] = new_dist
                        heapq.heappush(heap, (new_dist, neighbour))
           
            return sum(1 for d in dist if 0 < d <= distanceThreshold)

        ans, minn = -1, float('inf')
        for i in range(n):
            reachable = bfs(i)
            if reachable <= minn:
                minn = reachable
                ans = i  

        return ans
