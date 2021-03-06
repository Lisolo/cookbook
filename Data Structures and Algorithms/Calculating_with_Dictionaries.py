# coding=utf-8

"""
Problem

You want to perform various calculations (e.g., minimum value, maximum value, sorting, etc.) 
on a dictionary of data.

Solution

Consider a dictionary that maps stock names to prices:
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

"""
In order to perform useful calculations on the dictionary contents, it is often useful to invert 
the keys and values of the dictionary using zip(). For example, here is how to find the minimum 
and maximum price and stock name:
"""
min_price = min(zip(prices.values(), prices.keys()))
# min_prices is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

"""
Similarly, to rank the data, use zip() with sorted(), as in the following:
"""
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

"""
When doing these calculations, be aware that zip() creates an iterator that can only be consumed once. 
For example, the following code is an error:
"""
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))   #OK
print(max(prices_and_names))   #ValueError: max() arg is an empty sequence

"""
If you try to perform common data reductions on a dictionary, you’ll find that they only process the keys, 
not the values. For example:
"""
min(prices)   # Returns 'APPL'
max(prices)   # Returns 'IBM'

"""
This is probably not what you want because you’re actually trying to perform a calculation involving the 
dictionary values. You might try to fix this using the values() method of a dictionary:
"""
min(prices.values())   # Returns 10.75
max(prices.values())   # Returns 612.78

"""
Unfortunately, this is often not exactly what you want either. For example, you may want to know 
information about the corresponding keys (e.g., which stock has the lowest price?).

You can get the key corresponding to the min or max value if you supply a key function to min() 
and max(). For example:
"""
min(prices, key=lambda k: prices[k])   # Returns 'FB'
max(prices, key=lambda k: prices[K])   # Returns 'AAPL'

"""
However, to get the minimum value, you’ll need to perform an extra lookup step. For example:
"""
min_value = prices[min(prices, key=lambda k: prices[k])]   # Returns 10.75

"""
The solution involving zip() solves the problem by "inverting" the dictionary into a sequence 
of (value, key) pairs. When performing comparisons on such tuples, the value element is compared 
first, followed by the key. This gives you exactly the behavior that you want and allows reductions 
and sorting to be easily performed on the dictionary contents using a single statement.

It should be noted that in calculations involving (value, key) pairs, the key will be used to determine 
the result in instances where multiple entries happen to have the same value. For instance, 
in calculations such as min() and max(), the entry with the smallest or largest key will be returned 
if there happen to be duplicate values. For example:
"""
prices2 = {'pen': 10.86, 'ruler': 10.86}
min(zip(prices2.values(), prices2.keys()))   # Returns (10.86, 'pen')
max(zip(prices2.values(), prices2.keys()))   # Returns (10.86, 'ruler')
