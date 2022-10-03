import math
#btlist = [1,3,9,None,None,15,7,None,None,None,None,67,8,9,0]
btlist = [3,9,20,None,None,15,7]

class BinaryTree:
    def __init__(self, value, deep=0, left=None, right=None) -> None:
      self.value = value
      self.left = left
      self.right = right
      self.deep = deep
    

index = 0
root=[]
def creating_binary_tree(btlist, index, rtree=root):
  if index >= len(btlist):
    return rtree

  elif len(btlist) > 2*index+1 and len(btlist) > 2*index+2:
    tree = BinaryTree(btlist[index])
    tree.left = btlist[2*index+1]
    tree.right = btlist[2*index+2]
    tree.deep = math.trunc(math.log(index+1,2))+1
    index+=1
    rtree.append(tree)
    return creating_binary_tree(btlist,index,root)
  
  else:
    tree = BinaryTree(btlist[index])
    tree.deep = math.trunc(math.log(index+1,2))+1
    index+=1
    rtree.append(tree)
    return creating_binary_tree(btlist,index,root)    
  
ftree = creating_binary_tree(btlist,index,root)
print(ftree)
lowest_deep=100
for i in ftree:
  if i.left == None and i.right == None and lowest_deep > i.deep:
    lowest_deep = i.deep
    
print(lowest_deep)
  