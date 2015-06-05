class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    res=[]
    def printTree(self, root):
        if not root:
            return []
        if root:
            self.res.append(root.val)
            if root.left:
                self.printTree(root.left)
            if root.right:
                self.printTree(root.right)
        return self.res
class Solution:
    def morris_inorder(self, root):
        res = []
        p = root
        while p:
            if p.left is None:
                res.append(p.val)
                p = p.right
            else:
                tmp = p.left
                while tmp.right and tmp.right != p:
                    tmp = tmp.right
                if  tmp.right is None:
                    tmp.right = p
                    p = p.left
                else:
                    res.append(p.val)
                    tmp.right = None
                    p = p.right
        return res
    def morris_preorder(self, root):
        res = []
        current = root           
        while current:           
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    res.append(current.val)
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    current = current.right
        return res
    def reverse(self, p1, p2):
        if p1 == p2:
            return
        pre = p1
        p = p1.right
        
        while 1:
            tmp = p.right
            p.right = pre
            if p == p2:
                break
            pre = p
            p = tmp
    def helper(self,p1, p2 ):
        self.reverse(p1,p2)
        p = p2
        while 1:
            self.res.append(p.val)
            if p == p1:
                break
            p = p.right
        self.reverse(p1,p2)
    def morris_postorder(self, root):
        self.res = []
        dump = TreeNode(-1)
        dump.left = root
        cur = dump
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    self.helper(cur.left, pre)
                    pre.right = None
                    cur = cur.right
        return self.res

    
if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(None)
    root= TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(None)
    root.left.right = TreeNode(1)
    
    print tree.printTree(root)
    print sol.morris_preorder(root)
    print sol.morris_inorder(root)
    print sol.morris_postorder(root)
