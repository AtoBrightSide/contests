from collections import Counter, defaultdict


def main():
    n, m = input().split()
    print(solution(int(n), int(m)))


def solution(n, m):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(node):
        if node == parent[node]:
            return node

        parent[node] = find(parent[node])
        return find(parent[node])

    def unite(a, b):
        pa = find(a)
        pb = find(b)

        if pa != pb:
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
                rank[pb] = 0
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
                rank[pa] = 0
            return True

        return False
    

    graph = defaultdict(list)
    ans = 0
    for _ in range(m):
        u, v = input().split()
        unite(int(u) - 1, int(v) - 1)
        graph[u].append(v)
        graph[v].append(u)
    
    temp = [node for node in parent]
    
    return ans


main()
