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
