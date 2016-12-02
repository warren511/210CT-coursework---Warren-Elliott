class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
def in_order(tree):
    current=tree #create a variable current which is the values in the tree that will be checked
    newstack=[]#create an empty stack
    finished=False #set a boolean 

    while finished==False: #set the iteration to while the stack is not finished 
        if current != None: #if there are values in the tree add them to the new stack
            newstack.append(current)
            current=current.left    #set them to the left hand side 
        else:
            if newstack!=[]:
                current=newstack.pop()
                print (current.value)
                current=current.right
            else:
                finished=True 
        
    
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)


"""Reference:
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/"""
