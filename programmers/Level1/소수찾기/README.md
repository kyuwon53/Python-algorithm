# 🔔 프로그래머스 - Level 1
## 📑 소수찾기
### 📌 문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

### ✔️ 제한 사항
- n은 2이상 1000000이하의 자연수입니다.


### 💡 아이디어
- 2부터 자기자신까지 나눠서 나누어떨어지는 수가 있으면 그 즉시 return 

### 💬 개선사항
- 효율성과 시간복잡도 개선 
- 에라토스테네스의 체라는 알고리즘을 활용
```python
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
```

### 👉 문제 출처: [소수찾기](https://programmers.co.kr/learn/courses/30/lessons/12921)


