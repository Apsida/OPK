from hash_func import *
class Hash_Table:
    def __init__(self, size, hash_func, dtor):
        self.size_t = size
        self.table = [None] * size
        self.Hash_Func = hash_func
        self.destructor = dtor

    def ht_destroy(self):
        self.size_t = 0
        self.table = [None] * self.size_t

    def ht_set(self, key, data):
        hash_key = self.Hash_Func(key) % self.size_t
        self.table[hash_key] = data

    def ht_get(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        elem = self.table[hash_key]
        if elem != None:
            return elem
        raise Exception("NotExist")

    def ht_has(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        elem = self.table[hash_key]
        if elem != None:
            return 1
        return 0

    def ht_delete(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        if self.ht_has(key) == 0:
            raise Exception("DeleteVoid")
        self.table[hash_key] = None

    def ht_traverse(self, func):


    def ht_resize(self, new_size):
        return 0

if __name__ == "__main__":
    ht = Hash_Table(3, jenkins_hash, 0)
    ht.ht_set("Peter", "175")
    ht.ht_set("Polina", "165")
    print(ht.ht_get("Peter"))
    print(ht.ht_has("Polina"))
    ht.ht_delete("Polina")
    print(ht.ht_has("Polina"))