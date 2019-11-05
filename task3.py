k, n, m, u, v = [float(i) for i in input().split()]
n, m, u, v = int(n), int(m), int(u), int(v)
graf = {i: {} for i in range(n + 1)}

stat = {}
for i in range(m):
    x, y, r = [float(i) for i in input().split()]
    graf[int(x)][int(y)] = r
    graf[int(y)][int(x)] = r
    stat[int(x)] = {}
    stat[int(y)] = {}
q = int(input())
gas = []
if q:
    gas = [int(i) for i in input().split()]

visited = []
queue = [u]
stat[u] = {0: k}
n_queue = []


# first way
# res = float('inf')
#
# def rec(fuel, idx, visited, fill):
#     global res
#     if idx == v:
#         res = min(fill, res)
#         return
#     for i in graf[idx].keys():
#         if i in visited:
#             continue
#         l = graf[idx][i]
#         if fuel >= l:
#             rec(fuel - l, i, visited + [idx], fill)
#         if idx in gas:
#             rec(k - l, i, visited + [idx], fill + 1)
#     return
#
# rec(k, u, [], 0)
# if res == float('inf'):
#     print(-1)
# else:
#     print(res)

# second way

while queue:
    for i in queue:
        if i in visited: continue
        visited.append(i)
        neigh = sorted(graf[i].items(), key=lambda item: item[1])
        for n in neigh:
            r = n[1]
            n = n[0]
            for s in stat[i].items():
                flag =False
                if i in gas and s[1] != k and k >= r:
                    stat[n][s[0] + 1] = max(k - r, stat[n].get(s[0] + 1, 0))
                    flag = True
                if s[1] >= r:
                    stat[n][s[0]] = max(s[1] - r, stat[n].get(s[0], 0))
                    flag = True
                if flag and n not in n_queue:
                    n_queue.append(n)
    queue = n_queue[:]
    n_queue = []
if stat[v] == {}:
    print(-1)
else:
    print(min(stat[v].items(), key=lambda item: item[0])[0])