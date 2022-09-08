from binary_node import BinaryNode

print('\n\n===== Binary Tree: Insertion Activity =====')
root = BinaryNode(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)

root.search_for_node(root, 31)
root.search_for_node(root, 11)
