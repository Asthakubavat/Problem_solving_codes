class BTNode():
    def __init__(self,key):
        self.right=None
        self.left=None
        self.value=key
        
def create(root,l,index,n):
    if(index<n):
        temp=BTNode(l[index])
        root=temp
        root.left=create(root.left,l,2*index+1,n)
        root.right=create(root.left,l,2*index+2,n)
        
    return root
    
def isUnival(root):
    if(root==None):
        return True
        
    if(root.left!=None and root.left.value!=root.value):
        return False
        
    if(root.right!=None and root.right.value!=root.value):
        return False
        
    if(isUnival(root.left) and isUnival(root.right)):
        return True
        
    return False
    
    
    
def countUniNode(root):
    if(root==None):
        return 0
        
    total_count=countUniNode(root.left)+countUniNode(root.right)
    
    if(isUnival(root)):
        total_count+=1

    return total_count    
    
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.value)
        inorder(root.right)
        
    return 


#array contains tree in level order 
a=[1,3,3,2,3]
r=None
r=create(r,a,0,5)
print(countUniNode(r))

