
class Node:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tree = inner_tree(capacity) 
        self.left = None
        self.right = None
        self.height = 1

class Node2:
    def __init__(self,id):
        self.id = id
        self.tree2 = inner_tree2(id)
        self.left = None
        self.right = None
        self.height = 1


class inner_node2:
    def __init__(self, Obj_id):
        self.Obj_id = Obj_id
        self.height = 1
        self.left = None
        self.right = None

class inner_tree2:
    def __init__(self, id):
        self.root = None
        self.id = id

    def insertObjID(self, Obj_id):
        self.root = self.insert_obj_id(self.root, Obj_id)    

    def insert_obj_id(self, curr, Obj_id):
        if curr is None:
            return inner_node2(Obj_id)

        if Obj_id < curr.Obj_id:
            curr.left = self.insert_obj_id(curr.left, Obj_id)
        else:
            curr.right = self.insert_obj_id(curr.right, Obj_id)

        curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))

        balance = self.getBalance(curr)

        if balance > 1: 
            if Obj_id < curr.left.Obj_id:
                return self.rightRotate(curr)
            else:  
                curr.left = self.leftRotate(curr.left)
                return self.rightRotate(curr)

        if balance < -1: 
            if Obj_id > curr.right.Obj_id: 
                return self.leftRotate(curr)
            else: 
                curr.right = self.rightRotate(curr.right)
                return self.leftRotate(curr)

        return curr

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def delete_obj_id(self, Obj_id):
        self.root = self.delete_OBJ_ID(self.root, Obj_id)

    def delete_OBJ_ID(self, curr, Obj_id):
        if curr is None:
            return curr

        if Obj_id < curr.Obj_id:
            curr.left = self.delete_OBJ_ID(curr.left, Obj_id)
        elif Obj_id > curr.Obj_id:
            curr.right = self.delete_OBJ_ID(curr.right, Obj_id)
        else:
            if curr.left is None and curr.right is None:
                curr = None
                return curr
            elif curr.left is None:
                temp = curr.right
                curr = None
                return temp
            elif curr.right is None:
                temp = curr.left
                curr = None
                return temp
           
            temp = self.minValueNode(curr.right)
            curr.Obj_id = temp.Obj_id
            curr.right = self.delete_OBJ_ID(curr.right, curr.Obj_id)

        if curr is not None:
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

class inner_node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
        self.height = 1

class inner_tree:
    def __init__(self, capacity):
        self.root = None
        self.capacity = capacity

    def insertID(self, id):
        self.root = self.insert_id(self.root, id)

    def insert_id(self, curr, id):
        if curr is None:
            return inner_node(id)

        if id < curr.id:
            curr.left = self.insert_id(curr.left, id)
        else:
            curr.right = self.insert_id(curr.right, id)

        if not curr:
            return curr
        
        curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))
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

    def delete_id(self, id):
        self.root = self.delete(self.root, id)

    def delete(self, curr, id):
        if curr is None:
            return curr

        if id < curr.id:
            curr.left = self.delete(curr.left, id)
        elif id > curr.id:
            curr.right = self.delete(curr.right, id)
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
            curr.right = self.delete(curr.right, temp.id)

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
            if self.getBalance(curr.right) <= 0:
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

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        if z.left is None:
            return z
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
