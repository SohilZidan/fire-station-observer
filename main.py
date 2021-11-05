from threading import Thread
import json
import concurrent.futures
from lib.CallSubject import WaitingQueue
from lib.ObjectSerialization import *
from lib.EmpObserver import ConcreteObserver
from lib.Call import Call, lowPriority, highPriority
from lib.Employee import *


calls = [
    Call(1, "Sohil", None, lowPriority()),
    Call(14, "Mohammad", None, lowPriority()),
    Call(61, "Salim", None, highPriority()),
    Call(87, "khaled", None, lowPriority()),
    Call(2, "anas", None, lowPriority()),
    Call(78, "amer", None, lowPriority()),
    Call(90, "Yehya", None, highPriority()),
    Call(7, "foad", None, highPriority()),
    Call(56, "samir", None, highPriority())
]


data = [
    Junior(3, 'soso'),
    Junior(85, 'toto'),
    Senior(36, 'tata'),
    Senior(8, 'lala'),
    Manager(5, 'fofo'),
    Director(31, 'yoyo')
]


if __name__ == "__main__":
    # read employees' records
    try:
        employees = readJSON('Employee.json')
    except FileNotFoundError as e:
        print("%s => %s" % (e.strerror, e.filename))
        exit()

    # Joining employees
    MySys = WaitingQueue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(employees)) as executor:
        executor.map(MySys.joinPool, [ConcreteObserver(emp) for emp in employees])

    # start handling calls
    Thread(target=MySys.DispatchCalls).start()

    # start receiving calls
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(employees)) as executor:
        executor.map(MySys.receiveCall, calls)
