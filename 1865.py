T = int(input())
for testcase in range(T):

    n = int(input())
    ans = 1
    max = 0
    check = [0 for _ in range(n)]

    mapp = []
    for i in range(n):
        mapp.append(input().split(' '))
    
    def dfs(a, ans):
        global max
        if a == n:
            if max < ans:
                max = ans
            return
        if max >= ans:
            return
        for i in range(n):
            if check[i] == 1:
                continue

            if int(mapp[a][i]) == 0:
                continue



            check[i] = 1
            dfs(a+1, ans*int(mapp[a][i])*0.01)
            check[i] = 0

    dfs(0, 1)
    print('#{} {:.6f}'.format(testcase+1, max * 100))

