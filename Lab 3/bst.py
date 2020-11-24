# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:06:24 2020

@author: arnir
"""


class BinarySearchTree:
    
    def __init__(self):
        self._size= 0
        self._root=None
    
    class _Node:
        def __init__(self,key,value):
            self.left=None
            self.right=None
            self.key=key
            self.value=value
            
            
    # Add a node to the BST
    def add(self, key, value):
        node=self._Node(key,value)
        if self._root is None:
            self._root=node
        else:
            root=self._root
            while(root is not None):
                if(key< root.key):
                    if(root.left is None):
                        root.left=node
                        break
                    else:
                        root=root.left
                else:
                    if(root.right is None):
                        root.right=node
                        break
                    else:
                        root=root.right
        self._size +=1
        
            
    # Return the number of nodes in the BST
    def size(self):
        return self._size

    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        list=[]
        if (self._root==None):
            print ("EMPTY TREE")
            return None
        else:    
            self._inorder_traversal(self._root,list)
        return list

    def _inorder_traversal(self,root,list):
        if root is not None:
            self._inorder_traversal(root.left,list)
            list.append(root.key)
            self._inorder_traversal(root.right,list)        
        return list

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        list=[]
        if (self._root==None):
            print ("EMPTY TREE")
            return None
        else:    
            self._postorder_traversal(self._root,list)
        return list

    def _postorder_traversal(self,root,list):
        if root is not None:
            self._postorder_traversal(root.left,list)
            self._postorder_traversal(root.right,list)
            list.append(root.key)
        return list


    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        list=[]
        if (self._root==None):
            print ("EMPTY TREE")
            return None
        else:    
            self._preorder_traversal(self._root,list)
        return list

    def _preorder_traversal(self,root,list):
        if root is not None:
            list.append(root.key)
            self._preorder_traversal(root.left,list)
            self._preorder_traversal(root.right,list)
            
        return list


    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        root=self._root
        if(root is None):
            print ("EMPTY TREE")
            return None
        else:
            while (root is not None):
                if (key==root.key):
                    return root.value
                if(key < root.key):
                    root=root.left
                else:
                    root=root.right
        return False

    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        
        previous = self._root
        root=self._root
        if(root is None):
            print ("EMPTY TREE")
            return None
        
        while root is not None:
            if root.key == key:
                self._size -= 1
                if root.left is None and root.right is None: # LEAF NODE
                    print("Leaf")
                    print(previous.key)
                    if key < previous.key:
                            previous.left = None
                            root = None    
                    else:    
                            previous.right = None
                            root = None
                else:                    
                    if root.right is  None: #Only has One Child
                        print("One Child")
                        if key < previous.key:  #Left Child
                                             
                            previous.left = root.left
                            root = None    
                        else:    #Right Child
                            previous.right = root.left
                            root = None
                    else:   #Both Child is Present
                        print("Both Child")
                        temp = root.right
                        temp_prev = root 
                        while temp.left is not None:    #Find Inorder Sucessor
                            temp_prev = temp
                            temp = temp.left                        
                        root.key = temp.key
                        root.value = temp.value
                        if(temp.key < temp_prev.key):
                            temp_prev.left = None
                        else:
                            temp_prev.right = None
                        
                return ("Node Removed from Tree") 

            elif key < root.key:
                previous = root
                root = root.left

            elif key > root.key:
                previous = root
                root = root.right
            
        return False

    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        root=self._root
        if(root is None):
            print ("EMPTY TREE")
            return None
        else:
            while (root.left is not None):
                root=root.left
        return (root.key,root.value)

    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):
        root=self._root
        if(root is None):
            print ("EMPTY TREE")
            return None
        else:
            while (root.right is not None):
                root=root.right
        return (root.key,root.value)



if __name__=="__main__":
     bst=BinarySearchTree()
     bst.add(10, "Value for 10")
     bst.add(52, "Value for 52")
     bst.add(5, "Value for 5")
     bst.add(8, "Value for 8")
     bst.add(1, "Value for 1")
     bst.add(40, "Value for 40")
     bst.add(30, "Value for 30")
     bst.add(45, "Value for 45")
     print(bst.remove(40))
     print(bst.inorder_walk())
     
     print(bst.preorder_walk())
    
     
    # print(tree.remove(20))  
    
    # print(tree.remove(30))
    
    # print(tree.remove(50))  
