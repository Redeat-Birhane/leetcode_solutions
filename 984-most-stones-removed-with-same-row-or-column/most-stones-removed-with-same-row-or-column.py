class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * len(stones)
        components = 0

        def bfs(start):
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append(neighbour)

    
        for i in range(len(stones)):
            if not visited[i]:
                components += 1
                bfs(i)

        return len(stones) - components
