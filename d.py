from collections import deque

n, m = list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
landmarks = [-1] * (n+1)
for i in range(m):
  a, b = list(map(int, input().split()))
  edges[a].append(b)
  edges[b].append(a)

queue = deque()
landmarks[1] = 0
queue.append(1)
while len(queue) != 0:
  v = queue.popleft()
  for i in edges[v]:
    if landmarks[i] != -1:
      continue
    landmarks[i] = v
    queue.append(i)
flag = 1
for i in range(2,n+1):
  if landmarks[i] == -1:
    flag = 0
if flag:
  print('Yes')
  for i in range(2,n+1):
    print(landmarks[i])
else:
  print('No')
