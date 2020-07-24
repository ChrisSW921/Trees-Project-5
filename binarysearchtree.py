"""Binary search tree"""
from recursioncounter import RecursionCounter

class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        if not self.left_child and not self.right_child:
            return True
        else:
            return False

    def update_height(self):
        self.height = 0

    def __str__(self):
        if self.is_leaf():
            print(f"{self.data}--LEAF")
        else:
            print(self.data)



class BinarySearchTree:

    def __init__(self):
        self.size = 0
        self.root = None


    #Remove helper variables

    parent = None
    parent_ref = None
    search_parent = None
    count = 0
    pre_order = []

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def len_helper(self, counter=0):
        if counter < 40:
            self.len_helper(counter + 1)
        else:
            return self.size

    def __len__(self):
        print("")


    def height(self):
        return 0

    def __str__(self):
        def print_helper(cursor, offset):
            return 0


    def add(self, item):
        def add_helper(node):
            RecursionCounter()
            if item < node.data:
                if node.left_child is None:
                    node.left_child = Node(item)
                else:
                    add_helper(node.left_child)
            elif node.right_child is None:
                node.right_child = Node(item)
            else:
                add_helper(node.right_child)

        if self.is_empty():
            self.root = Node(item)
        else:
            add_helper(self.root)
        self.size += 1


    def remove(self, item):
        self.parent = None
        self.search_parent = None
        self.count = 0

        def remove_helper_2(item):
            if item.left_child and not item.right_child:
                self.parent.left_child = item.left_child
            elif item.right_child and not item.left_child:
                self.parent.right_child = item.right_child
            elif not item.right_child and not item.left_child:
                self.parent.right_child = None
                self.parent.left_child = None
            else:
                left = item.left_child
                while left.right_child:
                    self.search_parent = left
                    left = left.right_child
                    self.count += 1
                else:
                    item.data = left.data
                    if self.count == 0:
                        item.left_child = item.left_child.left_child
                    else:
                        self.search_parent.right_child = self.search_parent.right_child.left_child

        def remove_helper(item, new_root=None):
            RecursionCounter()
            if new_root:
                temp_root = new_root
            else:
                temp_root = self.root
            if temp_root.data == item:
                remove_helper_2(temp_root)
            elif item < temp_root.data:
                self.parent = temp_root
                remove_helper(item, temp_root.left_child)
            elif item > temp_root.data:
                self.parent = temp_root
                remove_helper(item, temp_root.right_child)
        self.size -= 1
        remove_helper(item)

    def find(self, item):

        def find_helper(node):
            RecursionCounter()
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return find_helper(node.left_child)
            else:
                return find_helper(node.right_child)

        return find_helper(self.root)

    def preorder_helper(self, node=None, iter=0):
        RecursionCounter()
        if iter == 0:
            node = self.root
            if node is None:
                return
            self.pre_order.append(node.data)
            self.preorder_helper(node.left_child, 1)
            self.preorder_helper(node.right_child, 1)

        else:
            if node is None:
                return
            self.pre_order.append(node.data)
            self.preorder_helper(node.left_child, 1)
            self.preorder_helper(node.right_child, 1)
        return self.pre_order

    def preorder(self):
        self.preorder_helper()
        temp = self.pre_order.copy()
        self.pre_order.clear()
        return temp


tree = BinarySearchTree()

tree.add(21)
tree.add(26)
tree.add(30)
tree.add(9)
tree.add(4)
tree.add(14)
tree.add(28)
tree.add(18)
tree.add(15)
tree.add(10)
tree.add(2)
tree.add(3)
tree.add(7)
print(tree.preorder())
print(tree.size)
tree.remove(21)
tree.remove(9)
tree.remove(4)
tree.remove(18)
tree.remove(15)
tree.remove(7)
print(tree.preorder())
print(tree.len_helper())
# print(tree.root.data)
# print(tree.root.left_child.data)
# print(tree.root.left_child.left_child.data)
# print(tree.root.left_child.right_child.data)
#
# print(tree.root.right_child.data)
# print(tree.root.right_child.right_child.data)
# print(tree.root.right_child.right_child.left_child.data)
#print(tree.preorder())
