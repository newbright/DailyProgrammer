#------------------------------------------------------------
# Challenge #214: "Chester, The Greedy Pomeranian"
# Difficulty: Hard
# May 15, 2014
# Brandon Newbright
#------------------------------------------------------------

from collections import namedtuple
from operator import itemgetter
from pprint import pformat
import math

class Node(namedtuple('Node','point left right')):
    def __repr__(self):
        return pformat(tuple(self))

    def remove(self, point, depth=0):
        


# Parses the input file into a list of 2-tuples ('points'), i.e. [(x0,y0), (x1,y1), ... , (xn,yn)]
def parse_points(filename):
    file_in = open(filename, 'r')
    point_list = [tuple(line.split(' ')) for line in file_in.read().splitlines()]
    point_list = point_list[1::]
    point_list = [(float(x), float(y)) for x, y in point_list]
    point_list.append((0.8, 0.5))
    return point_list
    
# Parses a list of points into a k-d tree of Nodes
def parse_tree(point_list, depth=0):
    try:
        k = len(point_list[0])
    except IndexError as e:
        return None

    axis = depth % k

    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2

    return Node(point=point_list[median], left=parse_tree(point_list[:median], depth + 1), right=parse_tree(point_list[median + 1:], depth + 1))

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



points = parse_points("input/6.txt")
print(points)
tree = parse_tree(points)
print(tree[0])