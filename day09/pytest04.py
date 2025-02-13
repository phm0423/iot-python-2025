# 4번 문제
# 입력한 수 거꾸로 출력

numBer=(input('숫자입력: '))
listNumber = numBer.split(' ')
listNumber.reverse()

i = len(listNumber) + 1

while i >= 2: 
    i -= 1
    print(listNumber[-i], end=' ')

