import math
class HashTable:

    EMPTY_SINCE_START = object()
    EMPTY_SINCE_REMOVED = object()
    PRIME = 7

    def get_optimal_prime_table_size(self, approx_items):
        print('\nCreating Double Hash Probing Hash Table...')
        optimal_size = approx_items * 2
        while True:  # keep testing new optimal_size candidates
            for i in range(2, int(math.sqrt(optimal_size))):
                if optimal_size % i == 0:
                    optimal_size += 1
                    break
            else:
                print(f"Hash Table of size {optimal_size} created!\n")
                return optimal_size



    def __init__(self, approx_items):
        self.size = self.get_optimal_prime_table_size(approx_items)
        self.table = [self.EMPTY_SINCE_START] * self.size
        self.count = 0


    def doubleHash(self, i, key):
        return (self.hash1(key) + i * self.hash2(key)) % self.size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return self.PRIME - (key % self.PRIME)

    def insert(self, package):
        if self.count == self.size:
            return False
        for i in range(self.size):
            bucket = self.doubleHash(i, package.getID())
            if self.table[bucket] == self.EMPTY_SINCE_START or self.table[bucket] == self.EMPTY_SINCE_REMOVAL:
                self.table[bucket] = package
                self.count += 1
                return True

        return False


    def remove(self, key):
        for i in range(self.size):
            bucket = self.doubleHash(i, key)
            if self.table[bucket].getID() == key:
                self.table[bucket] = self.EMPTY_SINCE_REMOVED
                self.count -= 1
                return True
            elif self.table[bucket] == self.EMPTY_SINCE_START:
                return False
        return False    

    def search(self, key):
        for i in range(self.size):
            bucket = self.doubleHash(i, key)
            if self.table[bucket].getID() == key:
                return self.table[bucket]
            elif self.table[bucket] == self.EMPTY_SINCE_START:
                return False
        return False 
    def getCount(self):
        return int(self.count)


