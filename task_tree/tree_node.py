# Implementation of a tree-node data structure
import datetime
import pickle

from task_tree.print_dict import *

class TreeNode:
    def __init__(self, title='', data=None, next=[]):
        self.data = {
            'creation date': datetime.date.today(),
            'goal date': datetime.date.today(),
            'title': title,
            'priority': -1,
            'difficulty': -1,
            'description': ' '
        }
        self.next = next

    def __str__(self):
        to_string = 'Task: ' + str(self.data['title']) + '\t\t\t\t' \
            + 'Started: ' + str(self.data['creation date']) + '\n' \
            + 'Description: ' + str(self.data['description'][0:23]) + '... ' \
            + 'Due: ' + str(self.data['goal date'])
        return to_string

    # Add a child TreeNode
    def add(self, title):
        task = TreeNode(title, None, [])
        self.next.append(task)
        return task

    # Save the node to a pickle file
    def save(self, filename):
        p = pickle.Pickler(open( filename, "wb" ))
        p.dump(self)
        if len(self.next) > 0:
            for node in self.next:
                self._saveHelper(node, p)

    def _saveHelper(self, node, p):
        p.dump(node)
        if len(node.next) > 0:
            for next_node in node.next:
                node._saveHelper(next_node, p)

    # Load and initialize tree from pickle file
    # This doesn't really make sense to be here
    def load(filename):
        return pickle.load( open( filename, "rb" ) )

    # Depth first find function
    def find(self, title):
        if self.data['title'] == title:
            return self
        else:
            for node in self.next:
                found_node = self._findHelper(node, title)
                if found_node:
                    return found_node

            return None

    def _findHelper(self, node, title):
        if node:
            if node.data['title'] == title:
                return node
            else:
                if len(node.next) > 0:
                    for node in node.next:
                        found_node = node._findHelper(node, title)
                        if found_node:
                            return found_node

        return None

    # Print tree in order
    def printTree(self):
        print(print_dict['root'])
        if len(self.next) > 1:
            for node in self.next[:-1]:
                node._printTreeHelper(node, 0, '|', ['|'])
            node._printTreeHelper(self.next[-1], 0, '`', [' '])
        else:
            for node in self.next:
                node._printTreeHelper(node, 0, '`', [' '])

    def _printTreeHelper(self, node, level, end, indent_types):
        if len(node.next) == 0: # Leaf Node
            prefix = ''
            for i in range(level):
                prefix = prefix + indent_types[i] + '  '
            print(prefix + end + '--' + str(node.data['title']) + '(' + str(level) + ')')
        elif len(node.next) == 1:
            prefix = ''
            for i in range(level):
                prefix = prefix + indent_types[i] + '  '
            print(prefix + end + '--' + str(node.data['title']) + '(' + str(level) + ')')
            indent_types.append(' ')
            node._printTreeHelper(node.next[0], level + 1, '`', indent_types)
        else:
            prefix = ''
            for i in range(level):
                prefix = prefix + indent_types[i] + '  '
            print(prefix + end + '--' + str(node.data['title']) + '(' + str(level) + ')')
            if len(node.next[:-1]) > 0:
                for next_node in node.next[:-1]:
                    indent_types.append('|')
                    node._printTreeHelper(next_node, level + 1, '|', indent_types)
                    indent_types.pop()
                indent_types.append(' ')
                node._printTreeHelper(node.next[-1], level + 1, '`', indent_types)
                indent_types.pop()

"""
|--do the dishes
|  |--vacuum the dining room
|  `--do image proccessing hw1
|     |--look into photoshop
|     |--clean pictures
|	  `--load pictures
`--take out the trash

do the dishes
    vacuum the dining room
    do image proccessing hw1
    clean pictures
    load picture
    look into photoshop
take out the trash

"""
'''
*  # Root
|
|--branch0/		# Lvl 0: Branch
|  |--branch1/	# Lvl 1: Branch
|  |  |--leaf2	# Lvl 2: Leaf
|  |  `--leaf3	# Lvl 2: End leaf
|  `--branch2/	# Lvl 1: End Branch
|     `--leaf4	# Lvl 2: End Leaf
|--leaf0		# Lvl 0: Leaf
`--leaf1		# Lvl 0: End Leaf
'''
