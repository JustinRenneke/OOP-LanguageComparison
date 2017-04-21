class Singleton:

    _instance = None
    _lock = threading.RLock()
    def __init__(self):
        self.timestamp = str(time.time())
        # Cannot hide ctor, so raise an error from 2nd instantiation
        if (Singleton._instance != None):
            raise(‘This is a Singleton! use Singleton.GetInstance method’)
        # Simulate ctor delay
        time.sleep(2)
        Singleton._instance = self
        PrintFlushed(‘Singleton was created by thread ID ‘ +  str(threading.current_thread().ident))
    @staticmethod
    def GetInstance():
        if (Singleton._instance == None):
            Singleton._lock.acquire()
            if (Singleton._instance == None):
                Singleton._instance = Singleton()
            Singleton._lock.release()
        return Singleton._instance
    @staticmethod
    def Reset():
        Singleton._instance = None
