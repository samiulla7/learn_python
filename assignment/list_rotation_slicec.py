
def rotate(my_list, num_rotations):
    l = len(my_list)
    if l == num_rotations:
        return my_list
    num_rotations = num_rotations if l>num_rotations else num_rotations%l
    print(num_rotations)
    m = my_list[:-num_rotations]
    n = my_list[-num_rotations:]
    return n+m

num_rotations = 3
letters = ['a', 'b', 'c', 'd', 'e']
print(rotate(letters, num_rotations))

# to create ['c', 'd', 'e', 'a', 'b']