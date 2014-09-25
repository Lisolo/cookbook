#coding=utf-8

"""
Problem

You want to output data using print(), but you also want to change the separator character or line ending.

Solution

Use the sep and end keyword arguments to print() to change the output as you wish. For example:
"""
print('ACME', 50, 91.5)
# ACME 50 91.5
print('ACME', 50, 91.5, sep=',')
# ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n')
# ACME,50,91.5!!

"""
Use of the end argument is also how you suppress the output of newlines in output. For example:
"""
for x in range(5):
    print(x)
# 0
# 1
# 2
# 3
# 4
for x in range(5):
    print(x, end=' ')
# 0 1 2 3 4 >>>

"""
Discussion

Using print() with a different item separator is often the easiest way to output data when you need 
something other than a space separating the items. Sometimes you’ll see programmers using str.join() 
to accomplish the same thing. For example:
"""
print(','.join('ACME','50','91.5'))
# ACME,50,91.5

"""
The problem with str.join() is that it only works with strings. 
This means that it’s often necessary to perform various acrobatics to get it to work. For example:
"""
row = ('ACME', 50, 91.5)
print(','.join(row))
# Traceback (most recent call last):
#   File "<stdin>", line 49, in <module>
# TypeError: sequence item 1: expected string, int found
print(','.join(str(x) for x in row))
# ACME,50,91.5

"""
Instead of doing that, you could just write the following:
"""
print(*row, sep=',')
# ACME,50,91.5
