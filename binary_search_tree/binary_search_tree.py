"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value 
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here 
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value 
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child 
            # we can park the new node here 
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE: check if current node's value is the target 
        if self.value == target:
            return True 
        else:
            # if target is less than the current value 
            if target < self.value:
                # if there is a left child
                if self.left:
                    # call contains function on left child with target
                    return self.left.contains(target)
                # BASE CASE: if not, return false (target is not in the tree)
                else:
                    return False 
            #if target is greater than or equal to current value 
            else:
                # if there is a right child 
                if self.right:
                    # call contains function on right child with target 
                    return self.right.contains(target)
                # BASE CASE: if not, return false (target is not in the tree)
                else:
                    return False 

    # Return the maximum value found in the tree
    def get_max(self):
        #recursive
        if self.right:
            return self.right.get_max()
        else:
            return self.value 
        
        #iterative
        # current = self

        # while current.right:
        #     current = current.right 

        # return current.value 


    # Call the function `fn` on the value of each node
    # This method doesn't return anything 
    def for_each(self, fn):
        #access every single node on the entire tree and call the passed function on it 


        #recursive - depth first traversal 
        #call the function on this node 
        fn(self.value)
        # if node has a right child 
        if self.right:
            # call for_each method on right child 
            self.right.for_each(fn)
        # if node has a left child
        if self.left:
            # call for_each method on left child 
            self.left.for_each(fn)

        # #iterative - depth first (vertically)
        # # use a stack to achieve same ordering 
        # stack = []
        # # add the root node to our stack 
        # stack.append(self)
        # #continue popping from our stack so long as there are nodes in it 
        # while len(stack) > 0:
        #     current_node = stack.pop()

        #     #check if this node has children 
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
            
        #     fn(current_node.value)

        # # iterative - breadth first - moves level by level (horizontally) - FIFO - queue
        # from collections import deque
        # q = deque()
        # q.append(self)

        # while len(q) > 0:
        #     current_node = q.popleft()

        #     #check if this node has children
        #     if current_node.left:
        #         q.append(current_node.left)
        #     if current_node.right:
        #         q.append(current_node.right)
            
        #     fn(current_node.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        
        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal - FIFO 
    def bft_print(self):
        from collections import deque
        q = deque()
        qPrint = deque()
    
        q.append(self)
        qPrint.append(self.value)
        
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
                qPrint.append(current_node.left.value)
            if current_node.right:
                q.append(current_node.right)
                qPrint.append(current_node.right.value)

        for i in qPrint:
            print(i)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal - LIFO 
    def dft_print(self):
        stack = []
        # printStack = []

        stack.append(self)
        # printStack.append(self.value)

        while len(stack) > 0:
            current_node = stack.pop() #pops node off the end and returns the popped node 
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
                # printStack.append(current_node.right.value)
            if current_node.left:
                stack.append(current_node.left)
                # printStack.append(current_node.left.value)

        # for i in printStack:
        #     print(i)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_print(self):
        pass

    # Print Post-order recursive DFT
    def post_order_print(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("bft_print")

bst.bft_print()

print("dft_print")

bst.dft_print()

print("elegant methods")
# print("pre order")
# bst.pre_order_print()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_print()  
