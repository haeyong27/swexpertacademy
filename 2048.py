testcase = int(input())

for t in range(testcase):
    n, direction = input().split()
    n = int(n)
    mapp = []

    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    newmap = [[0]*n for _ in range(n)]

    #up
    #temp가 0이면 temp에 현재 값을 넣어준다.
    if direction == 'up':
        for i in range(n):
            index = 0
            temp = 0
            for j in range(n):
                if temp == 0:
                    temp = mapp[j][i]
                elif temp == mapp[j][i]: #전의 값과 같으면 2배 해서 값 삽입해주고, temp는 0으로, index증가
                    newmap[index][i] = temp*2
                    index += 1
                    temp = 0
                else: # 다르면 그냥 그 값을 넣어주고
                    if mapp[j][i] == 0:
                        pass
                    else:
                        newmap[index][i] = temp
                        index += 1
                        temp = mapp[j][i]

                if j == n-1:
                    newmap[index][i] = temp

    #down
    if direction == 'down':
        for i in range(n):
            index = n-1
            temp = 0
            for j in reversed(range(n)):
                if temp == 0:
                    temp = mapp[j][i]
                elif temp == mapp[j][i]: #전의 값과 같으면 2배 해서 값 삽입해주고, temp는 0으로, index증가
                    newmap[index][i] = temp*2
                    index -= 1
                    temp = 0
                else: # 다르면 그냥 그 값을 넣어주고
                    if mapp[j][i] == 0:
                        pass
                    else:
                        newmap[index][i] = temp
                        index -= 1
                        temp = mapp[j][i]

                if j == 0:
                    newmap[index][i] = temp

    #right
    if direction == 'right':
        for j in range(n):
            index = n-1
            temp = 0
            for i in reversed(range(n)):
                if temp == 0:
                    temp = mapp[j][i]
                elif temp == mapp[j][i]: #전의 값과 같으면 2배 해서 값 삽입해주고, temp는 0으로, index증가
                    newmap[j][index] = temp*2
                    index -= 1
                    temp = 0
                else: # 다르면 그냥 그 값을 넣어주고
                    if mapp[j][i] == 0:
                        pass
                    else:
                        newmap[j][index] = temp
                        index -= 1
                        temp = mapp[j][i]

                if i == 0:
                    newmap[j][index] = temp

    #right
    if direction == 'left':
        for j in range(n):
            index = 0
            temp = 0
            for i in range(n):
                if temp == 0:
                    temp = mapp[j][i]
                elif temp == mapp[j][i]: #전의 값과 같으면 2배 해서 값 삽입해주고, temp는 0으로, index증가
                    newmap[j][index] = temp*2
                    index += 1
                    temp = 0
                else: # 다르면 그냥 그 값을 넣어주고
                    if mapp[j][i] == 0:
                        pass
                    else:
                        newmap[j][index] = temp
                        index += 1
                        temp = mapp[j][i]

                if i == n-1:
                    newmap[j][index] = temp
    print(f'#{t+1}')
    for i in range(n):
        for j in range(n):
            print(newmap[i][j], end=' ')
        print()
