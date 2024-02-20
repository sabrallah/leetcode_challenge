class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build Graph
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        # Step 2: Detect Cycle
        def hasCycle(course, visited, visiting):
            visited[course] = True
            visiting[course] = True

            for neighbor in graph[course]:
                if not visited[neighbor]:
                    if hasCycle(neighbor, visited, visiting):
                        return True
                elif visiting[neighbor]:
                    return True

            visiting[course] = False
            return False

        # Step 3: Iterate Through Courses
        visited = [False] * numCourses
        visiting = [False] * numCourses
        for course in range(numCourses):
            if not visited[course]:
                if hasCycle(course, visited, visiting):
                    return False

        # Step 4: Return True
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        