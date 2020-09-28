from room import Room
from player import Player
from world import World
from traverse import traverse

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt" # passed
# map_file = "maps/test_cross.txt" # passed
# map_file = "maps/test_loop.txt" # passed
# map_file = "maps/test_loop_fork.txt" # passed 
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

    print('d:', d)
    
    # initialize stack and queue
    stack = []
    queue = []

    stack.append([current_room, direction])

    while stack:
        print('traversal_path:', traversal_path)
        # pop off top of stack
        curr = stack.pop()
        print('popped:', curr[-1])
        print('curr room before travel:', player.current_room.id)
        # append direction and then travel
        
        player.travel(curr[-1])
        traversal_path.append(curr[-1])
        
        print('curr room after travel:', player.current_room.id)
        # get id's of exit rooms
        exits = player.current_room.get_exits()

        print('visited:', visited)

        ro = player.current_room.id
        print('ro:', ro)
    
        if ro not in d:
            d[ro] = {}
            for exit in exits:
                d[ro][exit] = '?'
            print(ro, 'added to d')
        else:
            print(ro, "in dict")
        print('d before getting exits:', d)

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
                print('d:', d)

        # if no unvisited exits
        except:
            
            print('no unvisited exits')
            # the last node in traversal (4 for example, won't have been added to dict for some reason )
            print(player.current_room.id, player.current_room.get_exits())
            exits = player.current_room.get_exits()
            current_room = player.current_room.id
            for exit in exits:
                # if exit has '?'
                print('all exits:', exits)
               # if '?' in d[current_room][exit]:
                if d[current_room][exit] == '?':
                    # add exit room to stack
                    stack.append([player.current_room.get_room_in_direction(exit).id, exit])
                    d[current_room][exit] = player.current_room.get_room_in_direction(exit).id
                    print('stack:', stack)
                    print('d after no unvisited exits:', d)
                else:
                    print('no')
            
                
                    

                    # print('d:', d[ro])
                    # # add d[room][exit] = id
                    # d[ro][exit] = world.rooms[ro].get_room_in_direction(exit).id 
                    # print('d:', d[ro])
    return traversal_path


            
                
                    




# Fill this out with directions to walk
traversal_path = ['n', 'n']
traversal_path = traverse(player)
print('final:', len(traversal_path))

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
