"""
LRU-cache implementation
"""


class Node:
    """
    node implementation
    """

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.nxt = None
        self.back = None

    def set_nxt(self, nxt):
        """
        Set nxt node
        """
        self.nxt = nxt

    def set_back(self, back):
        """
        Set back node
        """
        self.back = back


class Order:
    """
    order implementation
    """

    def __init__(self):
        self.first = Node()
        self.end = Node()
        self.first.set_nxt(self.end)
        self.end.set_back(self.first)

    def append_node(self, node):
        """
        Add a node to the end
        """
        node.set_back(self.end.back)
        node.set_nxt(self.end)
        self.end.back.set_nxt(node)
        self.end.set_back(node)

    def move_node(self, node):
        """
        Move node to the end
        """
        self.remove_node(node)
        self.append_node(node)

    @staticmethod
    def remove_node(node):
        """
        Remove node
        """
        node.back.set_nxt(node.nxt)
        node.nxt.set_back(node.back)


class LRUCache:
    """
    LRU-cache implementation
    """

    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.que = Order()

    def get(self, key):
        """
        Get requests
        """
        node = self.cache.get(key)
        if not node:
            return None
        self.que.move_node(node)
        return node.value

    def set(self, key, value):
        """
        Set key: value
        """
        node = self.cache.get(key)
        new_node = Node(key, value)
        if node:
            self.que.remove_node(node)
        else:
            if len(self.cache) == self.limit:
                old_node = self.que.first.nxt
                self.cache.pop(old_node.key)
                self.que.remove_node(old_node)
        self.que.append_node(new_node)
        self.cache[key] = new_node
