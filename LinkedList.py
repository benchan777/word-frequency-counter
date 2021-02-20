from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    return new_node


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'{current.data[0]}: {current.data[1]}')
        current = current.next
        
  def find(self,item):

      current = self.head

      found = False

      while current != None and not found:
        if current.data[0] == item:
          increment = current.data[1] + 1
          current = (current.data[0], increment)
          found = True
        else:
          current = current.next

      if found:
        return current
      else:
        return -1

  def replace(self, item):
    next_item = item.get_next()
    next_next_item = next_item.get_next()

    # replace duplicate node with head by assigning pointer to the node after the duplicate node
    # if no node exists, set new node pointer to none
    if next_next_item == None:
      item.next = None

    else:

      # if a node does exist after the duplicate node, check for the existence of another duplicate node further down the list
      # if a duplicate node exists further down the list, delete duplicate node
      if self.find(item.data[0]) != -1:
        current = self.head
        second = self.head

        # traverse through the entire list and check for duplicate node by comparing the head to every node in the linked list
        # if a duplicate is found, delete it by pointing the node previous to the duplicate node to point to the node after the duplciate node
        while second.get_next() != None:
          if second.get_next().data[0] == current.data[0]:
            if second.get_next().get_next() != None:
              second.next = second.get_next().get_next()
            if second.get_next().get_next() == None:
              second.next = None
            if second == None:
              break
          else:
            second = second.get_next()

      # sets the new node to point to the next node
      item.next = next_item