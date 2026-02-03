# DFS binary tree, recursion w/o helper function
class Solution:
#preorderTraversal
    def preorderTraversal(self, root):
		if not root:
            return []
        result = []
        
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result

#InorderTraversal		
	def inorderTraversal(self, root: TreeNode) -> List[int]:
            if not root:
                return []
            result = []
            
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
            return result

#PostorderTraversal
    def postorderTraversal(self, root: TreeNode) -> List[int]:            
        if not root:
            return[]
        result = []
        
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        
        return result