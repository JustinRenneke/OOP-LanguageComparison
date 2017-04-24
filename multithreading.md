## Multithreading
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