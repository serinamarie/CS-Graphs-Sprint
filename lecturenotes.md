
```
MODULE 1 OBJECTIVES

- describe what a graph is, explain its components, provide examples of its useful applications, and draw each of the different graph types

- represent a graph as an adjacency list and an adjacency matrix and compare and contrast the respective representations

- represent a breadth-first-search of a graph in pseudo-code and recall common applications for its use

- represent a depth-first-search of a graph in pseudo-code and recall common applications for its use
```


### Graphs
* are a set of vertices and edges that connect those vertices
* are collections of data represented by nodes and connections between nodes 
* graphs are ordered pairs (order matters), G = (V, E), where V is a set of vertices/nodes, and E is a set of edges/links. V contains a set of unordered references, whereas E might contains a set of unordered pairs, such as in an undirected graph. In a directed graph, E would contain ordered pairs.

### Components
- nodes/vertices: cities, animals, web pages could be objects in a dataset, represented by nodes/vertices
- edges: connections between vertices, can be bidrectional, how you can get from A to B
- weight: cost to travel across an edge

### Implement a graph by creation of a few different sets
- a set of nodes/vertices 
- a set of edges

### Use cases
- subway system
- github (history of commits and pull requests)
- social network

### Types of Graphs
- directed: has at least one edge that nly is not bidirectional
- undirected: bidirectional 
- cyclic: edges allow you to revisit at least one node/vertices (any undirected graph)
- acyclic: vertices can only be visited once

### Graph characteristics
* dense graph: many edges as compared to nodes
* sparse graph: smaller edge-to-node ratio
* edge list: a representation of all edges in a graph, finding an edge requires linear o(e) time
* adjacency matrix: represents which nodes have edges between them. 
    - the matrix serves as a lookup table where a value of 1 represents an edge that exist, and 0 represents an edge that does not. 
    - always a main diagonal of 0
    - adding or deleting an edge can be done in o(1) time since you can just look up the intersection
    - adjacency matrices can be wasteful when you have a sparse graph, 
    as you would need to build it out even though it'd be mostly 0s
    - requires o(v^2) of space
    - If a graph is undirected, its matrix will be symmetric
* adjacency list (a hybric): an array of linked lists that serve to represent
a graph, but also make it easy to see which *other* nodes are adjacent to other nodes
    - each node has a reference to all of its neighbors through an adjacent linked list
    - each vertex is given an index in its list, and the neighboring vertices
    are stored in a linked list adjacent to it
    - retrieving a node's neighbors takes constant o(1) time 
    - what if we want to find a particular edge to see if it exists? 
        - constant time o(1), in the worst case (having to go through the whole list), it takes o(d) time, where d is the degree of the vertex (the number of edges it has/of neighboring nodes it has)
    - space for adjacency list of an undirected graph is 2(|E|) elements, with E being total number of edges 
    - space for adjacency list of a directed graph is |E| elements

* degree: the degree of a vertex could be as large as |V| - 1 (1 meaning itself). min possible value of d is 0, since we could always have a graph with only one vertex (so 1-1 = 0)

* traversing a graph data structure involves visiting each verte in a graph
    - the order in which vertices are visited is how we can classify graph traversals
    - DFS uses a stack data structure whereas DBS uses a queue data structure

### BFS traversal
1. Choose a starting point
2. Add a node to queue of nodes to be visited
3. Visit the topmost node in the queue and mark it visited
4. If that node has any neighbors, check to see if they have been visited
5. Add any neighboring nodes that still need to be visited to the queue
6. Remove the node we've visited from the queue

BFS lends itself to determining the shortest path between any node in the graph and the 'parent' node, we can keep track of the parents, if it is a level 3 node, it has 3 edges to return back to the 'parent' node
    - an array of visited nodes, all marked FALSE to start
    - runtime complexity can be calculated from the fact that for every single vertex in the graph, we have to iterate through adjacency list once o(v+e), to visit every node once, and check every edge in its adjacency list

DFS is helpful in determining if a path even exist