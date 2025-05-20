class HashTable:

    EMPTY_SINCE_START = object()
    EMPTY_SINCE_REMOVED = object()

    def __init__(self, table_size=10):
        self.table = [EMPTY_SINCE_START] * table_size
        self.size = table_size
        self.c1 = 7
        self.c2 = 13
        self.count = 0


    def quadraticHash(self, i, baseHash):
        return (baseHash + (c1 * i) + (c2 * i**i)) % self.table_size

    def baseHash(self, key):
        return key % self.table.size

    def insert(self, key):
        #find bash hash
        basheHash = baseHash(key)
        #find Bucket
        bucket = baseHash

        for i in range(self.size):
            if

        pass

    def remove(key):
        pass

    def search(key):
        pass


