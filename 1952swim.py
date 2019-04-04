def dfs(idx, sum):
    global min_price
    if idx >= 12:
        if min_price > sum:
            min_price = sum
        return

    if month[idx] == 0:
        dfs(idx + 1, sum)

    for i in range(3):
        if i == 0:
            temp = month[idx] * price[i]
            sum += temp
            if min_price < sum:
                sum -= temp
                continue
            dfs(idx + 1, sum)
            sum -= temp

        elif i == 1:
            temp = price[i]
            sum += temp
            if min_price < sum:
                sum -= temp
                continue
            dfs(idx + 1, sum)
            sum -= temp

        elif i == 2:
            temp = price[i]
            sum += temp
            if min_price < sum:
                sum -= temp
                continue
            dfs(idx + 3, sum)
            sum -= temp



n = int(input())

for tc in range(n):
    price = list(map(int, input().split(' ')))
    month = list(map(int, input().split(' ')))
    min_price = price[3]
    dfs(0, 0)
    print(f'#{tc+1} {min_price}')
