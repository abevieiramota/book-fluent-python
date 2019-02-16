# My notes

## ch01  

* line breaks are ignored inside pairs of `[], {}, or ()`
* if genexp is the single argument in a function call -> no need of enclosing parentheses

## ch02

* `len(l[x:y]) = y - x`
* `[[]] * 3` is a list of 3 references to the same inner list
* repeated concatenation of immutable sequences is inefficient
* bisect -> lo and hi parameters define the region to be searched
* bisect = bisect_right
* memoryview class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes
* collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends
* deque append/popleft are atomic -> safe to multithreading