# 점수 N이 주어졌을때 자릿수를 기준으로 점수 N을 바능로 나누어 왼쪽 부분의 각 자릿수의 합과
#  오른쪽 부분의 각 자릿수의 합을 더한 값이 동일할 때 'LUCKY' 아니면 'READY'

n = input()
left = 0
right = 0
length = len(n)

for i in range(length//2):
    left += int(n[i])
for i in range(length//2, length):
    right += int(n[i])

if left == right:
    print('LUCKY')
else:
    print('READY')

