'''
# 문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

# 출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.
'''

### 직접구현 ###
def permutation(level):
    global N, choose, check

    # base case
    if level == N:
        print(' '.join(map(str, choose)))
        return

    # recursive case
    for i in range(1, N + 1):
        if check[i] == True:
            continue

        choose.append(i)
        check[i] = True

        permutation(level + 1)

        check[i] = False
        choose.pop()


N = int(input())
choose = []
check = [False] * (N + 1)

permutation(0)

### 라이브러리 ###
from itertools import permutations


N = int(input())

for permutation in permutations(range(1, N + 1)):
    print(' '.join(map(str, permutation)))