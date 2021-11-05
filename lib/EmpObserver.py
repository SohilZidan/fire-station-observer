import abc
import time
import random

random.seed(0)


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects (Employees) that should notify
    changes to a subject (waitingQueue)
    """

    def __init__(self, emp):
        self._subject = None
        self._observer_state = None
        self.employee = emp

    def __repr__(self):
        return repr(self.employee)

    @abc.abstractmethod
    def update(self, arg):
        pass

    @abc.abstractmethod
    def joinPool(self, queue):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        self._observer_state = arg

    def joinPool(self, pool):
        pool.joinPool(self)

    def doSomething(self, call):
        time.sleep(random.randint(1, 10))
        print(">> %d is finished\n" % (call.callerID))
        self.joinPool(self._subject)
