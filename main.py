from binarysearchtree import Node, BinarySearchTree


def main():
    """Main function"""
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

    pre = tree.preorder()

    for item in pre:
        print(item, end=', ')

    print('')
    print(tree)

    tree.remove(21)
    tree.remove(9)
    tree.remove(4)
    tree.remove(18)
    tree.remove(15)
    tree.remove(7)

    print(tree)


if __name__ == '__main__':
    main()
