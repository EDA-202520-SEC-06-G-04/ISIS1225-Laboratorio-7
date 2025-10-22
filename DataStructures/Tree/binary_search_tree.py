from DataStructures.List import array_list as al

def new_map():
    bst = {"root": None}
    return bst

def new_node(key, value):
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None
    }
    return node

def put(my_bst, key, value):

    def insert_node(root, key, value):
        if root is None:
            return new_node(key, value)
        if key < root["key"]:
            root["left"] = insert_node(root["left"], key, value)
        elif key > root["key"]:
            root["right"] = insert_node(root["right"], key, value)
        else:
            root["value"] = value
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
        return root

    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get(my_bst, key):

    def get_node(node, key):
        if node is None:
            return None
        if key == node["key"]:
            return node["value"]
        elif key < node["key"]:
            return get_node(node["left"], key)
        else:
            return get_node(node["right"])

    return get_node(my_bst["root"], key)

def contains(my_bst, key):
    return get(my_bst, key) is not None

def is_empty(my_bst):
    return size(my_bst) == 0

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(node):
    if node is None:
        return 0
    return node["size"]

def get_min(my_bst):
    if is_empty(my_bst):
        return None
    else:
        return get_min_node(my_bst["root"])["key"]

def get_min_node(node):
    if node["left"] is None:
        return node
    return get_min_node(node["left"])

def get_max(my_bst):
    if is_empty(my_bst):
        return None
    return get_max_node(my_bst["root"])["key"]

def get_max_node(node):
    if node["right"] is None:
        return node
    return get_max_node(node["right"])

def delete_min(my_bst):
    if not is_empty(my_bst):
        my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(node):
    if node["left"] is None:
        return node["right"]
    node["left"] = delete_min_tree(node["left"])
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return node

def delete_max(my_bst):
    if not is_empty(my_bst):
        my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(node):
    if node["right"] is None:
        return node["left"]
    node["right"] = delete_max_tree(node["right"])
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return node

def height(my_bst):
    return height_tree(my_bst["root"])

def height_tree(node):
    if node is None:
        return -1
    return 1 + max(height_tree(node["left"]), height_tree(node["right"]))

def default_compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def keys(my_bst):
    return keys_range(my_bst, get_min(my_bst), get_max(my_bst))

def keys_range(my_bst, lo, hi):
    queue = al.new_list()
    keys_range_tree(my_bst["root"], queue, lo, hi)
    return queue

def keys_range_tree(node, queue, lo, hi):
    if node is None:
        return
    cmplo = default_compare(lo, node["key"])
    cmphi = default_compare(hi, node["key"])
    if cmplo < 0:
        keys_range_tree(node["left"], queue, lo, hi)
    if cmplo <= 0 and cmphi >= 0:
        al.add_last(queue, node["key"])
    if cmphi > 0:
        keys_range_tree(node["right"], queue, lo, hi)

def values(my_bst):
    return values_range(my_bst, get_min(my_bst), get_max(my_bst))

def values_range(my_bst, lo, hi):
    queue = al.new_list()
    values_range_tree(my_bst["root"], queue, lo, hi)
    return queue

def values_range_tree(node, queue, lo, hi):
    if node is None:
        return
    cmplo = default_compare(lo, node["key"])
    cmphi = default_compare(hi, node["key"])
    if cmplo < 0:
        values_range_tree(node["left"], queue, lo, hi)
    if cmplo <= 0 and cmphi >= 0:
        al.add_last(queue, node["value"])
    if cmphi > 0:
        values_range_tree(node["right"], queue, lo, hi)

def key_set(my_bst):
    return key_set_tree(my_bst["root"])

def key_set_tree(node):
    if node is None:
        return set()
    keys = key_set_tree(node["left"])
    keys.add(node["key"])
    keys.update(key_set_tree(node["right"]))
    return keys

def value_set(my_bst):
    return value_set_tree(my_bst["root"])

def value_set_tree(node):
    if node is None:
        return set()
    values = value_set_tree(node["left"])
    values.add(node["value"])
    values.update(value_set_tree(node["right"]))
    return values
