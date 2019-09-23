"""
深度优先遍历
对于一颗二叉树，深度优先搜索(Depth First Search)是沿着树的深度遍历的节点，尽可能的搜索树的分支。
深度遍历有重要的三中方法。这三种方法常被用于访问树的节点，它们之间的不同在于访问每个节点的次序不同、
这三种遍历分别叫做先序遍历（preorder），中序遍历（inorder）和后序遍历（postorder）。
"""


# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree(object):
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    """
    先序遍历 在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树
    根节点->左子树->右子树
    """
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    """
    中序遍历 在中序遍历，我们递归使用中序遍历访问左子树，然后访问根节点，最后再递归使用中序遍历访问右子树
    左子树->根节点->右子树
    """
    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    """
    后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
    左子树->右子树->根节点
    """
    def postorder(self, root):
        """递归实现后序遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)