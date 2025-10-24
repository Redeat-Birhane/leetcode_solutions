class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Each node will store up to 2 distinct arrival times
        arrival_times = [[] for _ in range(n + 1)]

        # Step 3: Min-heap (time, node)
        heap = [(0, 1)]  # start from node 1 at time 0

        while heap:
            curr_time, node = heapq.heappop(heap)

            # Record the arrival time if < 2 and unique
            if len(arrival_times[node]) >= 2:
                continue
            if arrival_times[node] and arrival_times[node][-1] == curr_time:
                continue

            arrival_times[node].append(curr_time)

            # If we reached destination and this is the second arrival → answer
            if node == n and len(arrival_times[node]) == 2:
                return curr_time

            # Step 4: Traverse neighbors
            for nei in graph[node]:
                next_time = curr_time

                # Wait if light is red at this moment
                cycle = next_time // change
                if cycle % 2 == 1:  # currently red
                    next_time = (cycle + 1) * change

                # Travel to neighbor
                next_time += time

                heapq.heappush(heap, (next_time, nei))
