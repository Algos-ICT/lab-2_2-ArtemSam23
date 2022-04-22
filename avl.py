class Node:
    def __init__(self, num):
        self.key = num
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    return root.height if root is not None else 0


def balance_factor(root):
    return height(root.right) - height(root.left)


def fix_height(root):
    left = height(root.left)
    right = height(root.right)
    root.height = max(left, right) + 1


class Tree:
    @staticmethod
    def rotate_r(root):
        q = root.left
        root.left = q.right
        q.right = root
        fix_height(root)
        fix_height(q)
        return q

    @staticmethod
    def rotate_l(root):
        p = root.right
        root.right = p.left
        p.left = root
        fix_height(root)
        fix_height(p)
        return p

    def balance(self, root):
        fix_height(root)
        if balance_factor(root) == 2:
            if balance_factor(root.right) < 0:
                root.right = self.rotate_r(root.right)
            return self.rotate_l(root)
        if balance_factor(root) == -2:
            if balance_factor(root.left) > 0:
                root.left = self.rotate_l(root.left)
            return self.rotate_r(root)
        return root

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return self.balance(root)

    def find_right(self, root):
        if root.right is not None:
            return self.find_right(root.right)
        return root

    def find_right_and_delete(self, root):
        if root.right is not None:
            if root.right.right is None:
                root.right = None if root.right.left is None else root.right.left
            else:
                root.right = self.find_right_and_delete(root.right)
        return self.balance(root)

    def remove(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            else:
                new_root = self.find_right(root.left)
                root.key = new_root.key
                if root.left.key == new_root.key:
                    root.left = None if (root.left.left is None) else root.left.left
                else:
                    root.left = self.find_right_and_delete(root.left)
        return self.balance(root)

    @staticmethod
    def stringify(root):
        que = []
        number = 1
        que.append(root)
        ans = []
        while len(que) > 0:
            node = que.pop(0)
            line = f"{node.key} "
            if node.left is not None:
                number += 1
                line += f"{number} "
                que.append(node.left)
            else:
                line += "0 "

            if node.right is not None:
                number += 1
                line += f"{number}\n"
                que.append(node.right)
            else:
                line += "0\n"
            ans.append(line)
        return ans
