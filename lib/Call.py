import abc
import datetime
from lib.Employee import *


class Call(abc.ABC):
    """
    Call class follows Strategy design patterns
    in order to define a flexible structure of
    the ways a call can be handled by employees  
    """
    def __init__(self, callerID, callerName, EmpID=None, strategy=None):
        self.callerID = callerID
        self.callerName = callerName
        self.EmpID = EmpID
        currentDT = datetime.datetime.now()
        self.time = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        self.strategy = strategy

    def assignStrategy(self, strategy):
        self.strategy = strategy


class Strategy(abc.ABC):
    """
    represent the priority of a call
    """
    @abc.abstractmethod
    def algorithm(self):
        pass


class lowPriority(Strategy):
    def algorithm(self):
        return [Junior, Senior, Manager]

    def __repr__(self):
        return self.__class__.__name__


class highPriority(Strategy):
    def algorithm(self):
        return [Manager, Director]

    def __repr__(self):
        return self.__class__.__name__
