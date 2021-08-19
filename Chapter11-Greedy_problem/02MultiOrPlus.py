# 곱하기 혹은 더하기
# 각 자리가 숫자 (0~9)로만 이루어진 문자열 s가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+'연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
# 단, + 보다 X를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정.

# 아이디어: 1이하는 더하기, 그 외는 곱하기
s = input()
result = int(s[0])
for i in range(1,len(s)):
    if result <= 1 or int(s[i]) <= 1:
        result += int(s[i])
    else:
        result *= int(s[i])
print(result)
