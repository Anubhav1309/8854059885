from node import Node
from node import Node2

class AVLTree:
    def __init__(self):
        self.root = None

    def insertBin(self, id, capacity):
        self.root = self.insert_bin(self.root, id, capacity)

    def insert_bin(self, curr, id, capacity):
        if curr is None:
            new_node = Node(capacity)
            new_node.tree.insertID(id)
            return new_node
        
        if capacity < curr.capacity:
            curr.left = self.insert_bin(curr.left, id, capacity)
        elif capacity > curr.capacity:
            curr.right = self.insert_bin(curr.right, id, capacity)
        else:
            curr.tree.insertID(id)

        curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))
        balance = self.getBalance(curr)

        if balance > 1:
            if capacity < curr.left.capacity:
                return self.rightRotate(curr)
            else: 
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)

        if balance < -1: 
            if capacity > curr.right.capacity:
                return self.leftRotate(curr)
            else: 
                curr.right = self.rightRotate(curr.right)
                return self.leftRotate(curr)

        return curr

    def delete_cap(self, capacity):
        self.root = self.delete_CAP(self.root, capacity)
    
    def delete_CAP(self, curr, capacity):
        if curr is None:
            return curr

        if capacity < curr.capacity:
            curr.left = self.delete_CAP(curr.left, capacity)
        elif capacity > curr.capacity:
            curr.right = self.delete_CAP(curr.right, capacity)
        else:
            if curr.left is None:
                temp = curr.right
                curr = None
                return temp
            elif curr.right is None:
                temp = curr.left
                curr = None
                return temp

            temp = self.minValueNode(curr.right)
            curr.capacity = temp.capacity
            curr.tree = temp.tree
            curr.right = self.delete_CAP(curr.right, temp.capacity)

        if not curr:
            return curr
        
        curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))
        balance = self.getBalance(curr)

        if balance > 1:
            if self.getBalance(curr.left) >= 0:
                return self.rightRotate(curr)
            else:
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)

        if balance < -1:
            if self.getBalance(curr.right) >= 0:
                return self.leftRotate(curr)
            else:
                curr.right = self.rightRotate(curr.right)
                return self.leftRotate(curr)

        return curr

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height
    
    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self,z):
        if z.right is None:
            return z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def rightRotate(self,z):
        if z.left is None:
            return z
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def find_bin(self, capacity):
        return self.find_BIN(self.root, capacity)
    
    def find_BIN(self, curr, capacity):
        if curr is None:
            return None
        
        if curr.capacity == capacity:
            return curr
        elif curr.capacity < capacity:
            return self.find_BIN(curr.right, capacity)
        else:
            return self.find_BIN(curr.left, capacity)


class bin_id__obj_id:
    def __init__(self):
        self.root = None

    def insert_obj_id(self,id,obj_id):
        self.root = self.insert_obj_ID(self.root,id,obj_id)

    def insert_obj_ID(self,curr,id,obj_id):
        if curr is None:
            new_node = Node2(id)
            curr = new_node
            curr.tree2.insertObjID(obj_id)
            return curr

        if id < curr.id:
            curr.left = self.insert_obj_ID(curr.left,id,obj_id)
        elif id > curr.id:
            curr.right = self.insert_obj_ID(curr.right,id,obj_id)
        else:
            curr.tree2.insertObjID(obj_id)
        
        curr.height = 1 + max(self.getHeight(curr.left),self.getHeight(curr.right))
        balance = self.getBalance(curr)
        if balance > 1:
            if id < curr.left.id:
                return self.rightRotate(curr)
            else:
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)
        if balance < -1:
            if id > curr.right.id:
                return self.leftRotate(curr)
            else:
                curr.right = self.rightRotate(curr.right)
                return self.leftRotate(curr)
        return curr
    
    def getHeight(self,node):
        if node is None:
            return 0
        return node.height
    
    def getBalance(self,node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self,z):
        y = z.right
        
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def rightRotate(self,z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def delete_bin_id(self,bin_id):
        self.root = self.delete_BIN_ID(self.root,bin_id)
    
    def delete_BIN_ID(self,curr,bin_id):
        if curr is None:
            return curr
        
        if bin_id < curr.id:
            curr.left = self.delete_BIN_ID(curr.left,bin_id)
        elif bin_id > curr.id:
            curr.right = self.delete_BIN_ID(curr.right,bin_id)
        else:
            if curr.left is None:
                temp = curr.right
                curr = None
                return temp
            elif curr.right is None:
                temp = curr.left
                curr = None
                return temp
            temp = self.minValueNode(curr.right)
            curr.id = temp.id
            curr.right = self.delete_BIN_ID(curr.right,curr.id)
        
        curr.height = 1 + max(self.getHeight(curr.left),self.getHeight(curr.right))
        balance = self.getBalance(curr)
        if balance > 1:
            if self.getBalance(curr.left) >= 0:
                return self.rightRotate(curr)
            else:
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)
        if balance < -1:
            if self.getBalance(curr.right) <= 0:
                return self.leftRotate(curr)
            else:
                curr.right = self.rightRotate(curr.right)
                return self.leftRotate(curr)
        return curr
    
    def minValueNode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_bin_id(self, bin_id):
        return self.find_bin_ID(self.root, bin_id)

    def find_bin_ID(self, curr, bin_id):
        if curr is None:
            return None
        
        if curr.id == bin_id:
            return curr
        elif curr.id < bin_id:
            return self.find_bin_ID(curr.right, bin_id)
        else:
            return self.find_bin_ID(curr.left, bin_id)
        
    
