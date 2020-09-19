# understand problem
# acyclic directed graph where we want to traverse to the deepest vertex
# dft

# plan 
# create a hash table called vertices to store ancestors - check
# create an empty list for stack - check
# create an empty set for visited ancestors - check
# append all ancestors to vertices dict - check
# while there are ancestors in the stack - check
# pop off the most recently added vertex - check
# get its neighbors
# for each neighbor
# if not already visited
# add the neighbor
# edge cases: no ancestors
# also, keep track of depth

# execute
def earliest_ancestor(ancestors, starting_vertex):

    # create a hash table called vertices to store ancestors
    vertices = {}

    # append all ancestors and their edges to vertices dict
    for ancestor in ancestors:
        vertices[ancestor[1]] = set()
        vertices[ancestor[0]] = set()

    for ancestor in ancestors:
        if ancestor[1] not in vertices:
            vertices[ancestor[1]] = ancestor[0]
        else:
            vertices[ancestor[1]].add(ancestor[0])

    # if starting vertex has no ancestors
    if not vertices[starting_vertex]:
        return -1

    # if it has ancestors
    else:

        # create an empty list for stack
        stack = []

        # create an empty set for visited ancestors
        visited = set()

        # keep track of depth
        depth = {starting_vertex:0}

        # add the starting vertex to the visited vertices
        visited.add(starting_vertex)

        # add the starting vertex to the stack
        stack.append(starting_vertex)

        # while there are ancestors in the stack
        while stack:

            # pop off the most recently added vertex
            current_vert = stack.pop()

            # get a list of its ancestors
            edges = vertices[current_vert]

            # loop through vertex's edges
            for edge in edges:  

                # track the edge's depth as being one greater than the current node's
                depth[edge] = depth[current_vert] + 1
                
                # if not already visited
                if edge not in visited:

                    # add the edge to the visited list
                    visited.add(edge)

                    # add edge to top of the stack
                    stack.append(edge)
                
        # return the max depth(s)
        max_value = max(depth.values())

        # return the minimum key 
        return min([k for k, v in depth.items() if v == max_value])


if __name__ == '__main__':

    # ancestors
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), 
    (4, 8), (8, 9), (11, 8), (10, 1)]
    
    print(earliest_ancestor(test_ancestors, 9))
