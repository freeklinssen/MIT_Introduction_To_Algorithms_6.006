def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
     
    count = 1
    Len = 1
    max_len = 1
    
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            Len += 1
            
            if Len == max_len:
                count += 1    
            elif Len > max_len:
                max_len = Len
                count = 1
                      
        else:
            Len = 1
            
            if Len == max_len:
                count += 1 
                
    return count
