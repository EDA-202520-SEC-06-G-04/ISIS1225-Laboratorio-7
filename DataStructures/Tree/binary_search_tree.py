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
       
        root["size"] = 1 + size_tree(root["left"]) + size_tree(["right"])
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
            return get_node(node["right"], key)

    return get_node(my_bst["root"], key)

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(node):
    if node is None:
        return 0
    return node["size"]