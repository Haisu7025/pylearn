#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数据结构——图的相关工具


def find_path(graph, start, end, path=[]):
    # 寻找路径 非最短
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def find_all_paths(graph, start, end, path=[]):
    # 寻找全部路径
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    # 寻找最短路径
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path
