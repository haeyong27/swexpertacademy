n=int(input())
l = []
for i in range(n):
    l.append(list(input()))

d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if (l[i][j] == '1') and (d[i][j] == 0):
            cnt += 1
            stack = [(i, j)]
            while(stack):
                a, b = stack.pop(0)
                d[a][b] = cnt
                if a+1 >= n or b+1 >= n or a-1 < 0 or b-1 < 0:
                    continue
                if l[a+1][b] == '1' and d[a+1][b] == 0:
                    stack.append((a+1, b))
                if l[a][b+1] == '1' and d[a][b+1] == 0:
                    stack.append((a, b+1))
                if l[a-1][b] == '1' and d[a-1][b] == 0:
                    stack.append((a-1, b))
                if l[a][b-1] == '1' and d[a][b-1] == 0:
                    stack.append((a, b-1))
                


answer =[0 for _ in range(cnt+1)]
for i in range(n):
    for j in range(n):
        answer[d[i][j]] += 1

print(cnt)
answer = answer[1:]
answer.sort()
for i in answer:
    print(i)