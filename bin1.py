T = int(input())

#A->10, B->11...
def hexTodeci(s):
    try:
        s = int(s)
    except:
        s = ord(s) - ord('A') + 10
    return s

#2진수로 바꾸기
def deciTobin(i):
    l = []
    while(i>0):
        l.append(i%2)
        i = int(i/2)
    while(len(l) < 4):
        l.append(0)
    l.reverse()
    s = ''
    for i in l:
        s += str(i)
    return s


for t in range(1, 1+T):
    length, string = input().split()
    answer = ''
    
    for i in string:
        answer += deciTobin(hexTodeci(i))
        
    print('#{} {}'.format(t, answer))