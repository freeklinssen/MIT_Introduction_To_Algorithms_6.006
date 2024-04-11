import copy
def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    ##################
    # YOUR CODE HERE #
    ##################
    max_length = 0
    for i in range(len(C)):
        done = [None for _ in range(n*k)]
        for j in range(len(P[i])-1):
            if done[j] == None:
                length, s  = LIS(j, P[i], n, k, done)
                if length > max_length:
                        max_length = length
                        S, c = s, C[i]
    S.reverse()
    return (c, S)



def LIS(i, sequence, n, k, done):
        day = (i//k)
        max_day = day+2 if day+2 < n else n
        max_idx = k * (max_day)
        
        max_length, subsequence = 0, [] 
        
        if i == (max_idx-1):
            subsequence.append(sequence[i])
            return 1, subsequence
                
        else:        
            for j in range(i+1, max_idx):
                if sequence[j] < sequence[i]:
                    if done[j] != None:
                        length, tmp_subsequence = done[j]
                    else:         
                        length, tmp_subsequence = LIS(j, sequence, n, k, done)
                    if length > max_length:
                        max_length, subsequence  = length, tmp_subsequence
              
            subsequence.append(sequence[i])
            if done[i] == None: 
                done[i] = (1+max_length, copy.deepcopy(subsequence))
            return 1+max_length, subsequence
    