## Reflection
### Python
Python supports the notion of reflection in some ways, but with some important differences. First, Python calls it introspection rather than reflection. Secondly, Python is a dynamically typed language, so some of the concepts of reflection do not translate well or simply do not make sense in that context. For example, finding the type of an object of unknown type so you can create another instance of that object at runtime makes no sense in this context because you do not need that information in a dynamically typed language. That said, Python does support reflection-like abilities via introspection and allows you to find names, types, identity numbers (to see if an object is unique), attributes, callables (methods), and whether or not an object is a subclass.
Here is an example of these methods in action inside a function named interrogate that takes any object and prints the information provided by introspection:
```
def interrogate(item):
    """Print useful information about item."""
    if hasattr(item, '__name__'):
     print "NAME:    ", item.__name__
    if hasattr(item, '__class__'):
     print "CLASS:   ", item.__class__.__name__
    print "ID:      ", id(item)
    print "TYPE:    ", type(item)
    print "VALUE:   ", repr(item)
    print "CALLABLE:",
    if callable(item):
     print "Yes"
    else:
     print "No"
    if hasattr(item, '__doc__'):
     doc = getattr(item, '__doc__')
    doc = doc.strip()   # Remove leading/trailing whitespace.
    firstline = doc.split('\n')[0]
    print "DOC:     ", firstline

interrogate('a string')     # String object
```
Output:
```
CLASS:    str
ID:       141462040
TYPE:     <type 'str'>
VALUE:    'a string'
CALLABLE: No
DOC:      str(object) -> string
```
### C#
C# supports reflection with the System.Reflection namespace which can provide a view of loaded types, methods, and fields, with the ability to dynamically create and invoke types. The following sample code shows how reflection is implemented in C#:
```
using System;
using System.Reflection;

public class MyClass
{
   public virtual int AddNumb(int numb1,int numb2)
   {
     int result = numb1 + numb2;
     return result;
   }

}

class MyMainClass
{
  public static int Main()
  {
    Console.WriteLine ("\nReflection.MethodInfo");
    // Create MyClass object
    MyClass myClassObj = new MyClass();
    // Get the Type information.
    Type myTypeObj = myClassObj.GetType();
    // Get Method Information.
    MethodInfo myMethodInfo = myTypeObj.GetMethod("AddNumb");
    object[] mParam = new object[] {5, 10};
    // Get and display the Invoke method.
    Console.Write("\nFirst method - " + myTypeObj.FullName + " returns " +  
                         myMethodInfo.Invoke(myClassObj, mParam) + "\n");
    return 0;
  }
}
```