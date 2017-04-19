# __OOP Langage Comparison: Python vs C#__

* ## Language purpose/genesis  
	### Python
	Python was created by Guido van Rossum in 1991. Its purpose was to introduce a syntax that would emphasize code readability by using whitespace indentation instead of curly braces or keywords, as well as simplify and speed up development over the other languages that were available at the time such as C++ and Java.
	### C#
	C# was created by a team at Microsoft and first released in 2000. C# was created because Microsoft needed an object oriented programming language to support the .NET framework they were developing in the late 1990s. Microsoft was initially using Java, but Sun wouldn't allow Microsoft to make the changes it needed, so Microsoft created C# so they could have full control of the language. In the early years of C# the language was very similar to Java and received much criticism for being a copy cat, but as time went on Java and C# began to diverge as they implemented different features in different ways.
* ## Unique features of the language
	### Python
	Python doesn't really have any features that are completely unique across all languages - even its use of whitespace for structure can be seen in Haskell. However, the combination of many of its features gives it a unique power to increase productivity and ease of prototyping. It is widely agreed that, while it may be lacking in some areas of performance when compared to other object oriented languages, it is the best language for rapidly prototyping software using fewer lines of code and having fantastic readability. That said, Python includes some features that are somewhat special such as: use of indentation; interactive interpreter; collections being first class; functions being first class; and use of generators and coroutines.
	### C#
	C# could be said to be unique in the fact that at first it was nearly a straight copy of Java - most programming languages are created with some goal of improving on previous languages or adding new features. Eventually C# began to diverge from Java and has come to incorporate some special features including: assemblies; cross-language compatibility being first class (Common Language Runtime); properties, listeners, and foreign methods (extension methods) being first class; and use of partial classes.

* ## Name spaces
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
	In C# namespaces are implemented by organizing code within C# assemblies, which act as a fundamental unit of physical code grouping for a program. In comparison to Python, C# namespaces require more explicitness to use them. For instance, the built-in C# namespace is not automatically imported into programs - it must be included with a 'Using System' command. In addition, you can explicitly define your own namespaces within a C# file using the 'namespace' command, and you can nest these as much as you want within a file. Like Python, namespace members are accessed using the '.' operator.
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
* ## Types
	### Python
	The type system in Python uses implicit typing with dynamic type checking. This means you don't have to declare a type when declaring a variable. Python supports the following types: booleans, integers, longs, floats, complex numbers, strings, bytes, byte arrays, lists, tuples, sets, frozen sets, and dictionaries. All types are Python are reference types, the major difference between types is whether or not they are mutable. In Python, the numeric types, strings, tuples, and frozen sets are immutable. You can also create new value types that you define yourself.
	### C#
	C# is a statically typed, strongly-typed language like C where all variables must be of a declared type. C# supports the following built-in data types: boolean, byte, signed byte, character, decimal, double, float, integer, unsigned integer, long, unsigned long, object, short, unsigned short, and string. Again, as in C, both reference types and value types are supported with most of the built-in data types listed above being treated as value types. You can create new value types in C#, but they have some constraints as they are based on a C# object - ValueType.
* ## Classes
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

* ## Instance reference name in data type (class)
	### Python

	### C#
	* this? self?
* ## Properties
	### Python

	### C#
	* Getters and setters...write your own or built in?
	* Backing variables?
	* Computed properties?
* ## Interfaces / protocols
	### Python

	### C#
	* What does the language support?
	* What abilities does it have?
	* How is it used?
* ## Inheritance / extension
	### Python

	### C#
	* Reflection
	* What reflection abilities are supported?
	* How is reflection used?
* ## Memory management
	### Python

	### C#
	* How is it handled?
	* How does it work?
	* Garbage collection?
	* Automatic reference counting?
* ## Comparisons of references and values
	### Python

	### C#
	* How are values compared? (i.e. comparing two strings)
* ## Null/nil references
	### Python

	### C#
	* Which does the language use? (null/nil/etc)
	* Does the language have features for handling null/nil references?
* ## Errors and exception handling
	### Python

	### C#
* ## Lambda expressions, closures, or functions as types
	### Python

	### C#
* ## Implementation of listeners and event handlers
	### Python

	### C#
* ## Singleton
	### Python

	### C#
	* How is a singleton implemented?
	* Can it be made thread-safe?
	* Can the singleton instance be lazily instantiated?
* ## Procedural programming
	### Python

	### C#
	* Does the language support procedural programming?
* ## Functional programming
	### Python

	### C#
	* Does the language support functional programming?
* ## Multithreading
	### Python

	### C#
	* Threads or thread-like abilities
	* How is multitasking accomplished?
