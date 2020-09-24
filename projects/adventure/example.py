path = [2,1,0]

mydict = {
    2: {'s': 1},
    1: {'n': 2, 's': 0},
    0: {'n': 1, 's': '?', 'e': '?', 'w': '?'}
}
traversal_path = ['n', 'n']
for i, room in enumerate(path[:-1]):
    direction = list(mydict[room].keys())[list(mydict[room].values()).index(path[i+1])]
    traversal_path.append(direction)
print(traversal_path)
