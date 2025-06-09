# main_script.py
#   Jason Ritt, Brown University
#
# Imports a local module to demonstrate behavior of 
# python importing.
#
# Part of the Computational Fluency Short Course 2025,
# in the Carney Institute for Brain Science at 
# Brown University.

# Importing a module runs it and attaches its namespace

print('\n--- Importing my_module --v')
import my_module
print('--- my_module imported --^\n')

my_module.message()

# Already imported modules are not run again

input('\n> Hit return to import again: ')

print('\n--- Importing my_module again --v')
import my_module
print('--- my_module imported again --^\n')

my_module.message()

# Module names do not appear automatically in this namespace

input('\n> Hit return to try message() directly: ')

try:
    message()
except:
    print('There is no function message in the top name space')

input('\n> Hit return to import message() and run it: ')

# But module names can be attached if desired

from my_module import message

try:
    message()
except:
    print('There is no function message in the top name space')

input('\n> Hit return to view and set a module attribute: ')

# Objects in a modules namespace can be accessed and changed from outside

try:
    print(x)
except:
    print('There is no x in the top namespace')

# Read in the module namespace
print(f'my_module.x has the value {my_module.x}')

# Change in the module namespace
my_module.x=25
print(f'my_module.x now has the value {my_module.x}')
