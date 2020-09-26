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
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

def traverse(player):
    traversal_path = [] 
    d = {}
    visited = []
    
    starting_room = world.starting_room.id
    visited.append(starting_room)

    d[starting_room] = {}
    exits = world.starting_room.get_exits()
    for exit in exits:
        d[starting_room][exit] = '?'
    direction = random.choice(exits)
    traversal_path.append(direction)
    player.travel(direction)
    current_room = player.current_room.id
    d[starting_room][direction] = current_room
    
    stack = []
    queue = []

    stack.append(current_room)
    # while any('?' in room.values() for room in d.values()):
    while stack:
        room = stack.pop()
        visited.append(room)
        exits = player.current_room.get_exits()
        d[room] = {}
        for exit in exits:
            d[room][exit] = player.current_room.get_room_in_direction(exit).id
        for exit in exits:
            if d[room][exit] not in visited:
                traversal_path.append(exit)
                player.travel(exit)
                stack.append(d[room][exit])

    if any('?' in r.values() for r in d.values()):
        n = visited[-1]
        queue.append(n)
        
    while queue:
        path = queue.pop()
        if not isinstance(path, list):
            path = [path]
        last_in_path = path[-1]
        print('last in path:', last_in_path)
        if '?' in d[last_in_path].values():
            # get exits, etc.
            print('if ??? print path:', path)
            
            directions = []

            for i, room in enumerate(path[:-1]):
                direction = list(d[room].keys())[list(d[room].values()).index(path[i+1])]
                traversal_path.append(direction)
                directions.append(direction)
                # player.travel(direction)
        

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
            return traversal_path, player.current_room.id
            
        # else:
        print('traversal_path:', traversal_path)
        exits = player.current_room.get_exits()
        print('exits:', player.current_room.id, exits)
   
        for exit in exits:
            
            n = player.current_room.get_room_in_direction(exit).id
            print('exit:', n)
            print('if n not in:', path)
            if n not in path:
                new_path = list(path)
                player.travel(exit)
                print('new room:', player.current_room.id)
                new_path.append(n)
                print('new_path:', new_path)
                queue.append(new_path)
                if None:
                    return
                

    
    # return player.current_room.id, traversal_path
print(traverse(player))

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []
# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
