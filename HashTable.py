from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    array = []

    # creates an array and populates it with specified number of linked lists
    for i in range(size):
      linkedlist = LinkedList()
      array.append(linkedlist)

    return array

  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  # generates an index based on the first letter of each string being input
  def hash_func(self, key):
    first_letter = key[0]
    distance = ord(first_letter) - ord('a')
    index = distance % self.size

    return index

  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value 
  # is a counter for the number of times the word appeared. When inserting a new word in the 
  # hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    #run the hash function to generate a key hash
    key_hash = self.hash_func(key)
    # assign a tuple containing key and value to the variable item
    item = (key, value)

    # run the find method to see if any duplicates exist
    new_item = self.arr[key_hash].find(key)

    #if a duplicate exists, append the duplicate to the linked list, then run the replace method to remove the old duplicate
    if new_item != -1:
      new_object = self.arr[key_hash].append(new_item)
      self.arr[key_hash].replace(new_object)

    else:
      self.arr[key_hash].append(item)


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    # traverses the entire hashtable and prints out all the data in every linked list within the table
    for i in range(self.size):
      self.arr[i].print_nodes()
