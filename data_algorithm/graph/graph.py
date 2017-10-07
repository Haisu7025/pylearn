#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Graph:
    # 邻接矩阵实现图类
    def __init__(self, maps=[], nodenum=0, edgenum=0, isderected=False):
        self.map = maps
        self.nodenum = nodenum
        self.edgenum = edgenum
        self.isderected = isderected

    def get_nodenum(self):
        self.nodenum = len(self.map)
        return self.nodenum

    def get_edgenum(self):
        self.edgenum = 0
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                if self.map[i][j] == 1:
                    self.edgenum = self.edgenum + 1
        if self.isderected:
            # 有向图
            pass
        else:
            # 无向图
            self.edgenum = self.edgenum / 2
        return self.edgenum

    def insert_node(self):
        for i in range(self.nodenum):
            self.map[i].apppend[0]
        self.nodenum = self.nodenum + 1
        self.map.append([0] * self.nodenum)

    def delete_node(self, x):
        for i in range(self.nodenum):
            if self.map[i][x] == 1:
                self.map[i][x] = 0
                self.edgenum = self.edgenum - 1
            if self.map[x][i] == 1:
                self.map[x][i] = 0
                self.edgenum = self.edgenum - 1

    def add_edge(self, x, y):
        if self.map[x][y] == 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def del_edge(self, x, y):
        if self.map[x][y] == 1:
            self.map[x][y] = 0
            self.edgenum = self.edgenum - 1

    def broadth_first_search(self, func):
        def BFS(self, i):
            # TODO:operate node i
            func()
            pass

            visited[i] = 1
            for k in range(self.nodenum):
                if self.map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] == 0:
                BFS(self, i)

    def depth_first_search(self, func):
        def DFS(self, i, queue):
            # TODO:operate node i
            func()
            pass

            queue.append(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.nodenum):
                    if self.map[w][k] == 1 and visited[k] == 0:
                        DFS(self, k, queue)

        visited = [0] * self.nodenum
        queue = []
        for i in range(self.nodenum):
            DFS(self, i, queue)

    def Dijkstra(self, x):
        # dijkstra
        def find_nearest_node(self, dist, checked):
            node_nearest = -1
            dist_min = 1000
            for node in range(self.nodenum):
                if node not in checked and dist[node] < dist_min:
                    dist_min = dist[node]
                    node_nearest = node
            return [node_nearest, dist_min]

        def get_dist(self, node):
            dist = [0] * self.nodenum
            for i in range(self.nodenum):
                dist[i] = self.map[node][i]
            return dist

        paths = [x] * self.nodenum
        S = [x]
        S_dist = get_dist(self, S[len(S) - 1])
        while len(S) != self.get_nodenum():
            [nn, dm] = find_nearest_node(self, S_dist, S)
            S.append(nn)
            nn_dist = get_dist(self, nn)
            for node in range(self.nodenum):
                if node not in S:
                    if S_dist[node] > nn_dist[node] + dm:
                        S_dist[node] = nn_dist[node] + dm
                        paths[node] = nn

        return [S_dist, paths]

    def d_find_shortest(self, x, y):
        [dist, paths] = self.Dijkstra(x)
        node = y
        path = []
        while node != x:
            path.append(node)
            node = paths[node]
        path.append(x)
        path.reverse()
        return [path, dist[y]]

    def Floyd(self):
        D = [[0 for i in range(self.nodenum)] for i in range(self.nodenum)]
        P = [[0 for i in range(self.nodenum)] for i in range(self.nodenum)]
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                D[i][j] = self.map[i][j]
                if D[i][j] > 0:
                    P[i][j] = i

        for index in range(self.nodenum):
            for i in range(self.nodenum):
                for j in range(self.nodenum):
                    if D[i][j] > D[i][index] + D[index][j]:
                        D[i][j] = D[i][index] + D[index][j]
                        P[i][j] = index

        return [D, P]

    def f_find_shortest(self, x, y):
        [D, P] = self.Floyd()
        dist = D[x][y]
        node = y
        path = []
        while node != x:
            path.append(node)
            node = P[x][node]
        path.reverse()
        return [path, dist]
