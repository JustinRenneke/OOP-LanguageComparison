## Singleton
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