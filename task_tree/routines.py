"""
Routines to be added to the core
    can be useful for testing, automating task updates,
    or stringing custom commands together

    routines are stored in a standard format dictinoary
        the keys cannot overlap with existing commands
"""

routines = {
#   'routine': [['command', 'target', 'data'], ['command', 'target', 'data']]
    'test_add': [['add', 'task1', ''], ['add', 'task2', ''], ['add', 'task3', ''],
                ['add', 'task1', 'task4'], ['add', 'task4', 'task5'], ['add', 'task3', 'task6']]
}
