class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n)) 
        self.rank = [1] * n 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    n, m = map(int, input().split())
    events = []
    for _ in range(m):
        line = tuple(map(int, input().split()))
        events.append(line)

    dsu = DisjointSetUnion(n)
    paths = []  
    result = []

    for e, v, u in events:
        v -= 1 
        u -= 1
        if v > u: 
            v, u = u, v

        if e == 1:
            for x, y in paths:
                if (v < x < u and u < y) or (x < v < y and y < u):
                    dsu.union(v, x)
                    dsu.union(u, y)
            dsu.union(v, u)
            paths.append((v, u))
        elif e == 2:
            result.append('1' if dsu.connected(v, u) else '0')

    ans = ''.join(result)
    print(ans)
