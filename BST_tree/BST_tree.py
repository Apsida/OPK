class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, cmp_func):
        self.root = None
        self.cmp_func = cmp_func

    def min_data_node(self, root):
        current = root
        while (current.left is not None):
            current = current.left
        return current

    def _find_parent(self, value):
        if self.root is None:
            return None
        current_node = self.root
        while current_node is not None:
            if self.cmp_func(value, current_node.right.data) == 0 or self.cmp_func(value, current_node.left.data) == 0  :
                return current_node
            elif self.cmp_func(value, current_node.data) == 1:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while current_node is not None:
            if self.cmp_func(value, current_node.data) == 1:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right

    def del_knot(self, value):
        node_to_delete = self.search(value)
        if node_to_delete is None:
            raise Exception("notExist")
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete == self.root:
                self.root = None
                return
            parent = self._find_parent(value)
            if parent.left == node_to_delete:
                parent.left = None
            else:
                parent.right = None
            return

        if node_to_delete.left is None or node_to_delete.right is None:
            if node_to_delete == self.root:
                if node_to_delete.left is not None:
                    self.root = node_to_delete.left
                else:
                    self.root = node_to_delete.right
                return
            parent = self._find_parent(value)
            if node_to_delete.left is not None:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.left
                else:
                    parent.right = node_to_delete.left
                return
            else:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.right
                else:
                    parent.right = node_to_delete.right
                return

        if node_to_delete.left is not None and node_to_delete.right is not None:
            temp = self.min_data_node(node_to_delete.right)
            node_to_delete.right = self.del_knot(node_to_delete.right.data)
            return

    def search(self, value):
        if self.root is None:
            return None
        current_node = self.root
        while current_node is not None:
            if self.cmp_func(value, current_node.data) == 0 :
                return current_node
            elif self.cmp_func(value, current_node.data) == 1:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    
def size(root):
    a = 0
    if root:
        a += 1
        a += size(root.left)
        a += size(root.right)
    return a

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)

def creat (cmp_func):
    tree = Tree(cmp_func)
    return tree

def test_cmp(a,b):
    if a > b:
        return -1
    elif a == b:
        return 0
    else: return 1

if __name__ == "__main__":
    tr = creat(test_cmp)
    tr.insert(10)
    tr.insert(2)
    tr.insert(15)
    tr.insert(12)
    tr.insert(114)
    tr.insert(1)
    print_inorder(tr.root)
    
    