## Inheritance / extension
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