class Animal:

    def __init__(self, animal, sex, col, age):
        self.animal = animal
        self.sex = sex
        self.color = col
        self.age = age

    def getAnimal(self):
        return self.animal 

    def getSex(self):
        return self.sex

    def getColor(self):
        return self.color

    def getAge(self):
        return self.age
        

def main():

    animalList = Animal("butterfly", "female", "orange", "14 days")

    print(animalList.getAnimal())
    print(animalList.getSex())
    print(animalList.getColor())
    print(animalList.getAge())


if __name__ == "__main__":
    main()
