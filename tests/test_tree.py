import os
import sys
import pickle
sys.path.insert(0, os.path.abspath('..'))

"""
from task_tree import tree_node

# Initialize Tree
print('Initilizing Task Tree')
tree_root = tree.TreeNode()
tree_root.printTree()

print('Adding a Task')
dishes_node = tree_root.add('Do the dishes')
tree_root.printTree()

print('Adding a Task Description')
dishes_node.data['description'] = 'plates, cups, bowls, forks, spoons, cutting board'

print('Adding to Tree')
tree_root.add('Take out the trash')
dishes_node.add('Vacuum the dining room')
image = dishes_node.add('Do image processing hw1')
photo = image.add('look into photoshop')
image_pics = image.add('clean pictures')
photo.add('load pictures')
image.add('Watch videos')
tree_root.printTree()


# Saving Tree
data_file = './data/tree_root.p'
tree_root.save(data_file)

# Loading Tree
file = open(data_file)
load_tree = pickle.load(file)

load_tree.add('Do your homework')

tree_root.printTree()
load_tree.printTree()
"""
print(os.getcwd())
from task_tree import core
