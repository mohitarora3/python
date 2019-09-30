lst=[2,4,5,1,75,10]

def findIdxMin(lst,idxlb=0,idxub=len(lst)-1):
    '''
    objective: to find the index of minimum element using recursion
    input parameters: 
        lst: list of elements
    output: minimum  element of the list
    
    '''
    if idxlb==idxub:
        return idxlb
    else:
        if lst[idxlb]<lst[idxub]:
            return findIdxMin(lst,idxlb,idxub-1)
        else:
            return findIdxMin(lst,idxlb+1,idxub)
  
def sortList(lst,lb=0,idxminm=findIdxMin(lst)):
    '''
    objective: to sort a list of elements using recursion 
    input parameters: 
        lst: list of elements
    output: sorted list
    
    '''
    if lb<len(lst)-1:
        if lst[lb]!=lst[idxminm]:
            temp=lst[idxminm]
            lst.pop(idxminm)
            lst[lb+1:]=lst[lb:]
            lst[lb]=temp
            return sortList(lst,lb+1,findIdxMin(lst,lb+1))
        else:
            return sortList(lst,lb+1,findIdxMin(lst,lb+1))
    else:
        return lst
print(sortList(lst))
