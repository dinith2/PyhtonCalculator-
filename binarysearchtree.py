class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        self.root = self._add(self.root, key)

    def _add(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._add(root.left, key)
        elif key > root.key:
            root.right = self._add(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

# Example usage:
bst = BinarySearchTree()
bst.add(50)
bst.add(30)
bst.add(20)
bst.add(40)
bst.add(70)
bst.add(60)
bst.add(80)

print("Original BST:", bst.inorder_traversal(bst.root))

bst.delete(20)
print("BST after deleting 20:", bst.inorder_traversal(bst.root))

bst.delete(30)
print("BST after deleting 30:", bst.inorder_traversal(bst.root))
