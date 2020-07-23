

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

    # def __str__(self):
    #     return "ok"


class BinarySearchTree:
    root = None
    size = 0
    parent = None
    parent_ref = None
    search_parent = None
    count = 0

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __len__(self):
        def len_helper(cursor, offset):
            return 0
        return 0

    def height(self):
        return 0

    def __str__(self):
        def print_helper(cursor, offset):
            return 0
        return "OK"

    def add(self, item):
        def add_helper(node):
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
        self.parent_ref = None
        self.parent = None
        self.search_parent = None
        self.count = 0

        def remove_helper_2(item):
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
            if new_root:
                temp_root = new_root
            else:
                temp_root = self.root
            if temp_root.data == item:
                remove_helper_2(temp_root)
            elif item < temp_root.data:
                self.parent = temp_root
                self.parent_ref = temp_root.left_child
                remove_helper(item, temp_root.left_child)
            elif item > temp_root.data:
                self.parent = temp_root
                self.parent_ref = temp_root.right_child
                remove_helper(item, temp_root.right_child)
        remove_helper(item)












    def find(self, item):

        def find_helper(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return find_helper(node.left_child)
            else:
                return find_helper(node.right_child)

        return find_helper(self.root)

    def preorder(self):
        def preorder_helper(cursor, output):
            return 0
        return 0


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
print(tree.root.left_child.right_child.right_child.left_child.data)
tree.remove(10)
print(tree.find(10))

