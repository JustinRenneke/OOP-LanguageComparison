## Procedural programming
### Python

Because Python was designed with the purpose of readability and visual simplicity, procedural programming in Python is very straightforward:

```
def someMethod():
    return 5

def anotherMethod(number):
    return number - 10

someNumber = someMethod()
anotherNumber = anotherMethod(someNumber)
//etc
```
### C#

As a language designed primarily around the Object Oriented paradigm, C# design philosophy has very little support for procedural programming style. While looking for examples of "good" procedural programming in C#, all I found was examples of how to "fix" procedural programming in C#. The most straightforward way to write a procedural program in C# would be to start in the main method, instantiating variables and making method calls from there.

```
namespace ProceduralApp
{
    class ProceduralProgram
    {
        static void Main(string[] args)
        {
            int someNumber = someMethod(someNumber);
            int anotherNumber = anotherMethod(someNumber);
            //etc
        }
    }
}
```