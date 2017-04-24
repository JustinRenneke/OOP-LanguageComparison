## Classes
### Python
In Python, classes are declared simply with
```
class MyClass:
    <members>
```
and, unlike many object oriented languages, there are no access level modifiers for Python classes. You are expected simply to follow best practice guidelines to emulate access level behaviors instead of using hard coded levels.
To instantiate a class, Python uses simple function notation. The following instantiates a class called MyClass and assigns it to the variable x:
```
x = MyClass()
```
This creates an empty object with default state. To construct an object with arguments, you have to define an \_\_init\_\_ method in the class. This method acts as a stereotypical Java constructor and will automatically be invoked by instantiation statements. If you have defined
```
class MyClass:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
```
within MyClass, then
```
x = MyClass('John', 25)
```
will be the new way to instantiate the class.  
In Python, classes will automatically be deconstructed when nothing references it - there are no explicit deconstructors. You can force erasure of all references with
```
del x
```
and this will force deconstruction.
Here is a more complete [example of Python class structure](/CodeSnippets/PythonClassExample.py).
### C#
In C#, classes are defined with the pattern:
```
<access modifier> class <ClassName>
```
```
public class MyClass{
    <members>
}
```
C# access modifiers are: public, protected, private, internal, and protected internal.
New instances of a class can be instantiated in a more traditional way compared to Python, using constructors which are defined within the class.
```
public class MyClass{
    public string name;

    public MyClass(string newName){
            name = newName;
    }
}
```
Then to initialize an instance of MyClass you can call the constructor using the new keyword:
```
MyClass x = new MyClass("name");
```
In addition, C# will provide a default parameterless constructor if no constructor is defined in the class.
Destructors in C# are declared within a class, like so:
```
public class MyClass{
    ~MyClass(){
        <cleanup statements>
    }
}
```
The programmer has no control over when the deconstructors are called, they are invoked automatically by the garbage collector when the objects are no longer being used by the application or the application exits.
