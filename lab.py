import itertools

n, m = tuple(map(int, input().split()))
l = []
for i in range(n):
    l.append(input().split())
temp_l = l[:]

#안전영역 세는 함수
def count():
    count = 0
    for i in range(n):
        for j in range(m):
            if l[i][j] == '0':
                count += 1
    return count

#바이러스 퍼뜨리는 함수 
def spread():
    move = ((1,0), (0,1), (-1,0), (0,-1))
    virus_stack = []
    for i in range(n):
        for j in range(m):
            if l[i][j] == '2':
                virus_stack.append((i, j))

    while(virus_stack):
        x, y = virus_stack.pop(0)
        for i in range(4):
            xx = x+move[i][0]
            yy = y+move[i][1]
            if (0<=xx<n) and (0<=yy<m) and l[xx][yy] == '0':
                virus_stack.append((xx,yy))
                l[xx][yy] = '2'
    ans = max(ans, count())

#벽 세우는 함수
def wall(cnt):
    if cnt == 3:
        spread()
        answer.append(count())
        return

    for i in range(n):
        for j in range(m):
            if l[i][j] == '0':
                l[i][j] = '1'
                cnt += 1
                wall(cnt)
                cnt -= 1

wall(1)
print(max(answer))
