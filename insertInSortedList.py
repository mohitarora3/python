lst=[10,20,30,40]
value=15
def insInSortedList(lst,value):
    '''
    objective: To modify a list 
    input parameters:
         value: value that is to be inserted in the list
    output: List in the sorted order
    '''
    #approach: to use recursion
    if value > lst[-1]:
        lst.append(value)
        return lst
    elif lst[0]>value:
        lst[1:]=lst[0:]
        lst[0]=value
        return lst
    else:
        l=[lst[0]]
        return l+insInSortedList(lst[1:],value)
lst=insInSortedList(lst,value)
print(lst)   
