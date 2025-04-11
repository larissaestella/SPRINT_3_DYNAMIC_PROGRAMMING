class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def search_prefix(self, prefix):
        results = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                if node.value.lower().startswith(prefix.lower()):
                    results.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return results[:5]  # Limita a 5 sugestões
