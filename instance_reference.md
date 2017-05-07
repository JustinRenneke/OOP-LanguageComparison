## Instance reference name in data type (class)
### Python
* self keyword. 

"The first argument of every class method, including __init__, is always a reference to the current instance of the class. By convention, this argument is always named self. In the __init__ method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called." (https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/)
"However self is not a reserved keyword in python it’s just a strong convention."

```
class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
```

Because the first argument of every class method refers to the "current instance", it does not need to be called self, and can be called anything.
```
class Restaurant(object):
    bankrupt = False
    def open_branch(potato):
        if not potato.bankrupt:
            print("branch opened")
```
Works just as well. Because this argument is passed automaticalled when using *instance.method()* notation, the method **must** accept at least one argument:
```
class Restaurant(object):
    def open_branch():
        print("branch opened")
```
Will be an error, because the instance reference is being passed to open_branch()

When not using *instance.method* notation and instead using static method call *Class.method*, like Restaurant().open_branch(), an instance MUST be passed to open_branch even if it doesn't not need one. So all non-static class methods must accept a self argument. 

### C#
* this
"The this keyword refers to the current instance of the class and is also used as a modifier of the first parameter of an extension method." (https://docs.microsoft.com/en-us/dotnet/articles/csharp/language-reference/keywords/this)

Unlike Python, C# uses an explicit keyword ('this') to refer to the current instance of the class. This keyword is implicit and does not need to specified or defined. 

```
public Employee(string name, string alias)
{
    // Use this to qualify the fields, name and alias:
    this.name = name;
    this.alias = alias;
}
```

