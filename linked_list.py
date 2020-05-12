# Notes


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None

    def add(self, value):
        # reagardless of if the list is empty of not, we need to wrap the value
        # in a Node
        new_node = Node(value)
        # what if the lsit is empty?
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # We want to add the node to the last node on the list
            # we can get to the last nod eon th elist by traversing it
            current = self.head
            while current:
                current = current.get_next()
            # we're at the end of the linked list
            current.set_next(new_node)

        def remove_from_head(self):
            # what if the list is empty?
            if not self.head:
                return None
            # what if it isn't empty?
            else:
                # we want to return the value at the current head
                value = self.head.get_value()
                # remove the value at the head
                # update self.head
                self.head = self.head.get_next()
                return value


ll = Node(1)
ll.set_next(Node(2))
ll.next_node.next_node = Node(3)
ll.next_node.next_node.next_node = Node(4)
