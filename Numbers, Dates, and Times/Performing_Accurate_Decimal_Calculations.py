# coding=utf-8

"""
Problem

You need to perform accurate calculations with decimal numbers, and don’t want the small errors that 
naturally occur with floats.

Solution

A well-known issue with floating-point numbers is that they can’t accurately represent all base-10 
decimals. Moreover, even simple mathematical calculations introduce small errors. For example:
"""
a = 4.2
b = 2.1
print(a + b)
# 6.300000000000001
print((a + b) == 6.3)
# False

"""
These errors are a "feature" of the underlying CPU and the IEEE 754 arithmetic performed by its 
floating-point unit. Since Python’s float data type stores data using the native representation, 
there’s nothing you can do to avoid such errors if you write your code using float instances.

If you want more accuracy (and are willing to give up some performance), you can use the decimal module:
"""
from decimal import Decimal
a2 = Decimal('4.2')
b2 = Decimal('2.1')
a2 + b2
# Returns Decimal('6.3')
print(a2 + b2)
# 6.3
print((a2 + b2) == Decimal('6.3'))
# True

"""
At first glance, it might look a little weird (i.e., specifying numbers as strings). However, Decimal 
objects work in every way that you would expect them to (supporting all of the usual math operations, 
etc.). If you print them or use them in string formatting functions, they look like normal numbers.

A major feature of decimal is that it allows you to control different aspects of calculations, including 
number of digits and rounding. To do this, you create a local context and change its settings. 
For example:
"""
from decimal import localcontext
a3 = Decimal('1.3')
b3 = Decimal('1.7')
print(a3 / b3)
# 0.7647058823529411764705882353
with localcontext() as ctx:
	ctx.prec = 3
	print(a3 / b3)
# 0.765
with localcontext() as ctx:
	ctx.prec = 50
	print(a3 / b3)
# 0.76470588235294117647058823529411764705882352941176

"""
Discussion

The decimal module implements IBM’s "General Decimal Arithmetic Specification." Needless to say, there 
are a huge number of configuration options that are beyond the scope of this book.

Newcomers to Python might be inclined to use the decimal module to work around perceived accuracy problems 
with the float data type. However, it’s really important to understand your application domain. If you’re 
working with science or engineering problems, computer graphics, or most things of a scientific nature, 
it’s simply more common to use the normal floating-point type. For one, very few things in the real 
world are measured to the 17 digits of accuracy that floats provide. Thus, tiny errors introduced 
in calculations just don’t matter. Second, the performance of native floats is significantly 
faster—something that’s important if you’re performing a large number of calculations.

That said, you can’t ignore the errors completely. Mathematicians have spent a lot of time studying 
various algorithms, and some handle errors better than others. You also have to be a little careful 
with effects due to things such as subtractive cancellation and adding large and small numbers 
together. For example:
"""
nums = [1.23e+18, 1, -1.23e+18]
sum(nums)    # Notice how 1 disappears
# Returns 0.0

"""
This latter example can be addressed by using a more accurate implementation in math.fsum():
"""
import math
math.fsum(nums)
# Returns 1.0

"""
However, for other algorithms, you really need to study the algorithm and understand its error 
propagation properties.

All of this said, the main use of the decimal module is in programs involving things such as finance. 
In such programs, it is extremely annoying to have small errors creep into the calculation. 
Thus, decimal provides a way to avoid that. It is also common to encounter Decimal objects 
when Python interfaces with databases—again, especially when accessing financial data.
"""
