from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return[0]

        adj = [[] for _ in range(n)]
        degree = [0] * n


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            degree[u] += 1
            degree[v] += 1

        q = deque(i for i in range(n) if degree[i] == 1)

        while n>2:
            size = len(q)
            n -= size

            for _ in range(size):
                node = q.popleft()

                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)



        return list(q)



                

                
        