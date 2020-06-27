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
    
    return traversal_path
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
