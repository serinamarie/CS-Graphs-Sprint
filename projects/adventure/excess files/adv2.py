from room import Room
from player import Player
from world import World
from traverse import traverse

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt" # passed
# map_file = "maps/test_loop.txt" # passed
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
    # create dictionary 
    d = {}
    # create visited for filtering exits
    visited = []
    
    # get starting room
    starting_room = world.starting_room.id

    # add the starting room to visited
    visited.append(starting_room)

    # add the starting room to the dict
    d[starting_room] = {}

    # get the starting room's exits
    exits = world.starting_room.get_exits()

    # for each exit
    for exit in exits:

        # add a question mark
        d[starting_room][exit] = '?'

    # choose a direction from the exits
    direction = random.choice(exits)

    # add the direction to our traversal path
    traversal_path.append(direction)

    # have our player travel into that direction
    player.travel(direction)

    # get the current room number (this is the second room)
    current_room = player.current_room.id

    # create a dict for that starting room 
    d[starting_room][direction] = current_room
    
    # create an empty stack and queue
    stack = []
    queue = []

    # add the 2nd room to the stack
    stack.append(current_room)

    # while we have ? values in our dict
    while any('?' in ro.values() for ro in d.values()):

        # while we have something in the stack
        while stack:
            print('while stack:', stack)
            # get the first value
            room = stack.pop()
            print('room:', room)
            # add the value to visited
            visited.append(room)
           
            print('visited after stack append:', visited)
            # get the room's exits
            # exits = player.current_room.get_exits()
            exits = world.rooms[room].get_exits()
            print('d:', d)
            print('id and exits:', world.rooms[room].id, exits)
           
            # if room is already in dictionary
            if room in d:
                # if the room has no '?'
                if '?' not in d[room].values():
                    # skip it
                    continue 
            # otherwise if we haven't visited this room
            elif room not in d:
                # add a new dict entry
                d[room] = {}
                for exit in exits:
                    d[room][exit] = '?'
            # for each exit
            for exit in exits:
                print('exit:', exit)
                print('traversal path:', traversal_path)
                # if the room has been unexplored
                if d[room][exit] == '?':
                    
                    # add the next room to the stack
                    next_roo = world.rooms[room].get_room_in_direction(exit).id
                    stack.append(next_roo)
                    print('next roo:', next_roo)

        # for stack, cannot actually travel to room 

        if any('?' in r.values() for r in d.values()):
            n = visited[-1]
            queue.append([n])

        directions = []
        min_path_length = 100
        while queue:
            print('queue:', queue)
            path = queue.pop(0)
        
            last_in_path = path[-1]
            print('last in path', last_in_path)

            # print('last in path:', last_in_path)
            if '?' in d[last_in_path].values():
                # get exits, etc.
                # print('if ??? print path:', path)
                
                if len(path) < min_path_length:
                    print('dictionary:', d)

                    for i, room in enumerate(path[:-1]):
                        direction = list(d[room].keys())[list(d[room].values()).index(path[i+1])]
                        traversal_path.append(direction)
                        directions.append(direction)
                        player.travel(direction)
                    min_path_length = len(path)

                
                    brand_new = player.current_room.id
                    print('d brand new:', d[brand_new])

                    # return key in dict[0] where the key's value is 5
                    exits = player.current_room.get_exits()
                    second_to_last = path[-2:-1]
                    for exit in exits:
                        if player.current_room.get_room_in_direction(exit).id == second_to_last[0]:
                            d[brand_new][exit] = second_to_last[0]
                    print('d:', d)
                    #     b = player.current_room.get_room_in_direction(exit)
                    #     blah.append(exit)

                    # print('blah:', blah)
                    
                    # get unknown direction keys
                    a = [key  for (key, value) in d[brand_new].items() if value == '?']
                    print('a', a)

                    # pick a random room
                    if a: 
                        random_direction = random.choice(a)
                        print(random_direction)
                        the_chosen_one = player.current_room.get_room_in_direction(random_direction).id
                        d[player.current_room.id][random_direction] = the_chosen_one
                        player.travel(random_direction)
                        traversal_path.append(random_direction)
                        print('the chosen one:', the_chosen_one)

                        print('traversal path before stack', traversal_path)

                        # add chosen one to stack
                        stack.append(the_chosen_one)

                        queue = []
                        print('queue:', queue)
                    # # get random room 
                    # exits = player.current_room.get_exits()
                # # find where exit has ?
                # possible_next = []
                # for exit in exits:
                #     if d[player.current_room.id][exit] == '?':
                #         possible_next.append(exit)
                # print(possible_next)
                # # choose rand
                # stack.append(rand)
                
                
            else:
            # print('traversal_path:', traversal_path)
                if len(path) < min_path_length:
                    exits = world.rooms[last_in_path].get_exits()
                    print('exits:', world.rooms[last_in_path].id, exits)
                
                    print('d before travel:', d)
                    for exit in exits:
                        
                        n = world.rooms[last_in_path].get_room_in_direction(exit).id



                        # n = player.current_room.get_room_in_direction(exit).id
                        print('n:', exit, n)
                        # print('if n not in:', path)
                        if n not in path:
                            
                            new_path = list(path)
                            
                            # print('new room:', player.current_room.id)
                            new_path.append(n)
                            # print('new_path:', new_path)
                            queue.append(new_path)
                            
                        

    return traversal_path
                    

    
    # return player.current_room.id, traversal_path


# Fill this out with directions to walk
traversal_path = ['n', 'n']
traversal_path = traverse(player)


print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

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
