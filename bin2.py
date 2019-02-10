T = int(input())

def solution(N):
    answer = ''
    l = []
    for i in range(1, 13):
        l.append(1/2**i)

    for i in l:
        
        if(N - i >= 0):
            answer += '1'
            N = N - i
            if(N == 0):
                break
        else:
            answer += '0'
        
    if (N == 0):
        return answer
    else:
        return 'overflow'


for t in range(1, T+1):
    f = float(input())
    print('#{} {}'.format(t, solution(f)))
