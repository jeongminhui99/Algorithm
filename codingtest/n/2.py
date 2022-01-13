#from extratypes import Tree
def largestpath(node, m):
    if (not node):
        return len(m)
    if node.x in m:
        return len(m)
    else:
        m[node.x] = 1
    max_path = max(largestpath(node.l, m), largestpath(node.r, m))
    m[node.x] -= 1

    if m[node.x] == 0:
        del m[node.x]
    return max_path

def solution(T):
    if(T.l == None and T.r == None):
        return 1
    elif T.x == None:
        return 0
    else:
        Hash = {}
        return largestpath(T, Hash)
