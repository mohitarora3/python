def hanoi(n,source,spare,target):
    '''
    objective: to transfer discs from source to target with the heavier disc
               below the lighter one 
    input parameters:
               n: number of discs
               source: tower from which disc need to be transferred
               spare: tower which is used as an intermediate to transfer disc
                      from source to destination
               target: tower to which the discs needs to be transferred
    return value: none
    
    '''

  
    if n==1:
        print('Move a disc from ',source,' to ',target)
    else:
        hanoi(n-1,source,target,spare)
        print('Move a disc from ',source,' to ',target)
        hanoi(n-1,spare,source,target)

hanoi(3,1,2,3)
