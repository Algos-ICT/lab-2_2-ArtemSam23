import avl

inp = open("input.txt")
n = int(inp.readline())
lines = [inp.readline() for _ in range(n)]
lines.reverse()
nodes = {}
tree = avl.Tree()
for i in range(n):
    Ki, Li, Ri = map(int, lines[i].split())
    node = avl.Node(int(Ki))
    nodes[n - i] = node
    if Li != 0 and Ri != 0:
        node.left = nodes[Li]
        node.right = nodes[Ri]
        avl.fix_height(node)
    elif Li != 0:
        node.left = nodes[Li]
        avl.fix_height(node)
    elif Ri != 0:
        node.right = nodes[Ri]
        avl.fix_height(node)
    else:
        node.height = 1

if len(nodes) == 0:
    nodes[1] = None

key = int(inp.readline())
root = tree.remove(nodes[1], key)

out = open("output.txt", "w")
ans = tree.stringify(root)
if ans is not None:
    out.write(f"{len(ans)}\n")
    for i in ans:
        out.write(i)
else:
    out.write("0")

out.close()
inp.close()
