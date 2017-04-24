 ## Implementation of listeners and event handlers
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