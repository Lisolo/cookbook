# coding=utf-8

"""
Problem

You want to organize your code into a package consisting of a hierarchical collection of modules.

Solution

Making a package structure is simple. Just organize your code as you wish on the file-system and make sure that 
every directory defines an __init__.py file. For example:

   graphics/
        __init__.py
        primitive/
             __init__.py
             line.py
             fill.py
             text.py
        formats/
             __init__.py
             png.py
             jpg.py
"""

"""
Once you have done this, you should be able to perform various import statements, such as the following:

import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg
"""

"""
Discussion

Defining a hierarchy of modules is as easy as making a directory structure on the filesystem. 
The purpose of the __init__.py files is to include optional initialization code that runs as different levels of a package are encountered. 
For example, if you have the statement import graphics, the file graphics/__init__.py will be imported and form the contents of the graphics namespace. 
For an import such as import graphics.formats.jpg, the files graphics/__init__.py and graphics/formats/__init__.py will both be imported prior 
to the final import of the graphics/formats/jpg.py file.

More often that not, it’s fine to just leave the __init__.py files empty. 
However, there are certain situations where they might include code. 
For example, an __init__.py file can be used to automatically load submodules like this:

# graphics/formats/__init__.py

from . import jpg
from . import png
"""

"""
For such a file, a user merely has to use a single import graphics.formats instead of a separate import 
for graphics.formats.jpg and graphics.formats.png.

Other common uses of __init__.py include consolidating definitions from multiple files into a single logical namespace, 
as is sometimes done when splitting modules. This is discussed in “Splitting a Module into Multiple Files”.

Astute programmers will notice that Python 3.3 still seems to perform package imports even if no __init__.py files are present. 
If you don’t define __init__.py, you actually create what’s known as a "namespace package," 
which is described in “Making Separate Directories of Code Import Under a Common Namespace”. 
All things being equal, include the __init__.py files if you’re just starting out with the creation of a new package.
"""