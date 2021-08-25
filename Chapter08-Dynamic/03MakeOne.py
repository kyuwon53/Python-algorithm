# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산
# a. X가 5로 나누어떨어지면, 5로 나눈다.
# b. X가 3으로 나누어떨어지면, 3으로 나눈다.
# c. X가 2로 나누어떨어지면, 2로 나눈다.
# d. X에서 1을 뺀다.
# 정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오
x = int(input())
cnt = [0] * 30001

# 다이나믹 프로그래밍 진행(보텀업)
for i in range(2, x+1):
    # 1을 빼는 경우
    cnt[i] = cnt[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        cnt[i] = min(cnt[i],cnt[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        cnt[i] = min(cnt[i], cnt[i // 5] + 1)

print(cnt[x])