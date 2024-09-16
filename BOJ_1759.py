'''
# 문제
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다.
이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다.
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# 출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
'''

# .sort() 함수는 파이썬 리스트 클래스의 매소드로, 리스트 자료형에서만 사용 가능하다.
# sorted() 함수는 파이썬의 내장 함수로 iterable(순서가 존재하는) 객체에 대해 모두 사용 가능하다.

### 직접구현 ###
vows = ['a', 'e', 'i', 'o', 'u']
choose = []


def is_possible():
	global L, C, choose, arr

	vow = 0
	for c in choose:
		vow += (c in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)

def combination(idx, lev):
	global L, C, choose, arr

	# base case
	if lev == L:
		if is_possible():
			print(''.join(choose))
		return

	# recursive case
	for i in range(idx, C):
		choose.append(arr[i])
		combination(i + 1, lev + 1)
		choose.pop()


L, C = map(int, input().split())
arr = input().split()

arr.sort()

combination(0, 0)

### 라이브러리 ###
from itertools import combinations


vows = ['a', 'e', 'i', 'o', 'u']


def is_possible(word):
	global L, C, arr

	vow = 0
	for w in word:
		vow += (w in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)


L, C = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, L):
	if is_possible(word):
		print(''.join(word))