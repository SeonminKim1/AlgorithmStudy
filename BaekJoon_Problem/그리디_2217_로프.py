# BaekJoon 2217번 로프

# N(1≤N≤100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.
# 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
# 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는
# 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며,
# 임의로 몇 개의 로프를 골라서 사용해도 된다.

# 입출력 링크 : https://www.acmicpc.net/problem/2217

# 문제이해
# 예시
# 200 30 80 75 170
# (1) 내림차순으로 바꾼다. (바꾸는 이유는 젤 좋은 것부터 쓰는 것)
# (2) 200 170 80 75 30
# (3) 로프가 1개일때는 200밖에 못버팀
# (4) 로프가 2개일때는 200 170 -> 작은놈기준 170x2 -> 340 버팀
# (5) 로프가 3개일때는 200 170 80 -> 작은놈기준 80x3 -> 240 버팀
# (6) 로프가 4개일떄는 200 170 80 75 -> 작은놈 기준 75x4 -> 300 버팀
# (7) 로프가 5개일때는 200 170 80 75 30 -> 작은놈기준 30x5 -> 150 버팀
# (8) 여기서 곱해주는 숫자는 그 로프가 5개 있단 뜻이 아니라 최대 로프가 버틸수 있는
# 중량이 200이더라도 다 같은 중량을 책임저야 하고 30밖에 못쓰니까

import sys
N = int(sys.stdin.readline().strip())

ls = []
for _ in range(N):
    m = int(sys.stdin.readline().strip())
    ls.append(m)

# 내림차순으로 바꾸는건
ls.sort(reverse=True)

max_weight = 0
for i in range(len(ls)):
    temp_max = ls[i] * (i + 1)
    if temp_max > max_weight:
        max_weight = temp_max

print(max_weight)
