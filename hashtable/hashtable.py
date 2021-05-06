# A Hash function turns a string into a number
# Must be deterministic (same input always returns same output)

# String.encode() turns it into bytes (numbers)
# Adding the unicode values of the numbers creates a deterministic result
# This would run in O(n) where n is the length of the string (this will very rarely be huge)
# We then map the result to an index in an array by using % length of array (modulo to find remainder)

# Summary of steps to insert a key and value into a hash table:
# - hash key to convert it to a number
# - take that number and MOD it by the size of the hash table
# - insert the value into the index given by the MOD operation

# Summary of steps to retrieve a value given a specific key from a hash table:
# - hash the key to convert it to a number
# - use MOD to find the index within the array
# - use this new index to find the value in the array

# Dealing with Collisions

# PUT steps to deal with collisions         O(m) * m is the number of items in the largest linked list
# - hash the key to get the index
# - find the start of the linked list with the index
# - see if the key already exists and update the value
# - otherwise insert it into the linked list as a new HashTableEntry

# GET steps to deal with collisions         O(m) * m is the number of items in the largest linked list
# - hash the key to get the index
# - get the linked list at the index
# - see if the key exists in the linked list
# - otherwise return None

# DELETE steps to deal with collisions          O(m) * m is the number of items in the largest linked list
# - hash the key to get the index
# - get the linked list at the index
# - see if the key exists in the linked list
# - delete the node and return the value

# RESIZE steps to deal with large amounts of data           O(n) * n is the number of stored items
# - when the load factor (items / capacity) becomes too large (over 0.7)
#     - keep track of number of items with a variable (PUT doesn't always add)
#     - check load factor after each addition and deletion
#         - resize to make larger or smaller (should be between 0.2 and 0.7)
# - create a new array with twice (or half) the space
# - go through the old array and rehash each item
# - store them at the new index in the new array
# -

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.values = [HashTableEntry(None, None)] * capacity
        self.capacity = capacity
        self.num_of_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        # If something already exists at that index print a warning

        self.values[index] = HashTableEntry(key, value)
        # if self.values[index]:
        #     self.values[index].next = HashTableEntry(key, value)
        # else:
        #     self.values[index] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.values[index]:
            self.values[index] = None
        else:
            print("Nothing is stored at that key")



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.values[index]:
            return self.values[index].value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


# if __name__ == "__main__":
#     ht = HashTable(8)
#
#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")
#
#     print("")
#
#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))
#
#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()
#
#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")
#
#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))
#
#     print("")
