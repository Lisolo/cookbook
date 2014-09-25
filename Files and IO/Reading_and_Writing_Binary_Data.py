# coding=utf-8

"""
Problem

You need to read or write binary data, such as that found in images, sound files, and so on.

Solution

Use the open() function with mode rb or wb to read or write binary data. For example:
"""
# Read the entire file as a single byte string
with open('somefile.bin','rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f2:
    f2.write(b'Hello World')

"""
When reading binary, it is important to stress that all data returned will be in the form of byte strings, 
not text strings. Similarly, when writing, you must supply data in the form of objects that expose data as bytes 
(e.g., byte strings, bytearray objects, etc.).
"""

"""
Discussion

When reading binary data, the subtle semantic differences between byte strings and text strings pose a potential gotcha. 
In particular, be aware that indexing and iteration return integer byte values instead of byte strings. 
For example:
"""
# Text string
t = 'Hello World'
print(t[0])
# 'H'
for c in t:
    print(c)
# H
# e
# l
# l
# o
# 
# W
# o
# r
# l
# d

# Byte string
b = b'Hello World'
print(b[0])
# 72
for c in b:
    print(c)
# 72
# 101
# 108
# 108
# 111
# 32
# 87
# 111
# 114
# 108
# 100

"""
If you ever need to read or write text from a binary-mode file, make sure you remember to decode or encode it. 
For example:
"""
with open('somefile.bin', 'rb') as f3:
    data = f3.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f4:
    text = 'Hello World'
    f4.write(text.encode('utf-8'))

"""
A lesser-known aspect of binary I/O is that objects such as arrays and C structures can be used for writing 
without any kind of intermediate conversion to a bytes object. For example:
"""
import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f5:
    f5.write(nums)

"""
This applies to any object that implements the so-called "buffer interface,"  which directly exposes 
an underlying memory buffer to operations that can work with it. Writing binary data is one such operation.

Many objects also allow binary data to be directly read into their underlying memory using 
the readinto() method of files. For example:
"""
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f6:
    f6.readinto(a)
print(a)
# array('i', [0, 0, 0, 0, 0, 0, 0, 0])

"""
However, great care should be taken when using this technique, as it is often platform specific and 
may depend on such things as the word size and byte ordering (i.e., big endian versus little endian). 
See "Reading Binary Data into a Mutable Buffer" for another example of reading binary data into a mutable buffer.
"""
