# Test Driver for Spring 2021 CS 162P Lab 7A
# Created by Katie Strauss 5/12/2021

from person import Person
from player import Player, Ranger, Rogue, Wizard, Priest
import random


def main():
    # uncomment functions to run tests
    testPerson()
    testPlayerCharacters()
    testOverrides()


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

    fName = firstNames[random.randrange(FIRSTS)]
    lName = lastNames[random.randrange(LASTS)]

    age = random.randrange(MIN_AGE, MAX_AGE) + MIN_AGE

    return fName, lName, age


if __name__ == "__main__":
    main()
