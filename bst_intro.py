class TreeNode:
    def __init__(self, key) :
        self.key = key
        self.left = None
        self.right = None


def create_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = create_tree(data[0])
        node. right = create_tree(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def create_tuple(tree):
    if tree is None:
        return
    if tree.left is None:
        if tree.right is None:
            return tree.key
        else:
            return None, tree.key, create_tuple(tree.right)
    else:
        if tree.right is None:
            return create_tuple(tree.left), tree.key, None
        else:
            return create_tuple(tree.left), tree.key, create_tuple(tree.right)


tree_tuple = (1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))
binary_tree = create_tree(tree_tuple)

tree_tuple_derived = create_tuple(binary_tree)

print(tree_tuple_derived)
print(tree_tuple)

#1,3,2,3,4,5,6,7,8
def in_order_traversal(tree):
    if tree is None:
        return []
    return in_order_traversal(tree.left) + [tree.key] + in_order_traversal(tree.right)

print(in_order_traversal(binary_tree))

#2 3 1 5 3 4 7 6 8
def pre_order_traversal(tree):
    if tree is None:
        return []
    return [tree.key] + pre_order_traversal(tree.left) + pre_order_traversal(tree.right)

print(pre_order_traversal(binary_tree))

#1 3 4 3 6 8 7 5 2
def post_order_traversal(tree):
    if tree is None:
        return []
    return post_order_traversal(tree.left) + post_order_traversal(tree.right) + [tree.key]
print(post_order_traversal(binary_tree))

def calculate_tree_depth_one(tree):
    if tree is None:
        return 0
    return 1 + max(calculate_tree_depth_one(tree.left), calculate_tree_depth_one(tree.right))

print(f"depth of the binary tree {calculate_tree_depth_one(binary_tree)}")

def calculate_min_depth(tree):
    if tree is None:
        return 0
    return 1 + min(calculate_min_depth(tree.left), calculate_min_depth(tree.right))

print(f"minimum depth of the binary tree {calculate_min_depth(binary_tree)}")

#9
def count_nodes(tree, node_count):
    if tree is None:
        return node_count
    return count_nodes(tree.left, node_count) + 1 + count_nodes(tree.right, node_count)

print(f"number of nodes in the binary tree {count_nodes(binary_tree, 0)}")

print(f"tree depth (another way) : {calculate_tree_depth_one(binary_tree)}")

def depth(tree):
    if tree is None:
        return 0
    return 1 + max(depth(tree.left), depth(tree.right))

def diameter(tree):
    if tree is None:
        return 0
    ldepth = depth(tree.left)
    rdepth = depth(tree.right)
    return max(1+ldepth+rdepth, max(diameter(tree.left),diameter(tree.right)))

print(f"tree diameter: {diameter(binary_tree)}")

