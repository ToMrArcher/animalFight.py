from random import randrange
from random import shuffle
from animal import Animal
from fight import Fight

class Animals:
    listOfAnimalNames = [
        "Hest", 
        "Ku",
        "Flodhest",
        "Esel",
        "Hund",
        "Katt",
        "Skilpadde",
        "Elg",
        "Hybelkanin",
        "Martin"
    ]

    listOfAnimals = []
    def createAnimals(self):
            for i in range(0, self.numberOfAnimals):
                name = self.listOfAnimalNames[randrange(len(self.listOfAnimalNames))]
                hp = randrange(70, 130)
                ap = randrange(10, 40)
                self.listOfAnimals.append(Animal(name, hp, ap))

    def __init__(self, numberOfAnimals):
        self.numberOfAnimals = numberOfAnimals
        self.createAnimals()


    def printAnimals(self):
        print()
        print(f'{"Species":15} | {"AP":2} | {"HP":3}')
        print("---------------------------")
        for animal in self.listOfAnimals:
            print(f'{animal.getName():15} | {str(animal.getAp()):2} | {str(animal.getHp()):3}')
        
    def fight(self):
        while len(self.listOfAnimals) > 1:
            shuffle(self.listOfAnimals)
            self.printAnimals()
            pairs = []

            for i in range(1, len(self.listOfAnimals), 2):
                pair = []
                pair.append(self.listOfAnimals[i-1])
                pair.append(self.listOfAnimals[i])
                pairs.append(pair)
            
            if len(self.listOfAnimals) % 2 == 0:
                self.listOfAnimals.clear()
            else:
                for i in range(len(self.listOfAnimals) - 2, 0, -1):
                    self.listOfAnimals.pop(i)
            
            for pair in pairs:
                print("\n\n")
                print(f'Fight between {pair[0].getName()} and {pair[1].getName()}')
                print("--------------------------")
                print(f'{"Species":15} | {"AP":2} | {"HP":3}')
                print(f'{pair[0].getName():15} | {str(pair[0].getAp()):2} | {str(pair[0].getHp()):3}')
                print(f'{pair[1].getName():15} | {str(pair[1].getAp()):2} | {str(pair[1].getHp()):3}')
                while True:
                    input("any input")
                    Fight(pair[0], pair[1])
                    print("\n\n")
                    print(f'{"Species":15} | {"AP":2} | {"HP":3}')
                    print(f'{pair[0].getName():15} | {str(pair[0].getAp()):2} | {str(pair[0].getHp()):3}')
                    print(f'{pair[1].getName():15} | {str(pair[1].getAp()):2} | {str(pair[1].getHp()):3}')
                    if pair[0].getHp() < 0 and pair[1].getHp() < 0:
                        del(pair[1])
                        del(pair[0])
                        print("Both DIED")
                        break
                    elif pair[0].getHp() < 0:
                        print(f'{pair[0].getName()} died!')
                        del(pair[0])
                        self.listOfAnimals.append(pair[0])
                        break
                    elif pair[1].getHp() < 0:
                        print(f'{pair[1].getName()} died!')
                        del(pair[1])
                        self.listOfAnimals.append(pair[0])
                        break
        

        



