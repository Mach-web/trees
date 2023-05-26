class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    def insert(self, new_val):
        self.insert_implementation(self.root, new_val)
    '''create another method to implement inserting which will help us access the left and right nodes'''
    def insert_implementation(self, start, new_val):
        if start.value > new_val:
            ''' if number being inserted is greater than root let the function shift such that the new root is node to the left'''
            if start.left:
                return self.insert_implementation(start.left, new_val)
            else:
                ''' If there is no left node, let the new left node to be the inserted value'''
                # create a new object to hold the value
                obj_val = Node(new_val)
                start.left = obj_val
                print(obj_val.value)
        elif start.value < new_val:
            if start.right:
                return self.insert_implementation(start.right, new_val)
            else:
                obj_val = Node(new_val)
                start.right = obj_val
                print(obj_val.value)
        pass

    def search(self, find_val):
        return self.search_implementation(self.root, find_val)

    '''create another method to implement searching which will help us access the left and right nodes'''
    def search_implementation(self, start, find_val):
        if start.value == find_val:
            return True
        elif (find_val < start.value) and start.left:
            '''move to the left node if find_val is less than node'''
            return self.search_implementation(start.left, find_val)
        elif (find_val > start.value) and start.right:
            '''move to the right node if find_val is less than node'''
            return self.search_implementation(start.right, find_val)
        else:
            """This is returned if there is neither a left or right node"""
            return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(34)
tree.insert(65)
tree.insert(1)
tree.insert(5)
tree.insert(10)

# Check search
# Should be True
print(tree.search(3))
# Should be False
print(tree.search(13))