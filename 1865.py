n = 3
s = '''13 1 50
12 70 90
25 60 100'''
mapp = []
s = s.split('\n')
for i in s:
    mapp.append(i.split(' '))

check = [0 for _ in range(n)]

for i in mapp:
    print(i)
ans = 1
max = 0

def dfs(a):
    global ans
    global max
    if a == n:
        if max < ans:
            max = ans
        return

    for i in range(n):
        if check[i] == 1:
            continue
        check[i] = 1
        ans = ans * int(mapp[a][i]) * .01
        dfs(a+1)
        ans = ans / int(mapp[a][i]) * 100
        check[i] = 0

dfs(0)
print(max*100)
