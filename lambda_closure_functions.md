## Lambda expressions, closures, or functions as types

### Lambda Expressions
#### Python

Python supports Lambda expressions defined as anonymous by using the lambda keyword. 
```
anArray = [2, 3, 5, 7, 11]

print map(lambda x : x * 2, anArray)
> [4, 6, 10, 14, 22]
```
Anonymous functions can be assigned to variables:
```
f = lambda x : x + 5
print f(4)
> 9
```
Python does *not* support multi-statement lambdas. A lambda expression must be a single statement. 

#### C#

C# uses the **=>** operator to define an anonymous lambda function
```
int[] anArray = {2, 3, 5, 7, 11};

Console.WriteLine("[{0}]", string.Join(", ", anArray.Select(x => x*2)));
> [4, 6, 10, 14, 22]
```

A lambda can be assigned to a Func data type of the appropriate argument and result types:
```
int[] anArray = {2, 3, 5, 7, 11};
Func<int, int> aFunc = x => x + 5;
Console.WriteLine("[{0}]", string.Join(", ", anArray.Select(aFunc)));
> [7, 8, 10, 12, 16]
```

### Closures

#### Python

Python support of closures was introduced in Python 2.2, released in December of 2001
```
def funcWithClosure(input):
    def closure(otherInput):
        return input * otherInput
    return closure

multiplyByFive = funcWithClosure(5)
print multiplyByFive(4)
> 20
```

#### C#

C# supports closures, but isn't big fan of local methods, so the implementation requires assignement to func data types.

```
public static Func<int, int> funcWithClosure(int input){
    Func<int, int> closure =  (otherInput) => input * otherInput;

    return closure;
}

public static void Main(string[] args)
{
    Func<int, int> multiplyByFive = funcWithClosure(5);
    Console.WriteLine(multiplyByFive(4));
}

> 20
```

### Functions as Types

As seen in the examples above, both Python and C# support functions as types. Because Python is a dynamically typed language, and C# is primarily a staticly typed language, there are differences in the implementation and syntax. But functionally (ha!), they both have the same capabilities. 