# 3번 문제
# 입력한 단수의 구구단 결과 출력

x = int(input('단수를 입력하시오: '))
print(f'{x}단 시작')
for y in range(1, 9 + 1):
    if y == 9 + 1: break
    
    print(f'{x*y}', end=' ')