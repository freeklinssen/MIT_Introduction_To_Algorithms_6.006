from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)
    
    

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################
        A.sum = A.item.val
        A.max_prefix = A.item.val
        A.Key = A.item.key
        
        if A.left:
            A.sum += A.left.sum
            
            A.max_prefix = A.left.max_prefix
            A.Key = A.left.Key
            if (A.left.sum + A.item.val) > A.max_prefix: 
                A.max_prefix = A.left.sum + A.item.val
                A.Key = A.item.key
                
        if A.right: 
            A.sum += A.right.sum
            
            if A.left: 
                if (A.left.sum + A.item.val + A.right.max_prefix) > A.max_prefix: 
                    A.max_prefix = A.left.sum + A.item.val + A.right.max_prefix
                    A.Key = A.right.Key
            else:
                if (A.item.val + A.right.max_prefix) > A.max_prefix: 
                    A.max_prefix = A.item.val + A.right.max_prefix 
                    A.Key = A.right.Key
        

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)
        

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        ##################
        # YOUR CODE HERE #
        ##################
        k= self.root.Key
        s= self.root.max_prefix
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    tree = Part_B_Tree()
    
    toppings = sorted(toppings, key=lambda x: x[0])
    
    for topping in toppings:
        x = topping[0] 
        item = Key_Val_Item(topping[1], topping[2])
        #node = Part_B_Node(item)
        tree.insert(item)
        y, t  = tree.max_prefix()
        if t > T:
            X, Y, T = x, y, t
    
    return (X, Y, T)
