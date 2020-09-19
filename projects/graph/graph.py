"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):

        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Assuming this is a directed graph requiring edges made up of ordered pairs
        if v1 in self.vertices:
            
            # add the connection
            self.vertices[v1].add(v2)

        # if not in vertices dict
        else: 

            raise Exception(f"No {v1} vertex in dict of vertices")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # instantiate a queue
        queue = Queue()

        # create a set for our visited vertices
        visited = set() 

        # mark starting vertex as visited
        visited.add(starting_vertex)

        # queue up the starting vertex
        queue.enqueue(starting_vertex)

        # while we have a queue
        while queue.size() > 0:

            # grab the vert at the front of the line 
            current_vert = queue.dequeue()

            # print the vert
            print(current_vert)

            # get vert's neighbors 
            neighbors = self.get_neighbors(current_vert)

            # for each neighbor
            for neighbor in neighbors:

                # if neighbor has not been visited
                if neighbor not in visited:

                    # mark as visited
                    visited.add(neighbor)

                    # add neighbor to top of the stack
                    queue.enqueue(neighbor)

        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # instantiate a stack
        stack = Stack()

        # track visited verts as a set()
        visited = set() 

        # add starting vert to visited
        visited.add(starting_vertex)

        # push the starting vert
        stack.push(starting_vertex)
     
        # while stack isn't empty
        while stack.size() > 0:

            # pop off the top of the stack, and set to current vert
            current_vert = stack.pop()

            print(current_vert)

            # get vert's neighbors 
            neighbors = self.get_neighbors(current_vert)

            # for each neighbor
            for neighbor in neighbors:

                # if neighbor has not been visited
                if neighbor not in visited:

                    # mark as visited
                    visited.add(neighbor)

                    # add neighbor to top of the stack
                    stack.push(neighbor)

      
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # this passes but feels messy.. need to return with a cleaner way

        if not isinstance(starting_vertex, list):
            starting_vertex = [starting_vertex]

        # if length of starting_vertex equal to the number of vertices
        if len(starting_vertex) == len(self.vertices):

            # return vertices individually
            print('\n'.join(str(e) for e in starting_vertex))
    
        # else 
        else:

            # list starting vertex[-1]
            for neighbor in self.get_neighbors(starting_vertex[-1]):

                # if neighbor not already visited
                if neighbor not in starting_vertex:

                    # make a new path
                    new_path = list(starting_vertex)
    
                    # append neighbor to new path
                    new_path.append(neighbor)

                    # traverse
                    self.dft_recursive(new_path)



        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # instantiate a queue
        queue = Queue()

        # visited nodes
        visited = set()

        # queue the starting vertex
        queue.enqueue([starting_vertex])

        # while there is a queue
        while queue.size() > 0:

            # dequeue a path 
            path = queue.dequeue()

            # go to the deepest level in the path
            deepest_vertex = path[-1]

            # if the deepest level node is the destination vertex
            if deepest_vertex == destination_vertex:

                # this is the path! (or at least one of the paths of this length)
                # there may be others at this depth as well
                return path
            
            # for each neighbor
            for neighbor in self.get_neighbors(deepest_vertex):

                # create a new path (increasing the level of depth in our search)
                new_path = list(path)

                # where we add a new neighbor (level of depth) for each possibility
                new_path.append(neighbor)

                # add the new path to the queue
                queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # instantiate a stack
        stack = Stack()

        # push the starting vertex onto the stack
        stack.push([starting_vertex])

        # while there is a stack
        while stack.size() > 0:

            # pop off a path 
            path = stack.pop()

            # go to the deepest level in the path
            deepest_vertex = path[-1]

            # if the deepest level vertex is the destination vertex
            if deepest_vertex == destination_vertex:

                # we can stop our search
                return path
            
            # for each neighbor
            for neighbor in self.get_neighbors(deepest_vertex):

                # create a new path (increasing the level of depth in our search)
                new_path = list(path)

                # where we add a new neighbor (level of depth) for each possibility
                new_path.append(neighbor)

                # add the new path to the queue
                stack.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # not structured properly
        
        if not isinstance(starting_vertex, list):
            starting_vertex = [starting_vertex]
        # base case
        if starting_vertex[-1] == destination_vertex:
            print(starting_vertex)
        else:
            # get neighbors
            neighbors = self.get_neighbors(starting_vertex[-1])

            for neighbor in neighbors:
                # if neighbor not in starting_vertex 
                if neighbor not in starting_vertex:
                    new_path = list(starting_vertex)
                    # append neighbor
                    new_path.append(neighbor)
                    # recursion
                    self.dfs_recursive(new_path, destination_vertex)

              

                # return
    
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(7)
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    # graph.add_edge(1, 3)
    # graph.add_edge(2, 3)
    # graph.add_edge(3, 6)
    # graph.add_edge(5, 6)
    # graph.add_edge(5, 7)
    # graph.add_edge(4, 5)
    # graph.add_edge(4, 8)
    # graph.add_edge(8, 9)
    # graph.add_edge(11, 8)
    # graph.add_edge(10, 1)

    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(6, 3)
    graph.add_edge(6, 5)
    graph.add_edge(7, 5)
    graph.add_edge(5, 4)
    graph.add_edge(8, 4)
    graph.add_edge(9, 8)
    graph.add_edge(8, 11)
    graph.add_edge(1, 10)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('graph vertices:', graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('----bft iteration-----')
    graph.bft(6)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('----dft iteration-----')

    print(graph.dft(1))
    print('----dft recursion-----')
    print(graph.dft_recursive(6))

    # print('----bfs-----')
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('----dfs iterative----')
    print(graph.dfs(6, 10))

    print('----dfs recursive-----')
    print(graph.dfs_recursive(6, 10))

    dft = [
        "1\n2\n3\n5\n4\n6\n7\n",
        "1\n2\n3\n5\n4\n7\n6\n",
        "1\n2\n4\n7\n6\n3\n5\n",
        "1\n2\n4\n6\n3\n5\n7\n"
    ]
    import sys, io
    stdout_ = sys.stdout
    sys.stdout = io.StringIO()
    graph.dft_recursive(1)
    output = sys.stdout.getvalue()

    print(output, dft)

    sys.stdout = stdout_  # Restore stdout
