import random 

'''class House():
    l = []

    def __init__(self):
        self.rating = 5

    def getRating(self):
        return self.rating2

    def calculatePath(num):
        path = []

def gen():
    


def main():

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(House())

    print(m)

    num = int(input("how many houses: "))
 

if __name__ == "__main__":
    main()'''
 
class House:
 
    def __init__(self):
 
        self.visit = False
 
        self.rating = random.randint(1,10)
 
    def visitedhouse(self):
        self.visit = True
       
    def getRating(self):
        return self.rating
 
def gen(m):
 
    gen = None
    start = (1, 1)
   
    for x in range(len(m)):
        l= m[x]
        for y in range(len(l)):
            house = l[y]
            if gen is None:
                gen = house
                continue
       
            if house.getRating() > gen.getRating():
                start = (y,x)
                gen = house
    print("best rating possible: ")
    return(start)
 
 
 
def adj(m, x, y):
 
    r = []
   
    if x+1 < 5 and m[x+1] [y].visit == False:
        r.append(m[x+1][y].getRating())

    if y+1 < 5 and m[x] [y+1].visit == False:
        r.append(m[x][y+1].getRating())
        
    if x-1 > -1 and m[x-1] [y].visit == False:
        r.append(m[x-1] [y].getRating())
        
    if y-1 > -1 and m[x] [y-1].visit == False:
        r.append(m[x] [y-1].getRating()) 
 
    maxnum = max(r)
 
    indexI = r.index(maxnum)
 
    if indexI == 0:
        return [x+1, y, ratings[0]]
    if indexI == 1:
        return [x, y+1, ratings[1]]
    if indexI == 2:
        return [x-1, y, ratings[2]]
    if indexI == 3:
        return [x, y-1, ratings[3]]  
 
 
def main():
   
    m = [[], [], [], [], []]
    
    for l in m:
        for i in range(5):
            l.append(House())
    for l in m:
        print("\n")
        for house in l:
            print(house.getRating(), end = "  ")
    print("\n")
    print("\n")
 
 
 
    start = gen(m)
    sum1 = m[start[0]][start[1]].getRating()
    print(sum1)
    print("\n")
    print("starting point:")
    print(start)
    print("\n")
   
    num = int(input("houses to visit: "))
 
    for a in range(num):
        yes = adj(m, start[0], start[1])
        m[yes[0]][yes[1]].visitedhouse()
       
        
        sum1 = sum1 + yes[2]
        print(yes)
 
        x = yes[0]
        y = yes[1]
 
    print(sum1/num)
       
        
        
if __name__ == "__main__":
    main()
