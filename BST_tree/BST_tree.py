class Tree:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def size(root):
    a = 0
    if root:
        a += 1
        a += size(root.left)
        a += size(root.right)
    return a

def insert(root, key):
    if root is None:
        return Tree(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def del_knot(root, key):
    if root is None:
        raise NameError("DeleteNoneErr")
    if root.val > key:
        root.left = del_knot(root.left, key)
    elif root.val < key:
        root.right = del_knot(root.right, key)
    else:
        if root.right == None and root.left == None:
            root.val = None
            return root
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            root.val = max(root.left.val, root.right.val)
            root.right = del_knot(root.right, root.val)
    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)

if __name__ == "__main__":
    r = Tree(51)
    r = insert(r,32)
    r = insert(r, 61)
    r = insert(r, 78)
    r = insert(r, 21)
    r = insert(r, 1)
    r = insert(r, 1000)

    print(size(r))