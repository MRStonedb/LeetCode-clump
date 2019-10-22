"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
"""

class solution():
    def getMaxDeep(self, root):
        if not root:
            return 0
        max_l = self.getMaxDeep(root.left)  # 左子树的最大深度
        max_r = self.getMaxDeep(root.right) # 右子树的最大深度
        return max(max_l, max_r) + 1      # 深度加上根节点

    def maxDepth(self, root):
        stack = []                                              # 定义一个空栈，栈中的元素是结点及其对应的深度
        if root:                                                # 如果根结点不为空
            stack.append((root, 1))                             # 则将根节点及其对应深度1组成的元组入栈
        max_depth = 0                                           # 初始化最大深度为零
        while stack:                                            # 当栈非空时
            tree_node, cur_depth = stack.pop()                  # 弹出栈顶结点及其对应的深度
            if tree_node:                                       # 如果该结点不为空
                max_depth = max(max_depth, cur_depth)           # 更新当前最大深度，如果该结点深度更大的话
                stack.append((tree_node.left, cur_depth+1))     # 将该结点的左孩子结点及其对应深度压入栈中
                stack.append((tree_node.right, cur_depth+1))    # 将该结点的右孩子结点及其对应深度压入栈中

        return max_depth



root = [3,9,20,None,None,15,7]
s = solution()
# print(s.getMaxDeep(root))
print(s.maxDepth(root))

