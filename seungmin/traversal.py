class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


class Traversal:
    def __init__(self):
        self.tree = {}
    
    def insert(self, root, node):
        self.tree[root] = node

    def prefix(self, node):
        print(node.root, end='')
        if node.left != None:
            self.prefix(self.tree[node.left])
        if node.right != None:
            self.prefix(self.tree[node.right])

    def infix(self, node):
        if node.left != None:
            self.infix(self.tree[node.left])
        print(node.root, end='')
        if node.right != None:
            self.infix(self.tree[node.right])

    def postfix(self, node):
        if node.left != None:
            self.postfix(self.tree[node.left])
        if node.right != None:
            self.postfix(self.tree[node.right])
        print(node.root, end='')


if __name__ == "__main__":
    
    n = int(input())
    t = Traversal()

    for i in range(n):
        root, left, right = input().split()
        if left == '.':
            left = None
        if right == '.':
            right = None
        temp_node = Node(root, left, right)
        t.insert(root, temp_node)

    t.prefix(t.tree['A'])
    print()
    t.infix(t.tree['A'])
    print()
    t.postfix(t.tree['A'])

        
