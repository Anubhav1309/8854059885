from bin import Bin
from avl import AVLTree, bin_id__obj_id
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_cap = AVLTree()
        self.bin_obj = bin_id__obj_id()
        self.bins_no = binstree()
        self.object_tree = normaltree()

    def add_bin(self, bin_id, capacity):
        # Implement logic to add a bin to the GCMS
        self.bin_cap.insertBin(bin_id,capacity)
        self.bins_no.append(bin_id,capacity)

    def add_object(self, object_id, size, color): 
        # Implement logic to add an object to the GCMS
        y = 0
        if color == Color.BLUE or color == Color.YELLOW:
            node = self.bin_cap.root
            node = self.find_suitable_cap1(node,size)
    
            if node is None:
                raise NoBinFoundException

            new_node = node.tree.root
            cap = node.capacity - size

            if color == Color.BLUE:
                
                if new_node.left == None and new_node.right == None:
                    y = new_node.id
                    self.bin_cap.delete_cap(node.capacity)
                else:
                    while new_node.left is not None:
                        new_node = new_node.left

                    y = new_node.id
                    node.tree.delete_id(new_node.id)

            else:
                if new_node.left == None and new_node.right == None:
                    y = new_node.id
                    self.bin_cap.delete_cap(node.capacity)
                else:
                    while new_node.right is not None:
                        new_node = new_node.right

                    y = new_node.id
                    node.tree.delete_id(new_node.id)
            
            self.bin_cap.insertBin(y,cap)
            self.bin_obj.insert_obj_id(new_node.id,object_id)
            self.bins_no.remove(y,node.capacity)
            self.bins_no.append(y,cap)
            
        else:
            node = self.bin_cap.root
            node = self.find_suitable_cap2(node,size)
            if node is None:
                raise NoBinFoundException
            
            new_node = node.tree.root
            cap = node.capacity-size
            if color == Color.RED:
                
                if new_node.left == None and new_node.right == None:
                    y = new_node.id
                    self.bin_cap.delete_cap(node.capacity)
                    
                else:
                    while new_node.left is not None:
                        new_node = new_node.left
                    
                    y = new_node.id
                    node.tree.delete_id(new_node.id)
                
            else:
                if new_node.left == None and new_node.right == None:
                    y = new_node.id
                    self.bin_cap.delete_cap(node.capacity)
                    
                else:
                    while new_node.right is not None:
                        new_node = new_node.right
                    
                    y = new_node.id
                    node.tree.delete_id(new_node.id)
            
            self.bin_cap.insertBin(new_node.id,cap)
            self.bin_obj.insert_obj_id(new_node.id,object_id)
            self.bins_no.remove(y,node.capacity)
            self.bins_no.append(y,cap)
        
        self.object_tree.append(object_id, size, y)

    def delete_object(self, object_id):
        new_obj = self.object_tree.find(object_id)
        
        bin_id = new_obj.bin_id
        obj_size = new_obj.size
    
        self.object_tree.remove(object_id)
        new_bin = self.bins_no.find(bin_id)
        bin_cap = new_bin.bin_capacity
        new_cap = new_bin.bin_capacity+obj_size
        self.bins_no.remove(bin_id,bin_cap)
        self.bins_no.append(bin_id,new_cap) 
        
        new_node = self.bin_cap.find_bin(bin_cap)

        new_node.tree.delete_id(bin_id)
        if new_node.tree.root is None:
            self.bin_cap.delete_cap(bin_cap)

        node = self.bin_obj.find_bin_id(bin_id)
        node.tree2.delete_obj_id(object_id)

        self.bin_cap.insertBin(bin_id,new_cap)

    def bin_info(self, bin_id):
        new_bin = self.bins_no.find(bin_id)
        cap = 0
        if new_bin is not None:
            cap = new_bin.bin_capacity

        node = self.bin_obj.find_bin_id(bin_id)
        newroot = None
        if node is not None:
            newroot = node.tree2.root

        object_ids = []
        self.inorder(newroot,object_ids)
        return cap,object_ids

    def inorder(self,node,arr):
        if node is None:
            return
        
        self.inorder(node.left,arr)
        arr.append(node.Obj_id)
        self.inorder(node.right,arr)

    def object_info(self, object_id):
        new_obj = self.object_tree.find(object_id)
        bin_id = 0
        if new_obj is not None:
            bin_id = new_obj.bin_id

        return bin_id

    def find_suitable_cap1(self, node, size,temp=None):
        if node is None:
            return temp
        
        if node.capacity >= size:
            temp = node
            return self.find_suitable_cap1(node.left,size,temp)
        return self.find_suitable_cap1(node.right,size,temp)
            

    def find_suitable_cap2(self, node, size):
        if node is None:
            return None
        
        if node.right is None:
            return node
        else:
            return self.find_suitable_cap2(node.right, size)

    
class binstreenode:
    def __init__(self, bin_id,capacity):
        self.bin_id = bin_id
        self.bin_capacity = capacity
        self.left = None
        self.right = None
        self.height = 1

class binstree:
    def __init__(self):
        self.root = None
    
    def append(self, object_id,capacity):
        if self.root is None:
            self.root = binstreenode(object_id,capacity)
        else:
            self.root = self._append(self.root, object_id,capacity) 
    
    def _append(self, curr, object_id,capacity):   
        if curr is None:
            node = binstreenode(object_id,capacity)
            curr = node
            return curr

        if object_id < curr.bin_id:
            curr.left = self._append(curr.left,object_id,capacity)
        else:
            curr.right = self._append(curr.right,object_id,capacity)
        
        curr.height = 1 + max(self.getHeight(curr.left),self.getHeight(curr.right))
        balance = self.getBalance(curr)
        if balance > 1:
            if object_id < curr.left.bin_id:
                return self.rightRotate(curr)
            else:
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)
        if balance < -1:
            if object_id > curr.right.bin_id:
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

    def remove(self, object_id, capacity):
        self.root = self._remove(self.root, object_id, capacity)

    def _remove(self, node, object_id, capacity):
        if node is None:
            return None

        if object_id < node.bin_id:
            node.left = self._remove(node.left, object_id, capacity)
        elif object_id > node.bin_id:
            node.right = self._remove(node.right, object_id, capacity)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.bin_id, node.bin_capacity = temp.bin_id, temp.bin_capacity 
                node.right = self._remove(node.right, temp.bin_id, temp.bin_capacity)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1:
            if self.getBalance(node.left) >= 0:
                return self.rightRotate(node) 
            else:
                node.left = self.leftRotate(node.left) 
                return self.rightRotate(node)

        if balance < -1:  
            if self.getBalance(node.right) <= 0:
                return self.leftRotate(node) 
            else:
                node.right = self.rightRotate(node.right)  
                return self.leftRotate(node)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def find(self, object_id):
        return self._find(self.root, object_id)

    def _find(self, node, object_id):
        if node is None:
            return None
        if object_id < node.bin_id:
            return self._find(node.left, object_id)
        elif object_id > node.bin_id:
            return self._find(node.right, object_id)
        else:
            return node
        
class normaltreenode:
    def __init__(self, object_id,size,bin_id):
        self.object_id = object_id
        self.size = size
        self.bin_id = bin_id
        self.left = None
        self.right = None
        self.height = 1

class normaltree:
    def __init__(self):
        self.root = None
    
    def append(self, object_id,size,bin_id):
        if self.root is None:
            self.root = normaltreenode(object_id,size,bin_id)
        else:
            self.root = self._append(self.root, object_id,size,bin_id) 
    
    def _append(self, curr, object_id,size,bin_id):   
        if curr is None:
            node = normaltreenode(object_id,size,bin_id)
            curr = node
            return curr

        if object_id < curr.object_id:
            curr.left = self._append(curr.left,object_id,size,bin_id)
        else:
            curr.right = self._append(curr.right,object_id,size,bin_id)
        
        curr.height = 1 + max(self.getHeight(curr.left),self.getHeight(curr.right))
        balance = self.getBalance(curr)

        if balance > 1:
            if object_id < curr.left.object_id:
                return self.rightRotate(curr)
            else:
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)
        if balance < -1:
            if object_id > curr.right.object_id:
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

    def remove(self, object_id):
        self.root = self._remove(self.root, object_id)

    def _remove(self, node, object_id):
        if node is None:
            return None

        if object_id < node.object_id:
            node.left = self._remove(node.left, object_id)
        elif object_id > node.object_id:
            node.right = self._remove(node.right, object_id)
        else:
            if node.left is None and node.right is None:
                node = None
                return node
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._find_min(node.right)
            node.object_id, node.size,node.bin_id = temp.object_id, temp.size,temp.bin_id
            node.right = self._remove(node.right, temp.object_id)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1:
            if self.getBalance(node.left) >= 0:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)

        if balance < -1:
            if self.getBalance(node.right) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def find(self, object_id):
        return self._find(self.root, object_id)

    def _find(self, node, object_id):
        if node is None:
            return None
        if object_id < node.object_id:
            return self._find(node.left, object_id)
        elif object_id > node.object_id:
            return self._find(node.right, object_id)
        else:
            return node
