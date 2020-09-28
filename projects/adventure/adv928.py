from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt" # passed
# map_file = "maps/test_cross.txt" # passed
# map_file = "maps/test_loop.txt" # passed
# map_file = "maps/test_loop_fork.txt" # passed 
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# directions = world.rooms[8].get_exits()

# for direct in directions:
#     print(world.rooms[8].get_room_in_direction(direct).id)

def traverse(player):
    # create traversal path 
    traversal_path = [] 
    # create a dict for storage
    d = {}
    # keep track of visited for stack
    visited = []
    # get the id of the starting room
    starting_room = world.starting_room.id
    # add visited to starting room
    visited.append(starting_room)
    # create a dict entry for starting room
    d[starting_room] = {}
    # get starting room exits
    exits = world.starting_room.get_exits()
    # for each exit, create a dict key for that room with '?' value
    for exit in exits:
        d[starting_room][exit] = '?'
    # choose a random direction to start in
    direction = random.choice(exits)
    
    # # travel in that direction
    # player.travel(direction)

    # get current room id
    current_room = player.current_room.get_room_in_direction(direction).id
    print('current room:', current_room)
    # change the starting room '?' value to room id for that exit
    d[starting_room][direction] = current_room

    visited.append(current_room)

    stack = []
    stack.append([current_room, direction])
    while len(d) < len(room_graph):
        print('length of d:', len(d))
        print('length of room graph:', len(room_graph))
    

        # initialize stack and queue
        
        queue = []

        
        room_path = []
        while stack:
            # pop off top of stack
            curr = stack.pop()
            print('stack:', stack)
            print('popped:', curr[-1])
            print('curr room before travel:', player.current_room.id)
            # append direction and then travel
            
            player.travel(curr[-1])
            traversal_path.append(curr[-1])
            room_path.append(curr[0])
            
            print('curr room after travel:', player.current_room.id)
            # get id's of exit rooms
            exits = player.current_room.get_exits()

           

            ro = player.current_room.id
            print('ro:', ro)
        
            if ro not in d:
                d[ro] = {}
                for exit in exits:
                    d[ro][exit] = '?'
                print(ro, 'added to d')
            else:
                print(ro, "in dict")

            # get list of rooms
            list_of_rooms = {}
            for exit in exits:
                list_of_rooms[exit] = player.current_room.get_room_in_direction(exit).id


            # get list of unvisited rooms
            unvisited_exits = []
            unvisited_exits.append([k for k, v in list_of_rooms.items() if v not in visited])
            print('unvisited exits before trim:', unvisited_exits)
            # get room
            current_room = player.current_room.id
            print('current room:', current_room)
            try:
                unvisited_exits = unvisited_exits[0][0]
                print('unvisited exits:', unvisited_exits)
                # for each unvisited exit
                for ex in unvisited_exits:
                    print('ex:', ex)
                    direction = ex[0]
                    print('direction:', direction)
                    
                    # add room to visited
                    visited.append(player.current_room.get_room_in_direction(direction).id)
                    # add exit room and direction to stack
                    stack.append([current_room, direction])
                    # add d[room][exit] = id
                    print(player.current_room.get_room_in_direction(direction).id)
                
                    d[ro][direction] = player.current_room.get_room_in_direction(direction).id

            # if no unvisited exits
            except:
                
                print('no unvisited exits')
                # the last node in traversal (4 for example, won't have been added to dict for some reason )
                print(player.current_room.id, player.current_room.get_exits())
                exits = player.current_room.get_exits()
                current_room = player.current_room.id
                print('all exits:', exits)
                counter = 0
                for exit in exits:
                    # if exit has '?'
            
                # if '?' in d[current_room][exit]:
                    if d[current_room][exit] == '?':
                        d[current_room][exit] = player.current_room.get_room_in_direction(exit).id
                        # add exit room to stack
                        print('id_and_exit:', player.current_room.get_room_in_direction(exit).id, exit)
                        stack = []
                        stack.append([player.current_room.get_room_in_direction(exit).id, exit])

                    else:
                        counter += 1
                print('stack:', stack)
                if counter == len(exits):
                    stack = []
                    break
                    
        # if length of d is less than len(room graph)
        if len(d) < len(room_graph):
            # put current room into queue so we can find nearest room with ?
            queue.append([player.current_room.id])     
        min_path_length = 999 
        directions = []       
        while queue:
            # 121
            path = queue.pop(0)

            last_in_path = path[-1]
            print('last in path:', last_in_path)

            # goal reached
            if '?' in d[last_in_path].values():
            
                print('questions in here')
                
                if len(path) < min_path_length:
            
                    for i, room in enumerate(path[:-1]):
                        direction = list(d[room].keys())[list(d[room].values()).index(path[i+1])]
                        traversal_path.append(direction)
                        directions.append(direction)
                        player.travel(direction)
                        print('added to traversal path from queue:', player.current_room.id)

                        # 9/27
                        visited.append(room) # last one will be appended in stack

                        
                    room_for_stack = player.current_room.id

                    visited.append(room_for_stack) #9/27

                    print('room for stack:', room_for_stack)

                    # find if any unvisited nodes. 
                    exits = player.current_room.get_exits()
                    # get list of rooms
                    list_of_rooms = {}
                    for exit in exits:
                        list_of_rooms[exit] = player.current_room.get_room_in_direction(exit).id

                    # see if there are unvisited rooms before choosing one with a '?'
                    # get list of unvisited rooms
                    unvisited_exits = []
                    unvisited_exits.append([k for k, v in list_of_rooms.items() if v not in visited])
                    
                    # try getting unvisited rooms
                    try:
                        unvisited_exits = unvisited_exits[0][0]
                        print('unvisited exits:', unvisited_exits)
                        # if multiple unvisited nodes
                        if len(unvisited_exits) > 1:
                            # choose one at random and go there
                            random_exit = random.choice(unvisited_exits)
                            print('random exit:', random_exit)
                            chosen_exit_room = player.current_room.get_room_in_direction(random_exit).id 
                            print('chosen exit:', chosen_exit_room)
                            visited.append(chosen_exit_room)
                            d[room_for_stack][random_exit] = chosen_exit_room
                            print('d[room_for_stack]:', d[room_for_stack])
                            # player.travel(random_exit)
                            print('current room after travel:', player.current_room.id)
                            stack.append([chosen_exit_room, random_exit])
                            queue = []
                        elif len(unvisited_exits) == 1:
                    
                            exit_room = player.current_room.get_room_in_direction(unvisited_exits).id 
                            print('exit room:', exit_room)
                            visited.append(exit_room)
                            d[room_for_stack][unvisited_exits] = exit_room
                            print('d[room_for_stack]:', d[room_for_stack])
                            # player.travel(unvisited_exits)
                            print('current room after travel:', player.current_room.id)
                            stack.append([exit_room, unvisited_exits])
                            print('stack append:', [exit_room, unvisited_exits])
                            queue = []
                            
                    # if no unvisited rooms
                    except:

                        # find where room's exits are a question mark
                    
                        unknown_exits = [key for (key, value) in d[room_for_stack].items() if value == '?']
                        print('unknown exits:', unknown_exits)
                        # choose one at random 
                        if unknown_exits:
                        
                            random_direction = random.choice(unknown_exits)
                            print('random direction:', random_direction)
                            chosen = player.current_room.get_room_in_direction(random_direction).id
                            print('chosen:', chosen)
                            visited.append(chosen)
                            # add to dict
                            d[room_for_stack][random_direction] = chosen
                            print('d[room_for_stack]:', d[room_for_stack])
                            # 9/27
                            # player.travel(random_direction)
                            print('current room after travel:', player.current_room.id)
                        
                            
                            # as we do it in stack
                            # # have not appended to traversal path !
                            # traversal_path.append(random_direction)
                            # print('traversal path:', traversal_path)

                            stack.append([chosen, random_direction])
                            queue = []
                

                    # add to latest node to stack
            else:
                # if we have found a short path, no reason to keep going otherwise
                if len(path) < min_path_length:
                    exits = world.rooms[last_in_path].get_exits()
                    print('exits:', world.rooms[last_in_path].id, exits)
                    # w and e
                    for exit in exits:
                        exit_id = world.rooms[last_in_path].get_room_in_direction(exit).id
                        print('exit id:', exit_id)
                        if exit_id not in path:
                            new_path = list(path)
                            new_path.append(exit_id)
                            queue.append(new_path)
                            print(new_path)
                        else:
                            print(exit_id, 'is in path')

    print('length of d:', len(d))
    print('length of room graph:', len(room_graph))
    print(any('?' in ro.values() for ro in d.values()))
    print('traversal path:', traversal_path)
    print('algorithm says visited:', set(visited), len(visited))
    return traversal_path
    


            
                
                    




# Fill this out with directions to walk
traversal_path = ['n', 'n']
traversal_path = traverse(player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
ids = []

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    ids.append(player.current_room.id)


print("test says player's current room", ids, len(set(ids)))

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
