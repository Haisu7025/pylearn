#!/usr/bin/python
# -*- coding: UTF-8 -*-

import graph

map = [[0, 3, 1, 10], [2, 0, 1000, 1000], [1000, 1000, 0, 3], [1000, 1, 5, 0]]
test_graph = graph.Graph(map)

a = test_graph.get_nodenum()
print a

[a, b] = test_graph.Dijkstra(1)
print a, b

[a, b] = test_graph.d_find_shortest(1, 3)
print a, b

[a, b] = test_graph.Floyd()
print a, b
