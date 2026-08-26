import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):

        # Build graph
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        # Distance from k to every node
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        # Min heap
        heap = [(0, k)]

        while heap:

            current_distance, current_node = heapq.heappop(heap)

            # Ignore old/stale entry
            if current_distance > distance[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in graph[current_node]:

                new_distance = current_distance + weight

                if new_distance < distance[neighbor]:

                    distance[neighbor] = new_distance

                    heapq.heappush(
                        heap,
                        (new_distance, neighbor)
                    )

        # If any node is unreachable
        if float('inf') in distance[1:]:
            return -1

        # Last node to receive signal
        return max(distance[1:])