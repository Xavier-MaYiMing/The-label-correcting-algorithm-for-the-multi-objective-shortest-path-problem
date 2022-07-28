### The Label Correcting Algorithm for the Multi-Objective Shortest Path Problem

##### Reference: Paixão J M, Santos J L. Labeling methods for the general case of the multi-objective shortest path problem–a computational study[M]//Computational Intelligence and Decision Making. Springer, Dordrecht, 2013: 489-502.

The multi-objective aims to find a set of paths with minimized costs. 

| Variables   | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| network     | Dictionary, {node 1: {node 2: [weight 1, weight 2, ...], ...}, ...} |
| s_network   | The network described by a crisp weight on which we conduct the ripple relay race |
| source      | The source node                                              |
| destination | The destination node                                         |
| nn          | The number of nodes                                          |
| nw          | The number of objectives                                     |
| neighbor    | Dictionary, {node1: [the neighbor nodes of node1], ...}      |
| ind         | The index of each label added to the priority queue          |
| ni          | The index of each label that is assessed as the Pareto-optimal subpath |
| omega       | List, omega[n] contains all the indexes of labels that are assessed as the Pareto-optimal subpath from the source node to node n (Pareto-optimal labels) |
| obj_list    | List, the objective value of the each Pareto-optimal label   |
| path_list   | List, the path of each Pareto-optimal label                  |
| queue       | The priority queue, which outputs the label that has the minimum value of the summation of objectives at each iteration |

#### Example

![](C:\Users\dell\Desktop\研究生\个人算法主页\The NSGA-II for the multi-objective shortest path problem\MOSPP.png)

The red number associated with each arc is the first weight, and the green number is the second weight.

```python
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
```

##### Output:

```python
[
    {'path': [0, 2, 4], 'objective': [96, 130]}, 
    {'path': [0, 3, 4], 'objective': [121, 110]}, 
    {'path': [0, 3, 2, 4], 'objective': [151, 60]},
]
```

