# from queue import PriorityQueue
from threading import Condition, Thread, Lock
from lib.LinkedList import SinglyLinkedList


class WaitingQueue:
    def __init__(self):
        # 
        self._observers = SinglyLinkedList()
        # a queue
        self.calls = []
        # used to nitify the subject of an available observer
        self._condition = Condition()

        # used to notify the calls dispatcher for incoming calls
        self._callSync = Condition()

    def receiveCall(self, call):
        try:
            self._callSync.acquire()
            self.calls.append(call)
            self._callSync.notify_all()
        except:
            print(">> error in receiving thread")
        finally:
            self._callSync.release()

    def DispatchCalls(self):
        """
        assign incoming calls to employees
        """
        threads = []
        try:
            self._callSync.acquire()
            while True:
                if len(self.calls) == 0:
                    self._callSync.wait()
                call = self.calls.pop(0)
                print(">> new call (%d), (%s) is popped\n" % (call.callerID, call.strategy))
                threads.append(Thread(target=self.DispatchCall, args=(call,)))
                threads[-1].start()
        except:
            print("something wrong")
        finally:
            self._callSync.release()

    def DispatchCall(self, call):
        """
        assign a call to an employee
        """
        self._condition.acquire()
        try:

            while True:
                assignedObs = self._observers.findCriterion(call)
                if assignedObs is None:
                    print(">> %d call is waiting\n" % (call.callerID))
                    self._condition.wait()  # Blocks until an item is available for consumption.

                else:
                    print(">> %d (with %s) is assigned to %s (%d)\n" % (
                        call.callerID, call.strategy, assignedObs.employee.__class__.__name__, assignedObs.employee.Id))
                    self.releasePool(assignedObs)

                    thr = Thread(target=assignedObs.doSomething, args=(call,))
                    thr.start()

                    break
        except Exception as e:
            print(f">> error in DispatchCall: {e}")
        finally:
            self._condition.release()


    def joinPool(self, observer):
        self._condition.acquire()
        try:
            observer._subject = self
            self._observers.insert(observer)
            print(">> %s (%d) is available\n" % (observer.employee.__class__.__name__, observer.employee.Id))
            self._condition.notify_all()
        except:
            print(">> error in joinPool")
        finally:
            self._condition.release()


    def releasePool(self, observer):
        self._observers.removeKey(observer)
