# 가로의 길이가 N, 세로의 길이가 2인 직사작형 형태의 얇은 바닥이 있다.
# 1x2, 2x1, 2x2의 덮개를 이용해 채우고자 한다.
# 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
# 아이디어 : 왼쪽부터 i-1까지 길이가 이미 채워져있으면 2x1의 덮개를 채우는 하나의 경우밖에 존재하지 않는다.
#           왼쪽부터 i-2까지 길이가 덮개로 이미 채워져 있으면 1x2 덮개 2개 넣는 경우, 혹은 2x2의 덮개 하나를 넣는 경우로 2가지 존재.
# 2xN 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.
n = int(input())

d = [0]*1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2 ) % 796796

print(d[n])