class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

# LCA of v1 an v2, 
# if v1 and v2 is node.data, then return the node as LCA 
# if v1 and v2 in the left, discard right, 
# if v1 and v2 in the right, discard left 
# if node data is in the middle, then return node as LCA 

def lca(root : Node, v1 : int, v2 :int ) -> Node:
    if not root:
        return None
    if v1<=root.info <= v2 or v2<=root.info <=v1: 
        return root
    elif v1 < root.info and v2 < root.info:
        return lca(root.left, v1 ,v2)
    else:
        return lca(root.right, v1 ,v2)
        
tree = BinarySearchTree()