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
	Because Python doesn't have access levels, the 'Pythonic Way' would be to not use getters or setters. When you want to access a class member, you simply use the '.' operator. You can, however, mimic getter and setter behavior in Python if you wish to for design purposes. The most popular approach is to use the @property decorator to wrap a function and then mimic getter or setter functionality within.
	### C#
	C# makes use of backing variables which actually store member values. Example:
	```
	public class MyClass{
		private string name;
		public string Name
		{
	    	get { return name; }
	    	set { name = value; }
		}
	}
	```
	Now, if you do
	```
	MyClass.Name = "Bob";
	```
	"Bob" will be stored in the private string, name.

	C# will automatically set backing variables if you use the automatic property functionality to create getters and setters for class members like so:
	```
	public class myClass{
		public string Name {get; set;}
	}
	```
	This is equivalent to declaring a private member 'name' with explicit getters and setters as shown in the first snippet.

* ## Interfaces / protocols
	### Python
	In Python, interfaces are not strictly necessary as they are in a language like C# or Java because Python has multiple inheritance and ducktyping. However, later versions of Python introduced Abstract Base Classes which can stand in as an interface for design purposes, or you can implement pseudo interfaces by using NotImplementedError exception checks.

	Here is an example of an Abstract Base Class acting as an interface:
	```
	from abc import ABCMeta, abstractmethod

	class IInterface:
	    __metaclass__ = ABCMeta

	    @classmethod
	    def version(self): return "1.0"
	    @abstractmethod
	    def show(self): raise NotImplementedError

	class MyServer(IInterface):
	    def show(self):
	        print 'Hello, World 2!'

	class MyBadServer(object):
	    def show(self):
	        print 'Damn you, world!'


	class MyClient(object):

	    def __init__(self, server):
	        if not isinstance(server, IInterface): raise Exception('Bad interface')
	        if not IInterface.version() == '1.0': raise Exception('Bad revision')

	        self._server = server


	    def client_show(self):
	        self._server.show()


	# This call will fail with an exception
	try:
	    x = MyClient(MyBadServer)
	except Exception as exc:
	    print 'Failed as it should!'

	# This will pass with glory
	MyClient(MyServer()).client_show()
	```
	### C#
	C# supports traditional Java-like interfaces which contain abstract methods that must be defined by any class the implements the interface. An interface is declared using the interface keyword like so:
	```
	interface IEquatable<T>
    {
        bool Equals(T obj);
    }
	```
	And any class that implements the IEquatable interface must define the Equals function. C# interfaces allow classes to include behavior from multiple sources, which would not otherwise be possible because C# only supports single class inheritance.

	C# Interfaces can contain methods, properties, events, indexers, or any combination of those four member types. An interface can't contain constants, fields, operators, instance constructors, destructors, or types. Interface members are automatically public, and they can't include any access modifiers. Members also can't be static.

	C# interfaces are like abstract classes: any class that implements an interface must implement all of its members and interfaces cannot be instantiated directly.

	[Example of the implementation of the IEquatable interface from above.](/CodeSnippets/CSharpInterfaceExample.cs).
* ## Inheritance / extension
	### Python
	Python supports single and multiple inheritance. Single inheritance looks like this:
	```
	class DerivedClassName(BaseClassName):
	    <statement-1>
	    .
	    .
	    <statement-N>
	```
	and multiple inheritance looks like this:
	```
	class DerivedClassName(Base1, Base2, Base3):
	    <statement-1>
	    .
	    .
	    <statement-N>
	```

	### C#
	C# allows only single inheritance. In code, it looks like this:
	```
	public class DerivedClassName : BaseClassName
	{
		<statement-1>
		.
		.
		<statement-N>
	}
	```
* ## Reflection
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
* ## Memory management
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

* ## Comparisons of references and values
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
* ## Null/nil references
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
* ## Errors and exception handling
	### Python
	Python has an error and exception handling system based on try...except statements. A program may 'try' to execute a block of code, but if it fails for some reason, it can raise an exception which can be caught in an 'except' block. Exceptions can be raised upward through the call chain to be handled at higher levels of the program using the 'raise' functionality. All exceptions are classes derived from the Exception class and you can define your own subclasses of Exception. There is also an optional 'else' clause that can be added to the end of try...except statements that can be used for code that must be executed if the try clause does not raise an exception. In addition, Python offers the 'finally' clause to excecute code no matter what. Example of the system:
	```
	try:
	   	#You try to do your operations here
	except ExceptionI:
	   	#If there is ExceptionI, then execute this block.
	except ExceptionII:
	   	#If there is ExceptionII, then execute this block.
	else:
	   	#If there is no exception then execute this block.
	finally:
		#Execute this code whether an exception occured or not
	```
	In addition, Python uses 'assertions' to allow programmers to verify the validity of input and output. Example:
	```
	assert (number >= 0),"Negative number!"
	```
	In this example, if number is negative, the string will be printed and an AssertionError will be raised.
	If exceptions are not handled, the program terminates.
	### C#
	C# exception handling is based on try/catch blocks and offer the ability to execute code whether or not an exception was raised using the 'finally' clause. Example:
	```
	try
	{
	   // statements causing exception
	}
	catch( ExceptionName e1 )
	{
	   // error handling code
	}
	catch( ExceptionName eN )
	{
	   // error handling code
	}
	finally
	{
	   // clean up
	}
	```
	All exceptions are classes derived from the System.Exception class and you can define your own subclasses of System.Exception.
	C# also has the 'throw' statement which allows the programmer to choose to throw a specific type of exception. Example:
	```
	static int GetNumber(int index)
        {
            int[] nums = { 300, 600, 900 };
            if (index > nums.Length)
            {
                throw new IndexOutOfRangeException();
            }
            return nums[index];

        }
	```
* ## Lambda expressions, closures, or functions as types
	### Python

	### C#
* ## Implementation of listeners and event handlers
	### Python
	Python does not have listeners or event handlers by default. It is up to the programmer to implement for themselves (using, for example, Observer patterns), or to import a library that will add the functionality.
	### C#
	C# has one of the richest event systems of any object oriented language. C# uses a system of events, listeners, delegates, and publish-subscribe patters to handle events and notifications. If you know anything about object oriented languages, events, listeners, and publish-subscribe are self-explanatory. Delegates, however, are a special feature of C#. Delegates provide a functionality similar to function pointers from C. They are an improved version, however, as they allow you to execute a list of multiple functions referenced by a single delegate with one line of code. Delegates are ideally suited for use as events — notifications from one component to "listeners" about changes in that component, so they are often used in conjunction with the wider event system.

	A code snippet can provide the best explanation of the interactions of this complicated system.

	In the below snippet, a Metronome class creates events at a rate of one every 3 seconds, and a Listener class hears the metronome ticks by 'Subscribing' to the delegate and prints "HEARD IT" to the console every time it receives an event.
	```
	using System;
	namespace example
	{
	    public class Metronome
	    {
	        public event TickHandler Tick;
	        public EventArgs e = null;
	        public delegate void TickHandler(Metronome m, EventArgs e);
	        public void Start()
	        {
	            while (true)
	            {
	                System.Threading.Thread.Sleep(3000);
	                if (Tick != null)
	                {
	                    Tick(this, e);
	                }
	            }
	        }
	    }
	        public class Listener
	        {
	            public void Subscribe(Metronome m)
	            {
	                m.Tick += new Metronome.TickHandler(HeardIt);
	            }
	            private void HeardIt(Metronome m, EventArgs e)
	            {
	                System.Console.WriteLine("HEARD IT");
	            }

	        }
	    class Test
	    {
	        static void Main()
	        {
	            Metronome m = new Metronome();
	            Listener l = new Listener();
	            l.Subscribe(m);
	            m.Start();
	        }
	    }
	}
	```
* ## Singleton
	### Python
	There are multiple ways to implement a singleton in Python based on one of the following: tag it with a decorator, create it as a base class, use a metaclass, and more.

	The following snippet is an example of singleton implementation using a decorator:
	```
	def singleton(class_):
		instances = {}
		def getinstance(*args, **kwargs):
		if class_ not in instances:
		instances[class_] = class_(*args, **kwargs)
		return instances[class_]
		return getinstance

	@singleton
	class MyClass(BaseClass):
		pass
	```
	This method of creating a singleton using decorators can also be made thread-safe and lazily instantiable.

	[See an example](/CodeSnippets/PythonSingleton.py) of a thread-safe, lazily instantiable singleton class.

	### C#
	In comparison to Python, C# supports singletons without having to jump through so many hoops thanks to enforced access levels.

	The following code implements a singleton by using a private constructor that is thread-safe and can be lazily instantiated.
	```
	public sealed class Singleton
	{
	    private Singleton()
	    {
	    }

	    public static Singleton Instance { get { return Nested.instance; } }

	    private class Nested
	    {
	        // Explicit static constructor to tell C# compiler
	        // not to mark type as beforefieldinit
	        static Nested()
	        {
	        }

	        internal static readonly Singleton instance = new Singleton();
	    }
	}
	```
* ## Procedural programming
	### Python
	https://blog.newrelic.com/2015/04/01/python-programming-styles/
	### C#
	* Does the language support procedural programming?
* ## Functional programming
	### Python

	### C#
	* Does the language support functional programming?
* ## Multithreading
	### Python
	Python cannot offer true multithreading in the base Python implementation because of global interpreter lock. Instead, 'threads' in base Python perform interleaving and are useful to speed up heavy I/O operations, but they cannot perform actual parallel processing in the way that is typically assumed when talking about threading.

	However, newer versions of Python support a multiprocessing library that provides an API that allows the programmer to more easily spawn multiple Python processes to get the true parallel benefits of multitasking.

	Simple example of spawning processes:
	```
	from multiprocessing import Process

	def f(name):
	    print 'hello', name

	if __name__ == '__main__':
	    p = Process(target=f, args=('bob',))
	    p.start()
	    p.join()
	```
	### C#
	In contrast, C# provides proper multithreading capability.  The programmer can, if they wish, manage thread creation directly with
	```
	System.Threading.Thread newThread = new System.Threading.Thread(AMethod);
	```
	but the recommended way to create a threaded application in C# is to use the BackgroundWorker component.
	* Threads or thread-like abilities
	* How is multitasking accomplished?
