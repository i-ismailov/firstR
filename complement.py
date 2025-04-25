def complement(lst):
    """
    _summary_

    Args:
        lst (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_val=0
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val=lst[i]
    
    print("max num is: ",max_val)#########
    
    
    flag=[1]*(max_val+1)
    result=[]
    
    for n in lst:
        flag[n]=0
    
    for i in range(len(flag)):
        if flag[i] == 1:
            result.append(i)
            
    print(result)#######
    
    return result

complement([1,2,11,3,5,6])#########