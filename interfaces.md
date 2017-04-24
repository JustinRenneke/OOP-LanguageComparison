## Interfaces / protocols
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