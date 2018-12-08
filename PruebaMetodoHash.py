'''
Created on 04/12/2018

@author: acer
'''

class hash_table:
    def __init__(self):
        self.table = [None] * 127
        
    def Hash_func(self, value):
        key = 0
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127
    
    def Insert(self, value):
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
            
    def Search(self, value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            print("Se encontró el elemento en")
            return id(self.table[hash])
        
    def Remove(self, value):
        


H = hash_table()
H.Insert("Alo")
H.Insert("Bou")
H.Insert("Col")

print(H.Search("Bou"))