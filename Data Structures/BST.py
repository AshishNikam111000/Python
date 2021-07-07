import os

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def InorderT(self):
        ele = []
        if self.left:
            ele += self.left.InorderT()

        ele.append(self.data)

        if self.right:
            ele += self.right.InorderT()

        return ele

    def PreorderT(self):
        ele = []
        ele.append(self.data)

        if self.left:
            ele += self.left.PreorderT()

        if self.right:
            ele += self.right.PreorderT()

        return ele
    
    def PostorderT(self):
        ele = []
        if self.left:
            ele += self.left.PostorderT()

        if self.right:
            ele += self.right.PostorderT()

        ele.append(self.data)

        return ele

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        return self.left.find_min() if self.left else self.data

    def find_max(self):
        return self.right.find_max() if self.right else self.data
        
    def calculate_sum(self):
        total = 0
        if self.left:
            total += self.left.calculate_sum()

        total += self.data

        if self.right:
            total += self.right.calculate_sum()
        
        return total

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            ''' By finding min value from right sub-tree '''
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            ''' By finding max value from left sub-tree '''
            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete(max_val)
        return self

os.system('cls')

numbers = [17, 4, 1, 20, 9, 23, 18, 34, 25, 0, 5, 8, 75]
root = BSTNode(numbers[0])
for i in range(1, len(numbers)):
    root.add_child(numbers[i])

print("Inorder: ", root.InorderT())
print("Preorder: ", root.PreorderT())
print("Postorder: ", root.PostorderT())
print("Search Result: ", root.search(20))

print("Find Min: ", root.find_min())
print("Find Max: ", root.find_max())
print("Calculate Sum: ", root.calculate_sum())

print("Before Delete: ", root.InorderT(), len(root.InorderT()))
root.delete(9)
print("After Delete: ", root.InorderT(), len(root.InorderT()))