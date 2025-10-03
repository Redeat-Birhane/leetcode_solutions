class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            visited = set()
            dfs(i)
            if len(visited) == n:
                return i

        return -1
        