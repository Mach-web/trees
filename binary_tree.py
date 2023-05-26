class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""

        return self.preorder_print(self.root,[])

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""

        if start.value == find_val:
            # if a value is equal to root, true is executed and code stops
            return True
        # Incase any of the recursions is True a True value is returned of this elif statement
        elif start.left or start.right:
            # The first recursion assigns the root as left node
            if start.left:
                recursion1 = self.preorder_search(start.left, find_val)
            else:
                recursion1 = False
            # The second recursion assigns root as right node
            if start.right:
                recursion2 = self.preorder_search(start.right, find_val)
            else:
                recursion2 = False
            # if either of the recursion is true, a true value is returned
            search_results = (recursion1 or recursion2)
            return search_results
        else:
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # I chose a list because it is easier to work with
        traversal_list = traversal
        if start:
            if start.value not in traversal_list:
                traversal_list.append(start.value)
            self.preorder_print(start.left, traversal_list)
            self.preorder_print(start.right, traversal_list)
        # Convert the list into string
        traversal_str = ""
        for i in traversal_list:
            traversal_str += str(i)
            if i == traversal[-1]:
                break
            traversal_str += "-"
        return traversal_str
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(56)
tree.root.right.left = Node(23)
tree.root.right.right.right = Node(30)
tree.root.right.right.right.right = Node(53)
# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(44))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())