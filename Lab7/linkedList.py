class Link():
    def __init__(self, player):
        self.__value = player
        self.__next = None

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next
    
    def getValue(self):
        return self.__value

class LinkedList():
    def __init__(self):
        self.__head = None

    # adds a new link containing value, returns nothing
    def addHead(self, value):
        # create new link containing the value
        temp = Link(value)
        # update its next field to contain whatever head contained
        temp.setNext(self.__head)
        # update head to point to the new link
        self.__head = temp

    # removes the first link in the list, raising index_error if the list is empty
    def removeHead(self):
        # if list is empty, throw an exception
        if self.__head is None:
            raise IndexError("List is empty")
        # change head to point at the next link in the list
        self.__head = self.__head.getNext()
    
    # return the value contained in the first link of the list
    def getHead(self):
        if self.__head is None:
            raise IndexError("List is empty")
        return self.__head
    
    # returns True if there is a link containing a Player equal to value, else False
    def findValue(self, value):
        # start at the head
        current = self.__head
        # continue until the end
        while current is not None:
            # found it
            if current.getValue() == value:
                return True
            # not found
            current = current.getNext()
        # end of list
        return False
    
    # return true if the list is empty
    def isEmpty(self):
        return self.__head == None

    # return a printable representation of the list
    def __repr__(self):
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(current.getValue())
            current = current.getNext()
        nodes.append("None")
        return " -> ".join(nodes)