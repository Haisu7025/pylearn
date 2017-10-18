#!/usr/bin/python
# -*- coding: UTF-8 -*-

import graph

maps = [[0, 0, 0, 1], [1, 0, 1000, 1000],
        [1, 1000, 0, 1], [1000, 1, 1, 0]]
test_graph = graph.Graph(maps)
test_graph.get_edgenum()
test_graph.get_nodenum()

print test_graph.nodenum

test_graph.broadth_first_search()
