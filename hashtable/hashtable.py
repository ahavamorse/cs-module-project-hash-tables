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
# - and delete the node

# RESIZE steps to deal with large amounts of data           O(n) * n is the number of stored items
# - when the load factor (items / capacity) becomes too large (over 0.7)
#     - keep track of number of items with a variable (PUT doesn't always add)
#     - check load factor after each addition and deletion
#         - resize to make larger or smaller (should be between 0.2 and 0.7)
# - create a new array with twice (or half) the space
# - go through the old array and rehash each item
# - store them at the new index in the new array

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
        return self.num_of_items / self.capacity

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
        # index = self.hash_index(key)
        # self.values[index] = HashTableEntry(key, value)

        # Collisions
        index = self.hash_index(key)
        if self.values[index]:
            curr_item = self.values[index]
            while curr_item.next:
                if curr_item.key == key:
                    curr_item.value = value
                    return
                curr_item = curr_item.next
        old_head = self.values[index]
        self.values[index] = HashTableEntry(key, value)
        self.values[index].next = old_head


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        #
        # if self.values[index]:
        #     self.values[index] = None
        # else:
        #     print("Nothing is stored at that key")

        index = self.hash_index(key)
        if self.values[index]:
            curr_item = self.values[index]
            if curr_item.key == key:
                self.values[index] = curr_item.next
                return

            prev_item = curr_item
            curr_item = curr_item.next

            while curr_item.next:
                if curr_item.key == key:
                    prev_item.next = curr_item.next
                    return
                curr_item = curr_item.next




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        # if self.values[index]:
        #     return self.values[index].value
        # else:
        #     return None

        index = self.hash_index(key)
        if self.values[index]:
            curr_item = self.values[index]
            if curr_item.key == key:
                return curr_item.value

            while curr_item.next:
                if curr_item.next.key == key:
                    return curr_item.next.value
                curr_item = curr_item.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        old_values = self.values
        self.values = [HashTableEntry(None, None)] * new_capacity
        self.capacity = new_capacity
        for item in old_values:
            curr_item = item
            while item.next:
                self.put(curr_item.key, item.value)
                curr_item = curr_item.next


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

import unittest


class TestHashTable(unittest.TestCase):

    def test_hash_table_insertion_and_retrieval(self):
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        return_value = ht.get("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.get("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.get("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.get("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.get("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.get("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.get("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.get("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.get("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.get("key-9")
        self.assertTrue(return_value == "val-9")

    def test_hash_table_pution_overwrites_correctly(self):
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        ht.put("key-0", "new-val-0")
        ht.put("key-1", "new-val-1")
        ht.put("key-2", "new-val-2")
        ht.put("key-3", "new-val-3")
        ht.put("key-4", "new-val-4")
        ht.put("key-5", "new-val-5")
        ht.put("key-6", "new-val-6")
        ht.put("key-7", "new-val-7")
        ht.put("key-8", "new-val-8")
        ht.put("key-9", "new-val-9")

        return_value = ht.get("key-0")
        self.assertTrue(return_value == "new-val-0")
        return_value = ht.get("key-1")
        self.assertTrue(return_value == "new-val-1")
        return_value = ht.get("key-2")
        self.assertTrue(return_value == "new-val-2")
        return_value = ht.get("key-3")
        self.assertTrue(return_value == "new-val-3")
        return_value = ht.get("key-4")
        self.assertTrue(return_value == "new-val-4")
        return_value = ht.get("key-5")
        self.assertTrue(return_value == "new-val-5")
        return_value = ht.get("key-6")
        self.assertTrue(return_value == "new-val-6")
        return_value = ht.get("key-7")
        self.assertTrue(return_value == "new-val-7")
        return_value = ht.get("key-8")
        self.assertTrue(return_value == "new-val-8")
        return_value = ht.get("key-9")
        self.assertTrue(return_value == "new-val-9")

    def test_hash_table_removes_correctly(self):
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        return_value = ht.get("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.get("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.get("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.get("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.get("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.get("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.get("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.get("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.get("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.get("key-9")
        self.assertTrue(return_value == "val-9")

        ht.delete("key-9")
        ht.delete("key-8")
        ht.delete("key-7")
        ht.delete("key-6")
        ht.delete("key-5")
        ht.delete("key-4")
        ht.delete("key-3")
        ht.delete("key-2")
        ht.delete("key-1")
        ht.delete("key-0")

        return_value = ht.get("key-0")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-1")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-2")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-3")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-4")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-5")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-6")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-7")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-8")
        self.assertTrue(return_value is None)
        return_value = ht.get("key-9")
        self.assertTrue(return_value is None)

    def test_hash_table_resize(self):
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        ht.resize(1024)

        self.assertTrue(ht.get_num_slots() == 1024)

        return_value = ht.get("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.get("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.get("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.get("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.get("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.get("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.get("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.get("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.get("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.get("key-9")
        self.assertTrue(return_value == "val-9")


if __name__ == '__main__':
    unittest.main()
