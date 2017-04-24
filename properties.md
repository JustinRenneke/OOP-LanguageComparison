## Properties
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
