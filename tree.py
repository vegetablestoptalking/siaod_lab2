from ring import RingList as lst
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return '(%s, %s, %s)' % (self.left or '', self.key, self.right or '')


def insert(tree, key):
    if not tree:
        tree = Node(key)
    elif key < tree.key:
        tree = Node(tree.key, insert(tree.left, key), tree.right)
    elif key > tree.key:
        tree = Node(tree.key, tree.left, insert(tree.right, key))
    return tree


def delete(tree, key):
    a = lst()
    if tree is None:
        return None
    elif key < tree.key:
        return delete(tree.left, key)
    elif key > tree.key:
        return delete(tree.right, key)
    elif key == tree.key:
        tree = None
        return tree

def delete_not_unique(tree):
    keys = lst()
    while tree:
        if not keys.find(tree.key):
            keys.append(tree.key)
            '''not writed'''
    else:
        pass





