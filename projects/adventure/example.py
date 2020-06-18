path = [5,0]

# mydict = {
#     2: {'s': 1},
#     1: {'n': 2, 's': 0},
#     0: {'n': 1, 's': '?', 'e': '?', 'w': '?'}
# }

d = {
    5: {'s': 6, 'n': 0},
    0: {'n': 1, 's': '?', 'e': '?', 'w': '?'}
}

traversal_path = ['n', 'n']
print('path', path[:-1])
for i, room in enumerate([5]):
    print(list(d[room].keys()))
    direction = list(d[room].keys())[list(d[room].values()).index(path[i+1])]
    traversal_path.append(direction)
print(traversal_path)

