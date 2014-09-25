# coding=utf-8

"""
Problem

You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent 
throughout the string.

Solution

The split() method of string objects is really meant for very simple cases, and does not allow for 
multiple delimiters or account for possible whitespace around the delimiters. In cases when you 
need a bit more flexibility, use the re.split() method:
"""
import re
line = 'i am; solo, and,you,      ?'
re.split(r'[;,\s]\s*', line)
# Returns ['i', 'am', 'solo', 'and', 'you', '?']

"""
Discussion

The re.split() function is useful because you can specify multiple patterns for the separator. For 
example, as shown in the solution, the separator is either a comma (,), semicolon (;), or whitespace 
followed by any amount of extra whitespace. Whenever that pattern is found, the entire match becomes 
the delimiter between whatever fields lie on either side of the match. The result is a list of fields, 
just as with str.split().

When using re.split(), you need to be a bit careful should the regular expression pattern involve a 
capture group enclosed in parentheses. If capture groups are used, then the matched text is also 
included in the result. For example, watch what happens here:
"""
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# ['i', ' ', 'am', ';', 'solo', ',', 'and', ',', 'you', ',', '?']

"""
Getting the split characters might be useful in certain contexts. For example, maybe you need the split 
characters later on to reform an output string:
"""
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
# ['i', 'am', 'solo', 'and', 'you', '?']
print(delimiters)
# [' ', ';', ',', ',', ',', '']

"""
If you don’t want the separator characters in the result, but still need to use parentheses to group 
parts of the regular expression pattern, make sure you use a noncapture group, specified as (?:...). 
For example:
"""
re.split(r'(?:,|;|\s)\s*', line)
# Returns ['i', 'am', 'solo', 'and', 'you', '?']
