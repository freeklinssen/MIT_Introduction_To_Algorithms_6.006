class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        # sort of next node
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.head == None:
            self.head = self.tail = node
        else: 
            self.head.prev = node
            node.next = self.head
            node.prev = None 
            self.head = node
        

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node


    def delete_first(self):        
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.head
        if x.next != None:
            self.head = x.next
            self.head.prev = None
        else: 
            self.head = None 
            self.tail = None    
               
        x.next = None
        return x.item


    def delete_last(self):
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.tail
        if x.prev != None:
            self.tail = x.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        
        x.prev = None
        return x.item


    def remove(self, x1, x2):
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2 = Doubly_Linked_List_Seq()
        
        
        if x1.prev != None:
            if x2.next != None:
                x1.prev.next = x2.next
                x2.next.prev = x1.prev
            else:
                x1.prev.next = None
                self.tail = x1.prev    
        else: 
            if x2.next != None:
                x2.next.prev = None
                self.head = x2.next
            else:
                self.head = None
                self.tail = None 
        
        L2.head = x1
        L2.head.prev = None
        L2.tail = x2
        L2.tail.next = None

        return L2


    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        
        if self.tail == x:
            x.next = L2.head
            L2.head.prev = x
            self.tail = L2.tail  
        else:  
            L2.tail.next = x.next
            x.next.prev = L2.tail
            x.next = L2.head
            L2.head.prev = x
            
        L2.head = None
        L2.tail = None
        
        
        
