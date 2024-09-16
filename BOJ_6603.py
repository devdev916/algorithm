'''
# 문제
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.
예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])
집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

# 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.
입력의 마지막 줄에는 0이 하나 주어진다. 

# 출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.
각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.
'''

### 직접구현 ###
def combination(index, level):
	global choose, arr, k

	# base case
	if level == 6:
		for u in choose:
			print(u, end=' ')
		print()
		return

	# recursive case
	for i in range(index, k):
		choose.append(arr[i])
		combination(i + 1, level + 1)
		choose.pop()


while True:
	choose = []
	I = list(map(int, input().split())) 
	# input 1 line 문자열로 받아 공백 기준으로 나누어 리스트로 바꾼 후
	# 리스트 원소를 int type 바꿔 map object로 반환한걸 list 자료형으로 만듦

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	combination(0, 0)
	print()

### 라이브러리 ###
from itertools import combinations

while True:
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	for combination in combinations(arr, 6): # combinations(배열, 갯수)
		for ele in combination:
			print(ele, end=' ')
		print()
	print() 
