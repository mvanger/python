# Building a class
class Stack(object):

  def __init__(self):
    self.stack = []

  def push(self, object):
    self.stack.append(object)

  def pop(self):
    return self.stack.pop()

  def length(self):
    return len(self.stack)

a = Stack()
a.push(5)
a.push(10)
print a.pop()
print a.length()
print a.stack