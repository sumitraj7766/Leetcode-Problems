class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = [0] * numCourses

        def dfs(course):

            # Currently visiting → cycle
            if visited[course] == 1:
                return False

            # Already completely processed
            if visited[course] == 2:
                return True

            # Mark as currently visiting
            visited[course] = 1

            # Visit all dependent courses
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Completely processed
            visited[course] = 2

            return True

        # Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True