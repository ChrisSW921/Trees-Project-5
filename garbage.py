def remove_helper_2(node):
    if node.left_child and node.right_child:
        temp = node.left_child
        while temp.right_child:
            self.tparent = temp
            temp = self.tparent.right_child
            self.count += 1
        else:
            node.data = temp.data
            if self.count > 0:
                self.tparent.right_child = self.tparent.right_child.left_child
            else:
                node.left_child = temp.left_child


    elif node.left_child and not node.right_child:
        self.parent_ref = node.left_child
        self.size -= 1
    elif node.right_child and not node.left_child:
        self.parent_ref = node.right_child
        self.size -= 1


def remove_helper(item, t_root=None):
    if t_root is None:
        if self.temp_root.data != item:
            if item < self.temp_root.data:
                self.parent = self.temp_root
                self.parent_ref = self.parent.left_child
                remove_helper(item, self.temp_root.left_child)
            elif item > self.temp_root.data:
                self.parent = self.temp_root
                self.parent_ref = self.parent.right_child
                remove_helper(item, self.temp_root.right_child)
        else:
            remove_helper_2(self.temp_root)
    else:
        if t_root.data != item:
            if item < t_root.data:
                self.parent = t_root
                self.parent_ref = self.parent.left_child
                remove_helper(item, t_root.left_child)
            elif item > t_root.data:
                self.parent = t_root
                self.parent_ref = self.parent.right_child
                remove_helper(item, t_root.right_child)
        else:
            remove_helper_2(t_root)


remove_helper(item)