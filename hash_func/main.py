from hash_func import *

class Hash_Table:
    def __init__(self, size, hash_func, dtor):
        self.size_t = size
        self.table = [[None]] * size
        self.Hash_Func = hash_func
        self.destructor = dtor

    def ht_destroy(self):
        self.size_t = 0
        self.table = [[None]] * self.size_t

    def ht_set(self, key, data):
        hash_key = self.Hash_Func(key) % self.size_t
        if self.table[hash_key][0] == None:
            self.table[hash_key] = [[key, data]]
        else:
            self.table[hash_key].append([key,data])

    def ht_get(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        elem = self.table[hash_key]
        for i, key_val in enumerate(elem):
            k, v = key_val
            if key == k:
                return v
        raise Exception("NotExist")

    def ht_has(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        elem = self.table[hash_key]
        if elem == [] or elem[0] == None:
            return 0
        for i, key_val in enumerate(elem):
            k, v = key_val
            if key == k:
                return 1
        return 0

    def ht_delete(self, key):
        hash_key = self.Hash_Func(key) % self.size_t
        if self.ht_has(key) == 0:
            raise Exception("DeleteVoid")
        for i in range(len(self.table[hash_key])):
            if key == self.table[hash_key][i][0]:
                del self.table[hash_key][i]
                return

    def ht_traverse(self, func):
        for i in self.table:
            if i[0] != None:
                for j in i:
                    func(j)

    def ht_resize(self, new_size):
        new_table = [[None]]*new_size
        for i in self.table:
            if i[0] != None:
                for key_val in i:
                    hash_key = self.Hash_Func(key_val[0]) % new_size
                    if new_table[hash_key][0] == None:
                        new_table[hash_key] = [key_val]
                    else:
                        new_table[hash_key].append([key_val])
        self.table = new_table
        self.size_t = new_size

def test_func(a):
    if a[0] == None:
        return 0
    return len(a)

if __name__ == "__main__":
    ht = Hash_Table(5, jenkins_hash, 0)
    ht.ht_set("Peter", "175")
    ht.ht_set("Polina", "155")
    print(ht.ht_get("Peter"))
    print(ht.ht_has("Polina"))
    ht.ht_traverse(test_func)
    ht.ht_resize(10)
    ht.ht_traverse(test_func)
