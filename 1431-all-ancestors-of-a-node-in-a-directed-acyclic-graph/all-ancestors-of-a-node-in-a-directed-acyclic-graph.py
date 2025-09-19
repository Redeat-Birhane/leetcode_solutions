class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent_graph = defaultdict(list)
        answer = [[]] * n
        for u, v in edges:
            parent_graph[v].append(u)
        def dfs(i):
            if not parent_graph[i]:
                return 

            for parent in parent_graph[i]:
                if parent not in visited:
                    visited.add(parent)
                    dfs(parent)

        for i in range(n):
            visited = set()
            if parent_graph[i]:
                dfs(i)
                answer[i] = list(visited)
                answer[i].sort()

        return answer
       
       
       
      