import pickle
from task_tree.tree_node import TreeNode

class Commands():
  def __init__(self):
    self.trees = []
    print('Loading...')
    print()

  def help(self, target, data):
    print('[help]:\tprints list of commands and input format descriptions')
    print('\t[target]: N/A \n\t[data]: N/A')

    print('[quit]:\tend the program')
    print('\t[target]: N/A \n\t[data]: N/A')

    print('[save]:\tsave the target tree to the given file')
    print('\t[target]: task tree to save to file\n\t[data]: file to save to')

    print('[load]:\tload the task tree from the target file')
    print('\t[target]: file to load task tree from, "all" to load all trees from the data directory\n\t[data]: N/A')

    print('[add]:\tadd a task to the target parent task')
    print('\t[target]: title of the parent task to add to, if left blank, will create a new tree \n\t[data]: title of the task to add')

    print('[delete]:delete the target task (and all children tasks)')
    print('\t[target]:target task to delete \n\t[data]: N/A')

    print('[edit]: edit the target task')
    print('\t[target]: target task to edit \n\t[data]: N/A')

  def quit(self, target, data):
    print('Closing Task Tree')

  def save(self, target, data):
    print('Saving Task Tree ' + target + ' to file ' + data)

  def load(self, target, data):
    # load task and store file name) load
    file = open(target, 'rb')
    task_tree = pickle.load(file)
    if tree.data['title']:
        print('Loading Task Tree ' + tree.data['title'] + ' from file ' + target)
    else:
        print('Load failed')
    tree.printTree()
    print()

  def add(self, target, data):
    print('adding')
    if data:
        print('try to add to existing tree')
        for tree in self.trees:
        # need to recursively search tree for the target
            found_node = tree.find(target)
            if found_node:
                print('Found the target, adding...')
                new_node = found_node.add(data)
                return new_node
            else:
                print('Failed to find target task')
    else:
    # Create new tree
        new_root = TreeNode(len(self.trees))
        self.trees.append(new_root)
        new_root.add(target)
        print()
        return new_root

  def delete(self, target, data):
    print('deleting')


  def edit(self, target, data):
    print('editing')

  def list(self, target, data):
      for tree in self.trees:
          tree.printTree()

# Functions that will be valid inputs
commands = Commands()
command_funcs = {
  'help'     : commands.help,
  'quit'    : commands.quit,
  'save'    : commands.save,
  'load'    : commands.load,
  'add'    : commands.add,
  'delete'  : commands.delete,
  'edit'    : commands.edit,
  'list'    : commands.list
}
