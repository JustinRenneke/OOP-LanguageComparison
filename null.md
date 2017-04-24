## Null/nil references
### Python
Python uses 'None' for null/nil values. The only notable thing about handling null references in Python is that, since 'None' is actually an instantiated singleton object in Python, you can compare values to None in two ways:
```
if value == None:	# traditional way
    do stuff

if value is None:	# Pythonic way
    do stuff
```
There is no null pointer exception in Python; instead when an unexpected null is encountered, a TypeError or ValueError will be raised and must be handled.
### C#
C# uses the 'null' keyword. In the newest version of C#, there is the typical way for checking if an object is null and there is a new feature known as monadic null checking. Here is what they look like in comparison:
```
// Old way
if (points != null) {
    var next = points.FirstOrDefault();
    if (next != null && next.X != null) return next.X;
}   
return -1;

// New way with monadic null checking
var bestValue = points?.FirstOrDefault()?.X ?? -1;
```
This new '?.' syntactic sugar allows for more efficient null checking before accessing properties or methods.