## Name spaces
### Python
Python implements most namespaces as dictionaries. Namespaces in Python are created at different moments and have different lifetimes. The namespace containing Python's built-in names is created when the interpreter starts up and is never deleted. The global namespace for a specific module is created when its definition is read in and typically persists until the interpreter quits. Namespaces read from a script file or created interactively are part of a module called \_\_main\_\_ and have their own global namespace. Namespaces for functions are created when the function is called and deleted when the function returns false or raises an exception that can't be handled within the function.

Namespaces are imported into Python scripts using
```
import <namespace>
```
and are accessed using the '.' operator.

The following is a code snippet showing how Python's namespace implementation translates to textual scope:

```
def scope_test():
def do_local():
    spam = "local spam"

def do_nonlocal():
    nonlocal spam
    spam = "nonlocal spam"

def do_global():
    global spam
    spam = "global spam"

spam = "test spam"
do_local()
print("After local assignment:", spam)
do_nonlocal()
print("After nonlocal assignment:", spam)
do_global()
print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Outputs:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
### C#
In C# namespaces are implemented by organizing code within C# assemblies, which act as a fundamental unit of physical code grouping for a program. In comparison to Python, C# namespaces are activated with the 'Using' keyword and require more explicitness to use them. For instance, the built-in C# namespace is not automatically imported into programs - it must be included with a 'Using System' command. In addition, you can explicitly define your own namespaces within a C# file using the 'namespace' command, and you can nest these as much as you want within a file. Like Python, namespace members are accessed using the '.' operator.
The following is a code snippet showing how C# namespaces can be nested together and how they are accessed:
```
namespace SampleNamespace
{
    class SampleClass
    {
        public void SampleMethod()
        {
            System.Console.WriteLine(
              "SampleMethod inside SampleNamespace");
        }
    }

    // Create a nested namespace, and define another class.
    namespace NestedNamespace
    {
        class SampleClass
        {
            public void SampleMethod()
            {
                System.Console.WriteLine(
                  "SampleMethod inside NestedNamespace");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Displays "SampleMethod inside SampleNamespace."
            SampleClass outer = new SampleClass();
            outer.SampleMethod();

            // Displays "SampleMethod inside SampleNamespace."
            SampleNamespace.SampleClass outer2 = new SampleNamespace.SampleClass();
            outer2.SampleMethod();

            // Displays "SampleMethod inside NestedNamespace."
            NestedNamespace.SampleClass inner = new NestedNamespace.SampleClass();
            inner.SampleMethod();
        }
    }
}
```