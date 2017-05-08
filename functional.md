## Functional programming

Both Python and C# allow functions to be passed as arguments, which is critical to functional programming. 

### Python

Because Python is multiparadigm language, it is capable of functional programming and can mix functional programming with other styles of programming. 
Originally, Python lacked a significan number of tools associated with functional programming styles. The introduction of the **functools** module starting in Python 2.5 (released in 2006), begun adding these tools, which now include reduce(), which applies a function of two arguments cumulatively to the items of iterable to reduce the iterable to a single value, and partial(), which is an implementation of ["Currying"](https://en.wikipedia.org/wiki/Currying). Python also supports list comprehension, which can implement the same logic as map and filter functions commonly used in functional programming.


(example below from *Functional Programming in Python* by David Mertz, available [here](http://www.oreilly.com/programming/free/functional-programming-python.csp))
```
# Classic "FP-style"
transformed = map(tranformation, iterator)
# Comprehension
transformed = (transformation(x) for x in iterator)
# Classic "FP-style"
filtered = filter(predicate, iterator)
# Comprehension
filtered = (x for x in iterator if predicate(x))
```

### C# 

in .net 2.0, the concept of *predicates* was introduced. A predicate is a function that determines if a a value meets a certain criteria and returns a boolean indicating the result. Predicates are usually lambda funcitons, but can be any static function. This design concept is powerful because it allows more general functions to be reused for different specific uses by supplying different predicates. An example on [CodeProject.com](https://www.codeproject.com/Articles/375166/Functional-programming-in-Csharp#HOF) illustrates this by showing a generic counting function:
```
public static int Count<T>(T[] arr, Predicate<T> condition)
{
    int counter = 0;
    for (int i = 0; i < arr.Length; i++)
        if (condition(arr[i]))
            counter++;
    return counter;
}
```
and a variety of applications suppying different predicates:
```
Predicate<string> longWords = delegate(string word) { return word.Length > 10; };
int numberOfBooksWithLongNames = Count(words, longWords);
int numberOfCheapbooks = Count(books, delegate(Book b) { return b.Price< 20; });
int numberOfNegativeNumbers = Count(numbers, x => x < 0);
int numberOfEmptyBookTitles = Count(words, String.IsNullOrEmpty);
```

C# also comes with a extension called LINQ (short for Language Integrated Query), a component of the .NET framework. LINQ contains many useful list processing functions that accept predicates as arguments. 