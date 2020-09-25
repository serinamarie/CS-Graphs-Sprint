## Thoughts from Tim's lecture

- undirected graph

- get room in direction (he said you might not even need to)

- not a breadth first (at first), because it will require many more moves, 

- go in one direction until you hit dead end, retrace your steps, then explore the nearest unvisited node (room) (keep track of distance from start)

- read the readme very closely "starts by writing an algorithm that picks a random" etc.

- AMA Thursday night

- capabilities of each class

## class capabilities
 ### Room 
 - attributes: room id, room name, room desc, n_to, s_to, e_to, w_to, x, y
 - methods: 
    - get_exits(), could randomly shuffle possible exits and choose one
    - connect_rooms('n', 5)
    - get_room_in_direction('n') (for player to use)
    - get_coords()
### Player
- attributes: current_room
- methods: travel('n') (uses get_room_in_direction) and moves to it

### World
- attributes: starting room, rooms={}, room_grid=[], grid_size=0
- methods:
    - load_graph(graph), grid size becomes 1, rooms becomes an array of 500 Nones
    - adds each room from .txt file to dict

## Requirements:
- visit every room at least once
- starting graph a dictionary of rooms, each with four k/v pairs, n/s/w/e, with '?' to be replaced with a room #, if no room # need some other symbol to denote non-existence
- create algorithm which creates a map for the player, logging it into traversal_path
    - while # values in those keys have '?':
    - in starting room
    - choose random starting direction, dft
    - once dft completed, bfs for nearest unexplored room. return that path, convert path to a list of nsew directions before adding to traversal path, 
    - maybe? get end of the traversal path, do a dft until dead end (visit that direction), repeat

 - will need: visited, queue, stack, map dict,

 ## Plan algorithm
 def algorithm(map, starting_room):
    # dict = {}
    # get player.current_room.id
    # get player.current_room.get_exits()
    # add dict[current_room][id] # add all possible exits, with ? marks
    # direction ('n') = choose 1 exit randomly ('n')
    # current_room = player.travel(direction)
    # dict[starting_room][direction 'n'] = current_room.id (1)

    # visited_s = set() add starting room
    # create a stack
    # create a queue
    # push the current_room to stack

     
# while dict length is less than 500
    # while stack
        # room = pop()
        # add to visited_s

        # get exits 
        # exits ('n') = get_exits()
        # for exit ('n') in exits:
            create new entry in dict
            # dict[room.id][exit] = get_room_in_direction(exit)

            if dict[room.id][exit] not in visited_s
                # next_room = get_room_in_direction(exit)
                # add to visited_s
                # stack.push(next_room)

    n = last node in visited/path
    # add n to visited_q
    enqueue(n)
    
    while dict[n].values does not contain '?':
        # curr = dequeue()
        # exits = get curr's exits
        # for exit in exits
            # n = curr.get_room_in_direction(exit)
            # if n in visited_q
                # enqueue(n)
                # add to visited_q
    # room_with_question_mark = dequeue()
    # direction = get a random question mark from this room
    # next_room_for_stack = room_with_question_mark.get_room_in_direction(direction)
    # push(next_room_for_stack)
            

    # no unvisited, we must go back to nearest unvisited room 
    # find shortest distance to nearest unvisited room by doing bfs
    # once arrive at '?', 
    # add to stack

    queue = [visited]
    
    last = visited[-1]

    while dict[last.id] does not contain ?:

        queue.dequeue()
    
            

    


    
    

   - once dft completed, bfs for nearest unexplored room. return that path, convert path to a list of nsew directions before adding to traversal path, 
    - maybe? get end of the traversal path, do a dft until dead end (visit that direction), repeat


 