

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    R = list(R)
    
    if len(R)==1:
        return ((1, R[0][0], R[0][1]),)
    
    else:
        cut = len(R)//2
        
        R_1 = satisfying_booking(tuple(R[:cut]))
        R_2 = satisfying_booking(tuple(R[cut:]))
        
        
        B = []
        idx_1 = 0
        idx_2 = 0
        pointer = 0
        while(idx_1 < len(R_1) or idx_2 < len(R_2)):
            
            if idx_1 >= len(R_1):
                if pointer > R_2[idx_2][1]:
                    B.append((R_2[idx_2][0], pointer, R_2[idx_2][2]))
                    pointer = R_2[idx_2][2]
                    idx_2+=1     
                else:
                    B.append(R_2[idx_2])
                    pointer = R_2[idx_2][2]
                    idx_2+=1
                
            elif idx_2 >= len(R_2):
                if pointer > R_1[idx_1][1]:
                    B.append((R_1[idx_1][0], pointer, R_1[idx_1][2]))
                    pointer = R_1[idx_1][2]
                    idx_1+=1     
                else:
                    B.append(R_1[idx_1])
                    pointer = R_1[idx_1][2]
                    idx_1+=1
                
            elif pointer < R_1[idx_1][1] and pointer < R_2[idx_2][1]:
                pointer = min(R_1[idx_1][1],  R_2[idx_2][1]) 
                
            elif pointer >= R_1[idx_1][1]:
                if R_1[idx_1][2] <= R_2[idx_2][1]:    
                    B.append((R_1[idx_1][0], pointer, R_1[idx_1][2]))
                    pointer = R_1[idx_1][2]
                    idx_1+=1 
                elif R_2[idx_2][1] > pointer:
                    B.append((R_1[idx_1][0], pointer, R_2[idx_2][1]))
                    pointer = R_2[idx_2][1] 
                else:
                    B.append((R_1[idx_1][0]+R_2[idx_2][0], pointer, min(R_1[idx_1][2], R_2[idx_2][2]))) 
                    if len(B)>1 and B[-2][0] == B[-1][0] and B[-2][2] == B[-1][1]:
                        last = B.pop(-1)
                        first = B.pop(-1)
                        B.append((first[0], first[1], last[2]))

                    pointer = min(R_1[idx_1][2], R_2[idx_2][2])
                    if R_1[idx_1][2] == R_2[idx_2][2]:
                        idx_1+=1
                        idx_2+=1
                    elif min(R_1[idx_1][2], R_2[idx_2][2]) == R_1[idx_1][2]:
                        idx_1+=1
                    else:
                        idx_2+=1  
                            
                      
            elif pointer >= R_2[idx_2][1]:
                if R_2[idx_2][2] <= R_1[idx_1][1]:
                    B.append((R_2[idx_2][0], pointer, R_2[idx_2][2]))
                    pointer = R_2[idx_2][2]
                    idx_2+=1 
                elif R_1[idx_1][1] > pointer:
                    B.append((R_2[idx_2][0], pointer, R_1[idx_1][1]))
                    pointer = R_1[idx_1][1] 
                else:
                    B.append((R_2[idx_2][0]+R_1[idx_1][0], pointer, min(R_2[idx_2][2], R_1[idx_1][2]))) 
                    pointer = min(R_1[idx_1][2], R_2[idx_2][2])
                    if len(B)>1 and B[-2][0] == B[-1][0] and B[-2][2] == B[-1][1]:
                        last = B.pop(-1)
                        first = B.pop(-1)
                        B.append((first[0], first[1], last[2]))
                    if R_1[idx_1][2] == R_2[idx_2][2]:
                        idx_1+=1
                        idx_2+=1
                    elif min(R_1[idx_1][2], R_2[idx_2][2]) == R_1[idx_1][2]:
                        idx_1+=1
                    else:
                        idx_2+=1  
        
        #print(B)
                        
        return tuple(B)     
        

'''     
# Problem 2-5 (A)

A = ((1,0,2),(3,2,3),(2,3,4),(3,4,6),(4,6,8),(3,8,9),(2,9,10),(1,10,12),(1,13,14))

B = ((1,0,2),(3,2,3),(2,3,4),(3,4,6),(4,6,8),(3,8,9),(2,9,10),(1,10,12),(1,13,14))

A = list(A)
B = list(B) 
combination = []
latest_end_time = 0

while( len(A)!=0 and len(B)!=0):
    
    if(len(A) == 0):
        booking = B.pop(0)
    elif(len(B) == 0):
        booking = A.pop(0)
    elif A[0][1] < B[0][1]:
        booking = A.pop(0)
    else:
        booking = B.pop(0)
        
    
    #yadaydayda....
    #the same as a bove sort of
    
    combination.append(...)
    latest_end_time = ....


return combination

'''