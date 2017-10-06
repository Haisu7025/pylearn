#!/usr/bin/python
# -*- coding: UTF-8 -*-

import graph_tool as gt

"""
测试图
A -> B
A -> C
B -> C
B -> D
C -> D
D -> C
E -> F
F -> C
"""

# 图采用字典形式储存
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print gt.find_path(graph, 'A', 'D')
print gt.find_all_paths(graph, 'A', 'D')
print gt.find_shortest_path(graph, 'A', 'D')
