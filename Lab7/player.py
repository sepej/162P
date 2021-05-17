from person import Person

class Player():
    # init player class
    def __init__(self, first_name = "", last_name = "", age = None):
        self.__person = Person(first_name, last_name, age)
        self.__class_name = "unknown" 
        self.__class_action = "unknown"
        self.__level = 1
    
    # return player first name
    def getFirstName(self): 
        return self.__person.getFirstName()
    
    # return player last name
    def getLastName(self):
        return self.__person.getLastName()

    # return player full name
    def getPlayerName(self):
        return self.__person.getFirstName() + " " + self.__person.getLastName()
    
    # return player age
    def getPlayerAge(self):
        return self.__person.getAge()

    # return player level
    def getLevel(self):
        return self.__level
    
    # return class name
    def getClassName(self):
        return self.__class_name

    # return action
    def getAction(self):
        return self.__class_action

    # set level+1
    def levelUp(self):
        self.__level += 1

    # overrides
    def __eq__(self, other):
        return self.getPlayerName() == other.getPlayerName() and self.getPlayerAge() == other.getPlayerAge() and self.getClassName() == other.getClassName()

    def __gt__(self, other):
        return self.__level > other.__level

    def __str__(self):
        return self.getPlayerName() + " aged " + str(self.getPlayerAge()) + " playing a " + self.getClassName() + " " + self.getAction()

class Priest(Player):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def getClassName(self):
        return "Priest"
    def getAction(self):
        return "heals"

class Ranger(Player):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def getClassName(self):
        return "Ranger"
    def getAction(self):
        return "shoots arrows"
    

class Rogue(Player):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def getClassName(self):
        return "Rogue"
    def getAction(self):
        return "picks pockets"

class Wizard(Player):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def getClassName(self):
        return "Wizard"
    def getAction(self):
        return "casts fireballs"