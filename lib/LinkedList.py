from lib.Employee import Director, Junior, Senior, Manager


class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, priority=None, nextt=None):
        self.priority = priority
        self.data = data
        self.nextt = nextt

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.priorities = {Junior: 1, Senior: 2, Manager: 3, Director: 4}
        self.head = None


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.nextt
        return '[' + ', '.join(nodes) + ']'


    def prepend(self, data, priority=None):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, nextt=self.head)


    def append(self, data, priority=None):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.nextt:
            curr = curr.nextt
        curr.nextt = ListNode(data=data)


    def insert(self, data):

        """
        insert element based on a priority
        """
        priority = self.priorities[type(data.employee)]
        if not self.head:
            self.head = ListNode(data=data, priority=priority)
            return
        curr = self.head
        while curr.nextt and curr.nextt.priority <= priority:
            curr = curr.nextt
        curr.nextt = ListNode(data=data, priority=priority, nextt=curr.nextt)


    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.nextt
        return curr  # Will be None if not found


    def findCriterion(self, call):
        "find the employee who can handle the call"
        priorities = self.priorities
        callPrio = call.strategy.algorithm()
        curr = self.head
        while curr and (len(callPrio) is not 0) and not isinstance(curr.data.employee, callPrio[0]):
            if priorities[callPrio[0]] < priorities[type(curr.data.employee)]:
                callPrio = callPrio[1:]
            elif priorities[callPrio[0]] > priorities[type(curr.data.employee)]:
                curr = curr.nextt
        if curr and (len(callPrio) is not 0):
            return curr.data
        else:
            return None


    def removeKey(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.nextt
        # Unlink it from the list
        if prev is None:
            self.head = curr.nextt
        elif curr:
            prev.nextt = curr.nextt
            curr.nextt = None


    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.nextt
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
