from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if(numCourses == 0 or numCourses == 1):
            return True

        g = Graph(numCourses, prerequisites)

        return g.DFS()
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
 
class Graph:
    def __init__(self, vertices, listOfEdges):
        self.graph = defaultdict(list)
        self.V = vertices

        for x in listOfEdges:
            self.graph[x[0]].append(x[1])
            
    def DFS(self):
        """
        0 for not visited
        1 for still on stack
        2 for already visited
        """
        visited = [0]*self.V


        for i in range(self.V):
            if visited[i] != 0:
                continue

            test = self.DFSHelper(i,visited)
            if test == False:
                return False
        return True

    def DFSHelper(self, v, visited):
        visited[v] = 1

        for vertice in self.graph[v]:
            if visited[vertice] == 0:
                self.DFSHelper(vertice, visited)

            if visited[vertice] == 1:
                return False

        visited[v] = 2
        return True

s = Solution()
print(s.canFinish(2,[[1,0]]))
                












       
