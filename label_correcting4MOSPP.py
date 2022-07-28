#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 18:25
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : label_correcting4MOSPP.py
# @Statement : The label correcting algorithm for the multi-objective shortest path problem using the sum function
# @Reference : Paixão J M, Santos J L. Labeling methods for the general case of the multi-objective shortest path problem–a computational study[M]//Computational Intelligence and Decision Making. Springer, Dordrecht, 2013: 489-502.
import copy
import heapq


def find_neighbor(network):
    """
    find the neighbor of each node
    :param network:
    :return: {node 1: [the neighbor nodes of node 1], ...}
    """
    nn = len(network)
    neighbor = []
    for i in range(nn):
        neighbor.append(list(network[i].keys()))
    return neighbor


def dominated(obj1, obj2):
    """
    judgment whether ripple 1 is dominated by ripple 2
    :param obj1: the objective value of ripple 1
    :param obj2: the objective value of ripple 2
    :return:
    """
    sum_less = 0
    for i in range(len(obj1)):
        if obj1[i] < obj2[i]:
            return False
        elif obj1[i] != obj2[i]:
            sum_less += 1
    if sum_less != 0:
        return True
    return False


def add_labels(omega, obj_list, destination, temp_node, temp_obj):
    """

    :param omega:
    :param obj_list:
    :param destination:
    :param temp_node:
    :param temp_obj:
    :return:
    """
    for index in omega[temp_node]:
        if dominated(temp_obj, obj_list[index]):
            return False
    for index in omega[destination]:
        if dominated(temp_obj, obj_list[index]):
            return False
    return True


def main(network, source, destination):
    """
    the main function
    :param network: {node 1: {node 2: [weight1, weight2, ...], ...}, ...}
    :param source: the source node
    :param destination: the destination node
    :return:
    """
    # Step 1. Initialization
    neighbor = find_neighbor(network)
    nn = len(network)  # node number
    nw = len(network[source][neighbor[source][0]])  # objective number'
    obj_list = []
    path_list = []
    ni = 0
    omega = {}
    for node in range(nn):
        omega[node] = []
    queue = []
    ind = 0
    heapq.heappush(queue, (0, ind, {
        'path': [source],
        'obj': [0 for n in range(nw)],
    }))
    ind += 1

    # Step 2. The main loop
    while queue:
        length, temp_ind, info = heapq.heappop(queue)
        path = info['path']
        obj = info['obj']
        epicenter = path[-1]
        if add_labels(omega, obj_list, destination, epicenter, obj):
            omega[epicenter].append(ni)
            obj_list.append(obj)
            path_list.append(path)
            ni += 1
            for node in neighbor[epicenter]:
                if node not in path:
                    temp_list = network[epicenter][node]
                    temp_obj = [obj[n] + temp_list[n] for n in range(nw)]
                    temp_path = copy.deepcopy(path)
                    temp_path.append(node)
                    heapq.heappush(queue, (sum(temp_obj), ind, {
                        'path': temp_path,
                        'obj': temp_obj,
                    }))
                    ind += 1

    # Step 3. Sort the results
    result = []
    for index in omega[destination]:
        result.append({
            'path': path_list[index],
            'obj': obj_list[index],
        })
    return result


if __name__ == '__main__':
    if __name__ == '__main__':
        test_network = {
            0: {1: [62, 50], 2: [44, 90], 3: [67, 10]},
            1: {0: [62, 50], 2: [33, 25], 4: [52, 90]},
            2: {0: [44, 90], 1: [33, 25], 3: [32, 10], 4: [52, 40]},
            3: {0: [67, 10], 2: [32, 10], 4: [54, 100]},
            4: {1: [52, 90], 2: [52, 40], 3: [54, 100]},
        }
        source_node = 0
        destination_node = 4
        print(main(test_network, source_node, destination_node))
