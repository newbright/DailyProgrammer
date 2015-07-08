#------------------------------------------------------------
# Challenge #214: "Chester, The Greedy Pomeranian"
# Difficulty: Hard
# May 15, 2014
# Brandon Newbright
#------------------------------------------------------------

from collections import Iterable
from operator import itemgetter
import math

class Node(list):
    def __init__(self, point, left, right):
        list.__init__(self)
        self.append(point)
        self.append(left)
        self.append(right)

# "Flattens" all lists within lists into one list
def flatten(l):
    for item in l:
        if isinstance(item, Iterable) and not isinstance(item, tuple):
            for x in flatten(item):
                yield x
        else:
            yield item

def remove(point, tree):
    new_list = list(flatten(tree))
    new_list.remove(point)
    print(new_list)
    new_list = [x for x in new_list if not x is None]
    return parse_list_to_tree(new_list)

def add(point, tree):
    new_list = list(flatten(tree))
    new_list.append(point)
    print(new_list)
    new_list = [x for x in new_list if not x is None]
    return parse_list_to_tree(new_list)

# Parses the input file into a list of 2-tuples ('points'), i.e. [(x0,y0), (x1,y1), ... , (xn,yn)]
def parse_file_to_list(filename):
    file_in = open(filename, 'r')
    point_list = [tuple(line.split(' ')) for line in file_in.read().splitlines()]
    point_list = point_list[1::]
    point_list = [(float(x), float(y)) for x, y in point_list]
    return point_list
    
# Parses a list of points into a k-d tree of Nodes
def parse_list_to_tree(point_list, depth=0):
    try:
        k = len(point_list[0])
    except IndexError as e:
        return None

    axis = depth % k

    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2

    return Node(point=point_list[median], left=parse_list_to_tree(point_list[:median], depth + 1), right=parse_list_to_tree(point_list[median + 1:], depth + 1))

def distance(p1, p2):
    abs_x = p2[0] - p1[0]
    abs_y = p2[1] - p1[1]
    return sqrt((abs_x ** 2) + (abs_y ** 2))

# Finds the nearest neighbor to 'point' in 'tree', removes and returns that neighbor's coordinates, and updates 'tree'
def nearest_neighbor(tree, point, best_guess=None):
    if best_guess == None:
        best_guess = Tree[0]


def eat_treats(tree):
    current_point = (0.5, 0.5)
    total_distance = 0.0
    while len(tree) > 1:
        next_point = nearest_neighbor(tree, current_point)
        total_distance += distance(current_point, next_point)
        current_point = next_point
    return print("Chester travelled a total of {} units,".format(str(total_distance)))

points = parse_file_to_list("input/6.txt")
print(points)
tree = parse_list_to_tree(points)
print(tree)
tree = remove((0.7, 0.7), tree)
print(tree)

print(tree[1])