class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def get_next(self):
    return self.next

  def set_next(self, item):
    self.next = item