## Memory management
### Python
Memory management in Python varies slightly based on which implementation we are talking about. There are many under-the-hood implementations of Python such as CPython, Jython, PyPy, etc. The reference implementation, CPython, automatically manages memory within a private heap containing all Python objects and data structures. The Python memory manager manages this private heap, with different modules of the manager handling different types. Memory is allocated for an integer in a different way than for a string, for example, to maximize performance and memory usage. Python uses automatic garbage collection which tracks object references and automatically garbage collects items when there are no more references to it. The programmer cannot directly free memory allocated to an object, but can force an object to be garbage collected by deleting all references to it and then forcing the garbage collector to run. Example:
```
import gc			#import the garbage collector so we can explicitly call it
object = MyClass()	#instantiate
del object			#delete references to force collection
gc.collect() 		#force garbage collection
```
### C#
C# memory is handled on a managed heap. C# does automatic memory management which is implemented via garbage collection. When the C# garbage collector starts to run, it makes the assumption that all objects in the C# heap are garbage then starts walking the roots and building a graph of objects that are reachable. Any object that doesn't show up in one of the root graphs is considered to be garbage. So, if an object is no longer accessible other than by its destructor, that object becomes eligible for destruction. Once an object becomes eligible, at some unspecified time later, its destructor will be called and the item will become eligible for garbage collection. After that, again at some unspecified future point, the destructed object is garbage collected. There is no predictable order in which eligible objects are collected. Similar to CPython, the programmer cannot directly free an object from memory, but can request that garbage collection occur using static methods imported from System.GC.
