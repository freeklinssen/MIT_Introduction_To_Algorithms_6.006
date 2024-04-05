
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    
    if B[t[1]][t[0]] == 'o':
        return []
        
    num_sliders = 0
    num_obstocals = 0
    for row in B:
        for col in row:
            if col == 'o': 
                num_sliders+=1
            elif col == '#':
                num_obstocals+=1

    max_moves = 0
    for i in range(num_sliders):
        if i == 0:
            max_moves =  (len(B)**2 - num_obstocals - i)
        else: 
            max_moves *= (len(B)**2 - num_obstocals - i)

    max_moves *= (1/factorial(num_sliders)) 

    counter = 1
    queue = [(B,[])]
    seen = {B}
    
    while counter < max_moves and len(queue) != 0:
        curr_board = queue.pop(0)
        
        for play in ('up', 'down', 'left', 'right'):   
            if len(curr_board[1])==0 or curr_board[1][-1] != play:
                up_result = move(curr_board[0], play) 
                counter += 1
                if up_result not in seen:
                    seen.add(up_result)
                    steps = curr_board[1] + [play]
                    if up_result[t[1]][t[0]] == 'o':           
                        return steps    
                    else:
                        queue.append((up_result, steps))
                      
    return None



####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + ('-'*n) + '+']
    for row in B:
        rows.append('|' + ''.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S
