## Comparisons of references and values
### Python
In Python variables are compared by value using the typical '==' operator. You can compare variables by reference using the 'is' command. Example:
```
x = 1.2
y = 1.2
x is y	# this compares by reference and returns false because they have different IDs
x == y	# this returns true
```
Note: for some variables such as integers from -5 to 256 and strings, Python will automatically make duplicate variables point to the same object for performance optimization which in that case renders the 'is' command obsolete. This is known as 'interning.'
### C#
C# makes use of the ReferenceEquals() function to see if 2 objects refer to the same instance. In other words, this compares the object references for equality to see if they point to the same object in memory.

Value equality is checked with the usual '==' notation.

Strings are properly compared using
```
String.Compare(string1, string2);
```
It's also worth noting that strings are interned in C# just as they are in Python - trying to compare two different copies of the same string with ReferenceEquals() will return the same reference value.