class HashTable:

    def __init__(self):
        self.size = 5
        self.hashmap = [[] for _ in range(0, self.size)]

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
            return slot
        else:
            slot.append((key, value))
            return slot

    def get(self, key):
        hash_key = self.hash_func(key)
        slot = self.hashmap[hash_key]
        if slot:
            for kv in slot:
                k, v = kv
                if key == k:
                    return slot
        elif not slot:
            raise KeyError("The key does not exist.")

    def delete(self, key):
        global i
        hash_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del slot[i]
            return key
        else:
            raise KeyError(key)

    def show_hashmap(self):
        print(self.hashmap)


if __name__ == '__main__':

    hash_table = HashTable()
    print("---List:")
    hash_table.set("Canon", 2400)
    hash_table.set("Sony", 2800)
    hash_table.set("Panasonic", 3000)
    hash_table.show_hashmap()

    print(hash_table.get("Canon"))
    hash_table.delete("Canon")
    hash_table.show_hashmap()