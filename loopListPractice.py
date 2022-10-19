def con7(x):
    for i in range(len(x)-1):
        if x[i] == 7:
            if x[i+1] == 7:
                return True
            
    return False

def prime5(y):
    sum1 = 0
    for i in range(len(y)):
        if y[i] == 2 or y[i] == 3 or y[i] == 5 or y[i] == 7 or y[i] == 11:
            break
        else:
            sum1 = sum1 + (y[i])
    return sum1

def start2or3(z):
    '''sum2 = 0
    yes = 0
    for i in range (len(z)):
        if z[i] == 2:
            break
            yes = 1
        else:
            sum2 = sum2 + (z[i])

    for i in range (len(z)-1):
        if yes == 1:
            sum2 = sum2 + (z[i+1])
        if yes != 1:
            sum2 = sum2 + 0 '''

    sum2 = []
    yes = True

    for elem in z:
        if elem == 2 and yes == True:
            yes = False
            continue

        if elem == 3 and yes == False:
            yes = True
            continue

        if yes:
            sum2.append(elem)
            
    return sum(sum2)
    

def main():

    print(con7([1,2,3,7,7]))
    print(con7([1,7,2,7]))
    print(con7([7,8,7]))

    print(prime5([1,4,2,3,6]))
    print(prime5([1,20,12,8,5,8,10]))
    print(prime5([2,3,4,5,6,7,8,9,10]))

    print(start2or3([1,4,4]))
    print(start2or3([1,5,6,2,99,56,3]))
    print(start2or3([1,3,4,2,3,8]))

if __name__ == "__main__":
    main()
