class Stack:
  
  def __init__(self):
    self.stack = []
  
  def empty(self):
    return len(self.stack) == 0
  
  def push(self,item: str):
    self.stack.append(item)

  def pop(self):
    if self.empty():
      return None
    return self.stack.pop()
  
  def print(self):
    print(self.stack)


s = Stack()
str = input("Please input a sequence of parentheses, using only '(', '{' and '['\n")

if not len(str) % 2:
  balanced = True
  for i in str:
    if i in "({[":
      s.push(i)
    elif i in ")}]":
      if s.empty():
        balanced = False
        break
      else:
        j = s.pop()
        if j+i not in "(){}[]":
          balanced = False
          break
else:
  balanced = False
answer = "Yes" if balanced else "No"
print("Are the parentheses balanced?\n%s." % answer)