class node:
  def __init__(self,x):
    self.data=x
    self.left=None
    self.right=None

def sum(root):
  if (root==None):
    return 0
  else:
    return root.data+sum(root.left)+sum(root.right)


root=node(12)
root.left=node(40)
root.right=node(76)
root.left.left=node(23)
root.left.right=node(54)
root.right.left=node(63)
root.right.right=node(31)
sum(root)
