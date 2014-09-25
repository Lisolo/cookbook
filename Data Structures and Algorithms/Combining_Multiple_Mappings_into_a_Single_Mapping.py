# coding=utf-8

"""
Problem

You have multiple dictionaries or mappings that you want to logically combine into a single mapping to 
perform certain operations, such as looking up values or checking for the existence of keys.

Solution

Suppose you have two dictionaries:
"""
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

"""
Now suppose you want to perform lookups where you have to check both dictionaries (e.g., first checking 
in a and then in b if not found). An easy way to do this is to use the ChainMap class from the 
collections module. For example:
"""
from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])     # Outputs 1 (from a)
print(c['y'])     # Outputs 2 (from b)
print(c['z'])     # Outputs 3 (from a)

"""
Discussion

A ChainMap takes multiple mappings and makes them logically appear as one. However, the mappings are not 
literally merged together. Instead, a ChainMap simply keeps a list of the underlying mappings and 
redefines common dictionary operations to scan the list. Most operations will work. For example:
"""
len(c)
# Returns 3
list(c.keys())
# Returns ['x', 'y', 'z']
list(c.values())
# Returns [1, 2, 3]

"""
If there are duplicate keys, the values from the first mapping get used. Thus, the entry c['z'] in the 
example would always refer to the value in dictionary a, not the value in dictionary b.

Operations that mutate the mapping always affect the first mapping listed. For example:
"""
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# {'w': 40, 'z': 10}
del c['y']
# Traceback (most recent call last):
# ...
# KeyError: "Key not found in the first mapping: 'y'"

"""
A ChainMap is particularly useful when working with scoped values such as variables in a programming 
language (i.e., globals, locals, etc.). In fact, there are methods that make this easy:
"""
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x']
# Returns 3
# Discard last mapping
values = values.parents
values['x']
# Returns 2
values = values.parents
values['x']
# Returns 1
print(values)
# ChainMap({'x': 1})

"""
As an alternative to ChainMap, you might consider merging dictionaries together using the update() method. 
For example:
"""
merged = dict(b)
merged.update(a)
merged['x']
# Returns 1
merged['y']
# Returns 2
merged['z']
# Returns 3

"""
This works, but it requires you to make a completely separate dictionary object (or destructively alter 
one of the existing dictionaries). Also, if any of the original dictionaries mutate, the changes don’t 
get reflected in the merged dictionary. For example:
"""
a['x'] = 13
merged['x']
# Returns 1

"""
A ChainMap uses the original dictionaries, so it doesn’t have this behavior. For example:
"""
merged2 = ChainMap(a, b)
merged2['x']
# Returns 13
a['x'] = 42
merged2['x']   # Notice change to merged dicts
# Returns 42
