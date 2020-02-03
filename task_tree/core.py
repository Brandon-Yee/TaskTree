# Main module for running the program

#from commands import command_funcs
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from task_tree.commands import *
from task_tree.routines import *

print(' ----- Welcome to Task Tree -----')
user_in = input('Please enter a command "[command] [target] [data]" \n' + \
                'or type "help" for a list of commands:\n').lower().split(' ', 3)

command = user_in[0] if len(user_in) > 0 else None
target 	= user_in[1] if len(user_in) > 1 else None
data	= user_in[2] if len(user_in) > 2 else None

while command != 'quit':
    try:
        print()
        func_return = command_funcs[command](target, data)
        command_funcs['list'](None, None)
        print()
    except KeyError:
        print('Command not found')
        print('Searching routines')
        routine_return = routines[command]
        for task in routine_return:
            print(task)
            command_funcs[task[0]](task[1], task[2])
            command_funcs['list'](None, None)
            print()

        print()
    user_in = input('Please enter a command "[command] [target] [data]" \n' + \
                    'or type "help" for a list of commands:\n').lower().split(' ', 3)

    command = user_in[0] if len(user_in) > 0 else None
    target 	= user_in[1] if len(user_in) > 1 else None
    data	= user_in[2] if len(user_in) > 2 else None
