lass node:
  def __init__(self,x):
    self.data=x
    self.left=None
    self.right=None

def preorder(root):
  if root==None:
    return
  print(root.data)
  if root:
    preorder(root.left)
    preorder(root.right)
  

root=node('A')
root.left=node('J')
root.right=node('S')
root.left.left=node('T')
root.left.right=node('F')
root.left.right.left=node('M')
root.left.right.right=node('K')
preorder(root)
