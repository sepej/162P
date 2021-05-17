# Test Driver for Spring 2021 CS 162P Lab 7A
# Created by Katie Strauss 5/12/2021

# for makePlayer helper function
from random import randrange

# import your class files here
from person import Person
from player import Player, Ranger, Rogue, Wizard, Priest
from linkedList import LinkedList


def main():
    # uncomment functions to run tests

    # Part A tests
    # should still work after Part B has been implemented
    testPerson()
    testPlayerCharacters()
    testOverrides()

    # Part B tests
    # Tests LinkedList of Players
    testLinkedList()


def testPerson():
    print("Testing Person class.", "\n\n")

    defaultPerson = Person()
    print("The default person should have a blank first name, and last name, and the age of 0")
    print("printing firstName: ", defaultPerson.getFirstName())
    print("printing lastName: ", defaultPerson.getLastName())
    print("printing age: ", defaultPerson.getAge(), end="\n\n")

    print("Now modifying the the default person through setters.")
    defaultPerson.setFirstName("Englebert")
    defaultPerson.setLastName("Humperdinck")
    defaultPerson.setAge(85)

    print("Now outputting new values.")
    print(defaultPerson.getFirstName() + " " + defaultPerson.getLastName()
          + " was " + str(defaultPerson.getAge()) + " on May 8, 2021.", end="\n\n")

    print("Testing Overloaded Constructor")

    fName, lName, age = makePersonInfo()
    overloadPerson = Person(fName, lName, age)

    print("Outputting overloaded person")
    print(" expected: " + fName + " " + lName + " " + str(age))
    print(" actually: " + overloadPerson.getFirstName() + " " + overloadPerson.getLastName()
          + " " + str(overloadPerson.getAge()))
    
    print("Done testing Person ", end="\n\n")


def testPlayerCharacters():
    print("Testing Player and Character Classes.", end="\n\n")

    print("Creating a generic Player")
    fName, lName, age = makePersonInfo()
    testPlayer = Player(fName, lName, age)
    print(" expected: " + fName + " " + lName + " is " + str(age) + " years old.")
    print(" actually: " + testPlayer.getPlayerName() + " is " + str(testPlayer.getPlayerAge()) + " years old.")
    print(" expected: " + fName + " " + lName + " plays a level 1 unknown who unknown.")
    print(" actually: " + testPlayer.getPlayerName() + " plays a level " + str(testPlayer.getLevel()) + " "
          + testPlayer.getClassName() + " who " + testPlayer.getAction())
    print()

    print("Creating a character of each class")
    fName, lName, age = makePersonInfo()
    rakishRogue = Rogue(fName, lName, age)
    print(" expected: " + fName + " " + lName + " plays a level 1 Rogue who picks pockets.")
    print(" actually: " + rakishRogue.getPlayerName() + " plays a level " + str(rakishRogue.getLevel()) + " "
          + rakishRogue.getClassName() + " who " + rakishRogue.getAction())
    print()

    fName, lName, age = makePersonInfo()
    piousPriest = Priest(fName, lName, age)
    print(" expected: " + fName + " " + lName + " plays a level 1 Priest who heals.")
    print(" actually: " + piousPriest.getPlayerName() + " plays a level " + str(piousPriest.getLevel()) + " "
          + piousPriest.getClassName() + " who " + piousPriest.getAction())
    print()

    fName, lName, age = makePersonInfo()
    wizenedWizard = Wizard(fName, lName, age)
    print(" expected: " + fName + " " + lName + " plays a level 1 Wizard who shoots fireballs.")
    print(" actually: " + wizenedWizard.getPlayerName() + " plays a level " + str(wizenedWizard.getLevel()) + " "
          + wizenedWizard.getClassName() + " who " + wizenedWizard.getAction())
    print()

    fName, lName, age = makePersonInfo()
    reclusiveRanger = Ranger(fName, lName, age)
    print(" expected: " + fName + " " + lName + " plays a level 1 Ranger who shoots arrows.")
    print(" actually: " + reclusiveRanger.getPlayerName() + " plays a level " + str(reclusiveRanger.getLevel()) + " "
          + reclusiveRanger.getClassName() + " who " + reclusiveRanger.getAction())
    print()

    print("Now leveling up " + reclusiveRanger.getPlayerName())
    reclusiveRanger.levelUp()
    print(" expected: " + fName + " " + lName + " plays a level 2 Ranger who shoots arrows.")
    print(" actually: " + reclusiveRanger.getPlayerName() + " plays a level " + str(reclusiveRanger.getLevel()) + " "
          + reclusiveRanger.getClassName() + " who " + reclusiveRanger.getAction())
    print()

    print("Done testing Player and Character classes ", end="\n\n")


def testOverrides():
    fName1 = "Seli"
    lName1 = "D'Amor"
    age1 = 15

    ranger1 = Ranger(fName1, lName1, age1)
    ranger2 = Ranger(fName1, lName1, age1)

    print("Testing overloaded string.")
    print(ranger1)
    print()

    print("Testing equality on two identical Rangers. Should be equal.")
    if ranger1 == ranger2:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are equal")
    else:
        print("Something went wrong, identical rangers are not equal")
    print()

    print("Leveling up one ranger, should still be equal.")
    ranger1.levelUp()
    if ranger1 == ranger2:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are equal")
    else:
        print("Something went wrong, rangers identical in all ways except level are not equal")
    print()

    print("Checking greater than operator, the higher level ranger should be greater than the lower level ranger")
    if ranger1 > ranger2:
        print(ranger1)
        print("is greater than")
        print(ranger2)
    else:
        print("Something went wrong.")
        print(ranger1)
        print("is not greater than")
        print(ranger2)
    print()

    fName2 = "Silver"
    lName2 = "Unya"
    age2 = 33

    print("Creating a ranger with entirely different attributes.  Should not be equal.")
    ranger2 = Ranger(fName2, lName2, age2)
    if ranger1 == ranger2:
        print("Something went wrong, Rangers with different attributes are equal")
    else:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are not equal")
    print()

    print("Creating a ranger with the same last name and age, with a different first name.  Should not be equal.")
    ranger2 = Ranger(fName2, lName1, age1)
    if ranger1 == ranger2:
        print("Something went wrong, Rangers with different first names are equal")
    else:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are not equal")
    print()

    print("Creating a ranger with the same first name and age with a different last name.  Should not be equal.")
    ranger2 = Ranger(fName1, lName2, age1)
    if ranger1 == ranger2:
        print("Something went wrong, Rangers with different last names are equal")
    else:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are not equal")
    print()

    print("Creating a ranger with the same first and last name with a different age.  Should not be equal.")
    ranger2 = Ranger(fName1, lName1, age2)
    if ranger1 == ranger2:
        print("Something went wrong, Rangers with different ages are equal")
    else:
        print(ranger1)
        print("and")
        print(ranger2)
        print("are not equal")
    print()

    print("Creating a wizard with the same first name, last name, and age.  Should not be equal.")
    wizard1 = Wizard(fName1, lName1, age1)
    if ranger1 == wizard1:
        print("Something went wrong, Ranger and Wizard are equal")
    else:
        print(ranger1)
        print("and")
        print(wizard1)
        print("are not equal")
    print()

    print("Checking greater than operator, the higher level ranger should be greater than the lower level wizard")
    ranger1.levelUp()
    if ranger1 > wizard1:
        print(ranger1)
        print("is greater than")
        print(wizard1)
    else:
        print("Something went wrong.")
        print(ranger1)
        print("is not greater than")
        print(wizard1)
    print()


# random person creation helper function
def makePersonInfo():
    FIRSTS = 8
    LASTS = 7
    MIN_AGE = 10
    MAX_AGE = 90

    firstNames = ["Bill", "Mary", "John", "Nancy", "Paul", "George", "Frodo", "Linda"]
    lastNames = ["Jones", "Smith", "Green", "White", "Baggins", "Dunhill", "Scarlet"]

    fName = firstNames[randrange(FIRSTS)]
    lName = lastNames[randrange(LASTS)]

    age = randrange(MIN_AGE, MAX_AGE) + MIN_AGE

    return fName, lName, age


def testLinkedList():
    CHAR_TYPES = 4
    NUM_CHARS = 5
    pythonList = []

    print("Populating Python List with Players")
    for entry in range(NUM_CHARS):
        charType = randrange(CHAR_TYPES)
        fName, lName, age = makePersonInfo()

        if charType == 0:
            pythonList.append(Wizard(fName, lName, age))
        elif charType == 1:
            pythonList.append(Rogue(fName, lName, age))
        elif charType == 2:
            pythonList.append(Ranger(fName, lName, age))
        elif charType == 3:
            pythonList.append(Priest(fName, lName, age))
        else:
            raise TypeError

    print("Your players are: \n")
    for player in pythonList:
        print(player)
    print()

    print("Constructing a LinkedList")
    try:
        linkedList = LinkedList()
    except:
        print("LinkedList construction failed.\n")
    else:
        print("LinkedList successfully constructed.\n")

    print("Now adding players to your LinkedList.")
    try:
        for player in pythonList:
            linkedList.addHead(player)
    except:
        print("Error in addHead function\v")
    else:
        print("All players successfully added.\n")

    print("Now getting the value from the head of your LinkedList")
    try:
        print("Expected: " + str(pythonList[-1]))
        print("Actually: " + str(linkedList.getHead()))
    except:
        print("Error in getHead function.\n")
    else:
        print()

    print("Now looking for a player known to be in the list.")
    try:
        found = linkedList.findValue(pythonList[2])
    except:
        print("Error in findValue function.\n")
    else:
        print(pythonList[2])
        if found:
            print("was found in your LinkedList\n")
        else:
            print("was not found in your LinkedList and should have been\n")

    print("Now looking for a value known not to be in the list.")
    wizardJim = Wizard("Jim", "Bailey", "69")
    try:
        found = linkedList.findValue(wizardJim)
    except:
        print("Error in findValue function.\n")
    else:
        print(wizardJim)
        if found:
            print("was found in your LinkedList and should not have been\n")
        else:
            print("was not found in your LinkedList\n")

    linkedList.addHead(wizardJim)
    print("Testing RemoveHead")
    try:
        linkedList.removeHead()
    except IndexError:
        print("LinkedList was empty, it should not have been.")
    else:
        if linkedList.findValue(wizardJim):
            print("Value still in list, removeHead failed")
        else:
            print("removeHead successfully removed head")

    print("Emptying LinkedList and testing removeHead exception")
    try:
        for link in range(NUM_CHARS + NUM_CHARS): # way bigger than linkedList
            linkedList.removeHead()
    except IndexError:
        print("Caught IndexError when removing from empty list\n")
    except:
        print("Caught an unexpected exception, something is wrong.\n")

    print("Trying getHead on empty LinkedList, should raise IndexError")
    try:
        linkedList.getHead()
    except IndexError:
        print("Caught IndexError\n")
    except:
        print("Caught an unexpected exception, something is wrong\n")

    print("LinkedList testing completed\n")


if __name__ == "__main__":
    main()
