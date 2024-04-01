from collections import defaultdict

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    
    length = len(S[0])
    hashtable = {}
    composition = [0 for _ in range(26)]
    
    for i in range(len(T)):
            
        if i >= (length):
            composition[ord(T[i-(length)])-97] -= 1
        composition[ord(T[i])-97] += 1
        
        tup = tuple(composition)
        if tup in hashtable:
            hashtable[tup] += 1
        else:
            hashtable[tup] = 1  
                    
            
    for string in S:
        composition = [0 for _ in range(26)]
        for i in range(length):
           composition[ord(string[i])-97] += 1
        
        tup = tuple(composition)
        if tup in hashtable:
            count = hashtable[tup]
        else:
            count = 0 
        A.append(count)
        

    return tuple(A)
