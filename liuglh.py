'''class Animal:

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

    def setColor(self, c):
        self.Color = c

    def getAge(self):
        return self.age
        

def main():

    animalList1 = Animal("butterfly", "female", "orange", "14 days")
    animalList2 = Animal("butterfly","male","blue", "28 days")
    print("my favorite animal are butterflies")
    print("---------------------------------------")
    
    print(animalList1.getAnimal())
    print(animalList1.getSex())
    print(animalList1.getColor())
    animalList1.setColor("green")
    print(animalList1.getColor())
    print(animalList1.getAge())
    

    print("")
    
    print(animalList2.getAnimal())
    print(animalList2.getSex())
    print(animalList2.getColor())
    print(animalList2.getAge())



if __name__ == "__main__":
    main()'''

class Animal:

    def __init__(self, sex, col, age):
        self.sex = sex
        self.color = col
        self.age = age

    def getSex(self):
        return self.sex

    def getColor(self):
        return self.color

    def getAge(self):
        return self.age

    def setSex(self, s):
        self.sex = s

    def setColor(self, c):
        self.color = c
        

def main():

    animalList1 = Animal("female", "orange", "14 days")
    animalList2 = Animal("male", "blue", "28 days")

    print(animalList1.getSex())
    animalList1.setSex ("male")
    print(animalList1.getSex())
    print(animalList1.getColor())
    animalList1.setColor("purple")
    print(animalList1.getColor())
    print(animalList1.getAge())

    print(animalList2.getSex())
    print(animalList2.getColor())
    print(animalList2.getAge())


if __name__ == "__main__":
    main()
