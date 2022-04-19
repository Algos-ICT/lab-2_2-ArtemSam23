from tree import Node


def check(root):
        if root is None:
            return None
        que = []
        que.append((root, -1000000000, 10000000000))
        while len(que) > 0:
            line = que.pop(0)
            node = line[0] 
            if node.left is not None:
                if(node.left.key >= node.key) or (node.left.key >= line[2]) or (node.left.key <= line[1]):
                    return False
                que.append((node.left, line[1], node.key))
            if node.right is not None:
                if(node.right.key < node.key) or (node.right.key > line[2]) or (node.right.key <= line[1]):
                    return False
                que.append((node.right, node.key, line[2]))
        return True


inp = open('input.txt')
n = int(inp.readline())
lines = [inp.readline() for _ in range(n)]
nodes = []
K = []
L = []
R = []

for i in range(n):
    Ki, Li, Ri = lines[i].split()
    node = Node(int(Ki))
    nodes.append(node)
    K.append(int(Ki))
    L.append(int(Li))
    R.append(int(Ri))

for i in range(n):
    l = L[i]
    r = R[i]
    if l != -1:
        nodes[i].left = nodes[l]
    if r != -1:
        nodes[i].right = nodes[r]
inp.close()

if nodes:
    result = check(nodes[0])
else:
    result = True

if __name__ == '__main__':
    out = open('output.txt', 'w')
    if result:
        out.write("CORRECT")
    else:
        out.write("INCORRECT")
    out.close()
