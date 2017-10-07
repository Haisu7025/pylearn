#!/usr/bin/python
# -*- coding: UTF-8 -*-
import graph
people_num = 3
wolf_num = 3

# construct graph
# [left shore people, left shore wolf, ship position]


def judge(node1, node2):
    if node1[0] == node2[0]:
        if (node1[1] - node2[1] == 2 or node1[1] - node2[1] == 1) and node1[2] == 0 and node2[2] == 1:
            return 1
        elif (node1[1] - node2[1] == -2 or node1[1] - node2[1]) == -1 and node1[2] == 1 and node2[2] == 0:
            return 1
    elif node1[1] == node2[1]:
        if (node1[0] - node2[0] == 2 or node1[0] - node2[0] == 1) and node1[2] == 0 and node2[2] == 1:
            return 1
        elif (node1[0] - node2[0] == -2 or node1[0] - node2[0]) == -1 and node1[2] == 1 and node2[2] == 0:
            return 1
    elif node1[0] - node2[0] == 1 and node1[1] - node2[1] == 1 and node1[2] == 0 and node2[2] == 1:
        return 1
    elif node1[0] - node2[0] == -1 and node1[1] - node2[1] == -1 and node1[2] == 1 and node2[2] == 0:
        return 1
    return 1000


node_list = []
nodenum = 0
for i in range(people_num + 1):
    for j in range(wolf_num + 1):
        for k in range(2):
            if (i < j and k == 1) or (3 - i < 3 - j and k == 0):
                continue
            node_list.append([i, j, k])
            nodenum = nodenum + 1

maps = [[0 for i in range(nodenum)] for i in range(nodenum)]

for i in range(nodenum):
    for j in range(nodenum):
        if i != j:
            maps[i][j] = judge(node_list[i], node_list[j])
        else:
            maps[i][j] = 0

rc_state = graph.Graph(maps)
print rc_state.get_nodenum()
[path, dist] = rc_state.d_find_shortest(
    node_list.index([3, 3, 0]), node_list.index([0, 0, 1]))

for foot in path:
    print node_list[foot]
