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