import random


class User:
    def __init__(self, name, username, email_id):
        self.name = name
        self.username = username
        self.email_id = email_id

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'User({self.name},{self.username},{self.email_id})'


akash = User('akash', 'aakash', 'aakash@gmail.com')
bakash = User('bkash', 'bakash', 'bakash@gmail.com')
ckash = User('ckash', 'cakash', 'cakash@gmail.com')
dkash = User('dkash', 'dakash', 'dakash@gmail.com')
ekash = User('ekash', 'eakash', 'eakash@gmail.com')
fkash = User('fkash', 'fakash', 'fakash@gmail.com')
gkash = User('gkash', 'gakash', 'gakash@gmail.com')
hkash = User('hkash', 'hakash', 'hakash@gmail.com')
ikash = User('ikash', 'iakash', 'iakash@gmail.com')
jkash = User('jkash', 'jakash', 'jakash@gmail.com')

skewed_input = [akash, bakash, ckash, dkash, ekash, fkash, gkash, hkash, ikash, jkash]

shuffled_input = skewed_input[::-1]
random.shuffle(shuffled_input)
random.shuffle(shuffled_input)


class BSTNode:
    def __init__(self, user: User):
        self.key = user.username
        self.data = user
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.data.__str__()


def insert(node, user):
    if node is None:
        node = BSTNode(user)
    elif node.key < user.username:
        node.left = insert(node.left, user)
        node.left.parent = node
    else:
        node.right = insert(node.right, user)
        node.right.parent = node
    return node


def display_tree(data, level, space='\t'):
    if data is None:
        return
    if data.right is None and data.left is None:
        pass
    elif data.right is None:
        print(f"{space*(level+1)} Ω")
    else:
        display_tree(data.right, level+1, space='\t')
    print(f"{space*level} {data.key}")
    if data.right is None and data.left is None:
        pass
    elif data.left is None:
        print(f"{space*(level+1)} Ω")
    else:
        display_tree(data.left, level+1, space='\t')


def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif node.key < key:
        return find(node.left, key)
    elif node.key > key:
        return find(node.right, key)


def update(node, user):
    user_node = find(node, user.username)
    if user_node is not None:
        user_node.data = user


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.data)] + list_all(node.right)

def is_bst(tree):
    if tree is None:
        return True, None, None
    l_balanced, l_min, l_max = is_bst(tree.left)
    r_balanced, r_min, r_max = is_bst(tree.right)
    t_balanced, t_min, t_max = l_balanced and \
        r_balanced and (l_max is None or l_max < tree.key) and \
        (r_min is None or r_min > tree.key), \
        min(list(filter(None, list(l_min, tree.key, r_min)))), \
        max(list(filter(None, list(l_max, tree.key, r_max))))
    return t_balanced, t_min, t_max



def is_balanced(tree):
    if tree is None:
        return True, 0
    l_balanced, l_height = is_balanced(tree.left)
    r_balanced, r_height = is_balanced(tree.right)
    balanced, height = l_balanced and r_balanced and abs(l_height-r_height) <= 1,\
        1 + max(l_height, r_height)
    return balanced, height


def create_balanced_tree(data, lo=0, hi = None, tree=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mi = (hi + lo) // 2
    value = data[mi]
    t_node = BSTNode(value)
    t_node.parent = tree
    t_node.left = create_balanced_tree(data, lo, mi-1, t_node)
    t_node.right = create_balanced_tree(data, mi+1, hi, t_node)
    return t_node


def balance_bst(imb_node):
    return create_balanced_tree(list_all(imb_node))


node = None
for user in skewed_input:
    node = insert(node, user)

display_tree(node, 0)

print(find(node, 'jakash'))

jakash = User('jakash', 'jakash', 'jadhav@gmail.com')
update(node, jakash)
print(find(node, 'jakash'))


print(is_balanced(node))

print(list_all(node))

balanced_tree = create_balanced_tree(skewed_input)
display_tree(balanced_tree, 0)
print(is_balanced(balanced_tree))



