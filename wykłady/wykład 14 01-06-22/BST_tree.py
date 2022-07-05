class BST_node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def insert(root, key):
    previous = None
    while root is not None:
        if root.key > key:
            previous = root
            root = root.left
        else:
            previous = root
            root = root.right
    if key < previous.key:
        previous.left = BST_node(key)
        previous.left.parent = previous
    else:
        previous.right = BST_node(key)
        previous.right.parent = previous


def remove(root, value):
    actual_root = find(root, value)
    if actual_root is None:
        return None
    elif actual_root.right is None:
        if actual_root.left is None:
            if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
                actual_root.parent.left = None
            else:
                actual_root.parent.right = None
        else:
            if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
                actual_root.parent.left = actual_root.left
            elif actual_root.parent.right is not None and actual_root.parent.right.key == actual_root.key:
                actual_root.parent.right = actual_root.right
    elif actual_root.left is None:
        if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
            actual_root.parent.left = actual_root.right
        if actual_root.parent.right is not None and actual_root.parent.right.key == actual_root.key:
            actual_root.parent.right = actual_root.right
    else:
        root_value = successor(root, actual_root.key)
        remove(root, root_value)
        actual_root.key = root_value


def maximum(root):
    while root.right is not None:
        root = root.right
    return root.key


def minimum(root):
    while root.left is not None:
        root = root.left
    return root.key


def successor(root, actual_root_value):
    actual_root = find(root, actual_root_value)
    value = actual_root.key
    if actual_root.right is not None:
        return minimum(actual_root.right)
    while actual_root.parent is not None and actual_root.parent.key < actual_root.key:
        actual_root = actual_root.parent
    if actual_root.parent is not None:
        if actual_root.parent.key < value:
            return None
        return actual_root.parent.key
    if actual_root.key < value:
        return None


def predecessor(root, actual_root_value):
    actual_root = find(root, actual_root_value)
    value = actual_root.key
    if actual_root.left is not None:
        return maximum(actual_root.left)
    while actual_root.parent is not None and actual_root.parent.key > actual_root.key:
        actual_root = actual_root.parent
    if actual_root.parent is not None:
        if actual_root.parent.key > value:
            return None
        return actual_root.parent.key
    if actual_root.key > value:
        return None