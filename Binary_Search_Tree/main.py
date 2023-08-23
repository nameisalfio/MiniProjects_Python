from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left, self.right, self.parent = None, None, None
    
    def node_print(self, verbose=False):
        if verbose:
            parent_key = self.parent.key if self.parent else None
            left_key = self.left.key if self.left else None
            right_key = self.right.key if self.right else None
            print(f"key: {self.key}, parent: {parent_key}, left: {left_key}, right: {right_key}")
        else:
            print(self.key)

class BST:
    def __init__(self):
        self.root = None

    # insert
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):
        if node.left is None and key <= node.key:
            node.left = Node(key)
            node.left.parent = node
            return

        if node.right is None and key > node.key:
            node.right = Node(key)
            node.right.parent = node
            return

        if key <= node.key:
            self.insert_recursive(node.left, key)
        else:
            self.insert_recursive(node.right, key)
    
    # search
    def search(self, key):
        if self.root is None:
            return False
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node is None:
            return False, None 
        
        if key == node.key:
            return True, node
        
        if key <= node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

    # remove
    def remove(self, key):
        if self.root is None:
            return

        self.root = self.remove_recursive(self.root, key)

    def remove_recursive(self, node, key):
        if node is None:
            return node

        if key <= node.key:
            node.left = self.remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self.remove_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            successor_node = self.min(node.right)
            node.key = successor_node.key

            # Delete the inorder successor
            node.right = self.remove_recursive(node.right, successor_node.key)

        return node

    # pre order
    def pre_order(self, verbose=False):
        print("pre-order visit: ")
        self.pre_order_recursive(self.root, verbose)
    
    def pre_order_recursive(self, node, verbose):
        if node is None:
            return
        
        node.node_print(verbose)
        self.pre_order_recursive(node.left, verbose)
        self.pre_order_recursive(node.right, verbose)

    # in order
    def in_order(self, verbose=False):
        print("in-order visit: ")
        self.in_order_recursive(self.root, verbose)

    def in_order_recursive(self, node, verbose):
        if node is None:
            return
        
        self.in_order_recursive(node.left, verbose)
        node.node_print(verbose)
        self.in_order_recursive(node.right, verbose)

    # post order
    def post_order(self, verbose=False):
        print("post-order visit: ")
        self.post_order_recursive(self.root, verbose)
        
    def post_order_recursive(self, node, verbose):
        if node is None:
            return
        
        self.post_order_recursive(node.left, verbose)
        self.post_order_recursive(node.right, verbose)
        node.node_print(verbose)

    # level order
    def level_order(self):
        if self.root is None:
            return
        
        queue = deque()
        queue.append(self.root)
        level = 0
        
        while queue:
            level_size = len(queue)
            print(f"lv.{level}: \t", end="") # non torna a capo
            
            for _ in range(level_size):
                node = queue.popleft()
                
                print(node.key, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print()
            level += 1

    # min
    def bst_min(self):
        if(self.root is None):
            return None
        return self.min(self.root)
        
    def min(self, node):
        while node.left:
            node = node.left
        return node

    # max
    def bst_max(self):
        if(self.root is None):
            return None
        return self.max(self.root)
        
    def max(self, node):
        while node.right:
            node = node.right
        return node

    # predecessor
    def predecessor(self, key):
        node = self.search(key)
        if node is None or node == self.min().key:
            return None
        
        if node.left:
            return max(node.left)
        
        parent = node.parent
        while(node and node == parent.left):
            node = parent
            parent = parent.parent
        return parent
        
    # successor
    def successor(self, key):
        node = self.search(key)
        if node is None or node == self.min().key:
            return None
        
        if node.left:
            return min(node.right)
        
        parent = node.parent
        while(node and node == parent.right):
            node = parent
            parent = parent.parent
        return parent

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

tree.level_order()

