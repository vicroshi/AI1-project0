class Stack:
  
  """class init function"""
  def __init__(self):
    self.stack = []
  
  """checks if stack is empty"""
  def empty(self):
    return len(self.stack) == 0
  
  """pushes element to stack"""
  def push(self,item: str):
    self.stack.append(item)

  """pops last element from stack"""
  def pop(self):
    if self.empty():
      return None
    return self.stack.pop()
  
  """prints stack"""
  def print(self):
    print(self.stack)


s = Stack()
str = input("Please input a sequence of parentheses, using only the characters '( and )', '{ and }' and '[ and ]'\n")
"""the logic here is to push to the stack every opening parentheses and when encountering a closing one,
   pop the stack to see if they match and continue parsing the sequence, else stop and mark it as unbalanced"""
if not len(str) % 2: #if sequence is not even it can't be balanced
  balanced = True
  for i in str:
    if i in "({[": #if we have an opening parentheses push it
      s.push(i)
    elif i in ")}]": #it's a closing parentheses than check if the stack is empty
      if s.empty():  #if it is, then it can't be balanced, because should have pushed an opening one prior to every closing one 
        balanced = False #this also covers the case were a sequence starts with a closing parentheses.
        break
      else:
        j = s.pop() #if it's not empty pop the stack to see what type of opening parentheses it is
        if j+i not in "(){}[]": #if it's an opening one of the same type, then by concatenating them it should be inside the string
          balanced = False #if the concatenation is for example '(}', then it's unbalanced
          break
else:
  balanced = False
answer = "Yes" if balanced else "No"
print("Are the parentheses balanced?\n%s." % answer)