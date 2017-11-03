def myCos(x):
    '''
    objective: to compute the value of cos(x)
    input parameters:
        x: enter the number whose cosine value user wants to find out
    approach: write the infinite series of cosine using while loop
    return value: value of cos(x)
    '''
    epsilon=0.00001
    multBy=-x**2
    term=1
    total=1
    nxtInSeq=1

    while abs(term)>epsilon:
        divBy=nxtInSeq*(nxtInSeq+1)
        term=term*multBy/divBy
        total+=term
        nxtInSeq+=2
    return total

def main():
    '''
    objective: to compute the value of cos(x)
    input parameters:
        x: enter the number whose cosine value user wants to find out
    return value: cos(x)
    '''
    x=float(input('Enter a number :'))
    print('cos(x) = ',myCos(x))
    
if __name__=='__main__':
    main()
