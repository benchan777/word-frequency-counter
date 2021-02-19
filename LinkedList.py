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
    if next_next_item == None:
      item.next = None
    else:

      if self.find(item.data[0]) != -1:
        current = self.head
        second = self.head

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

      item.next = next_item