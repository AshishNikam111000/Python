import os
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        ''' Collision Handling - Chaining Method '''
        '''
        found = False
        for index, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0]==key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        '''
        
        ''' Collision Handling - Linear Probing Method '''
        done = False
        found = False
        for index, ele in enumerate(self.arr[h]):
            if ele==key:
                self.arr[h] = (key, value)
                found = True
                break
        if not found:
            if self.arr[h] == []:
                self.arr[h] = (key, value)
                done = True
            else:
                for i in range(h+1, self.MAX):
                    if self.arr[i] == []:
                        self.arr[i] = (key, value)
                        done = True
                        break
                if not done:
                    for i in range(0, h):
                        if self.arr[i] == []:
                            self.arr[i] = (key, value)
                            done = True
                            break

    def __getitem__(self, key):
        h = self.get_hash(key)
        '''
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
        '''
        if self.arr[h][0] == key:
            return self.arr[h][1]
        else:
            for index, ele in enumerate(self.arr):
                if ele[0] == key:
                    return self.arr[index][1]
            
    def __delitem__(self, key):
        h = self.get_hash(key)
        '''
        for index, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][index]
        '''
        if self.arr[h][0] == key:
            del self.arr[h]
        else:
            for index, ele in enumerate(self.arr):
                if ele[0] == key:
                    self.arr[index] = []
                    break

    def display(self):
        print()
        print(self.arr)

os.system('cls')
t = HashTable()
t["march 6"] = 130
t["D d"] = 168
t["march 6"] = 78
t["march 1"] = 20
t["dec 17"] = 209
t["march 17"] = 254
t.display()

del t["march 17"]
del t["march 6"]
t.display()