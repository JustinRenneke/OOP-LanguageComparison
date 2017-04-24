## Errors and exception handling
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