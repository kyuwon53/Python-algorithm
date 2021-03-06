# 도시 분할 계획
# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
# 길은 어느 방향으로든지 다닐 수 있는 편리한 길이고 길마다 길을 유지하는데 드는 유지비가 있다.
# 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
# 마을을 분할할 때 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
# 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다.
# 불필요한 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.

# 입력
# 집의 개수 N, 길의 개수 M
# 길의 정보 : A, B, C [ A번 집과 B번 집을 연결하는 길의 유지비가 C ]
# 출력 : 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력

# 아이디어: 2개의 최소 신장 트리를 만들어야함 => 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤 => 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거
# 최소 신장 트리를 찾은 뒤에 가장 큰 간선을 제거

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <b :
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0    # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    print('edge',edge)
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

