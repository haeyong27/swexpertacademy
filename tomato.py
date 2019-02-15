from collections import deque

a = []
column, row = tuple(map(int, input().split()))

for i in range(row):
    a.append(list(map(int, input().split())))

d = [[-1 for i in range(column)] for j in range(row)]
q = deque()
#1 찾기 
for i in range(row):
    for j in range(column):
        if a[i][j] == 1:
            d[i][j] = 0
            q.append((i, j))

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
answer = 0
while q:
    i, j = q.popleft()
    for n in range(4):
        ii = i + dx[n]
        jj = j + dy[n]
        if (0 <= ii < row) and (0 <= jj < column):
            if (d[ii][jj] == -1) and (a[ii][jj] == 0):
                
                d[ii][jj] = d[i][j] + 1
                a[ii][jj] = 1
                q.append((ii, jj))

for i in range(row):
    for j in range(column):
        if answer < d[i][j]:
            answer = d[i][j]
        

for i in a:
    if 0 in i:
        answer  = -1
            


print(answer)