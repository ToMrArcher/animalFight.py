from animals import Animals

if __name__ == "__main__":
    numberOfAnimals = input("How many animals do you want?: ")
    animals: Animals = Animals(int(numberOfAnimals))
    animals.fight()