import random

class GroceryStore:

    def __init__(self):
        self.stuff ={"candy" : 1.25,
                "sushi" : 10.75,
                "coffee" : 2.50,
                "celery" : 0.50,
                "banana" : 1.75,
                "taco seasoning" : 0.75,
                "slim jim": 3.70,
                "popcorn": 5.25,
                "soymilk": 6.75,
                "butter": 1.35}

        self.sManager = str("Taylor Swift")

        self.sName = str("Foodstore")

    def getManager(self):
        return self.sManager
        
    def getName(self):
        return self.sName

def main():

    G = GroceryStore()
    man = (G.getManager())
    name = (G.getName())
    
    print("\n")   
    print(man + " (Store Manager): 'Hi welcome to " + name + "! Wanna know whats on sale?")
    print("\n")
    print("You: 'yes' or 'no'")
    print("\n")
    selected = input()
    wow = list(G.stuff.keys())
    owo = list(G.stuff.values())
    if selected == "yes":
        print("\n")
        print("...")
        print("\n")
        for v in wow:
            print(v)
        print("\n")
            
    if selected == "no":
        print("\n")
        print("wow...")
        print("\n")
        for v in wow:
            print(v)
        print("\n")

    print("Which of these items can I scan for you?")
    
    grabItems = input()
    

    add = 0

    stop = False

    while True:
        for i in range (len(G.stuff)):
            if grabItems == wow[i]:
                print("\n")
                print(wow[i])
                print("\n")
                print("that item is: $" + (str(owo[i])))
                add = add + (owo[i])
                print("\n")
                print("your total so far is: $" + str(add))
                print("\n")
                print("would you like to add something else to your cart?")
                print("\n")
                ask = input()
                    
                if ask != "no" or ask == "yes ":
                    print("please select another item from the list")
                    for v in wow:
                        print(v)
                        
                    grabItems = input()
                    break
                    
                if ask == "no":
                    print("then your grand total is: $" + (str(add)))
                    stop = True

        if stop:
            break

    print("\n\n\n\n")
    print("your " + (grabItems) + " is damaged. would you like to ask Anna for 25% off?")
    damage = input()
    x = random.randint(0,1)
    y = random.randint(0,1)

    if damage == "yes":
        if x == 1: 
            print(man + ": yeah that " + (grabItems)+ " is not in good shape")
            print("I'll go ahead and take 25% off for that item specifically")
            percent = (owo[i]) - (int(owo[i])/4)
            print("\n")
            print("your "+(grabItems)+ " is now " + str(percent))
            add = (add - (owo[i])) + percent
            print("your new total is " + str(add))
            print("\n")
        if x == 0:
            print("We don't do discounts for that kind of stuff")
            print("your grand total is: $" + (str(add)))
            print("\n")

    if damage == "no":
        print("your grand total is: $" + (str(add)))
        print("\n")

    print("you check all of your pockets and realize your wallet is no where to be found")
    print("do you want to make a run with your items and hope you escape successfully?")
    run = input()
    
    if run == "yes":
        if y == 1:
            print("you escaped " + name + " and successfully stole your items")

        if y == 0:
            print("CAUGHT RED HANDED")
            print(man + " demanded you pay or else.")

    if run == "no":
        print("What a good citizen you are. The person behind you offered to foot your bill.")
        

    return (add)
                

    
    


if __name__ == "__main__":
    main()





