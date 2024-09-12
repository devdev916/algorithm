'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

### 재귀함수 ###
def fibonacci(n):
	global cnt
	cnt += 1

	# base case
	if n == 0:
		return 0
	if n == 1:
		return 1

	# recursuve case
	return fibonacci(n-1) + fibonacci(n-2)

cnt = 0
n = int(input())
print(fibonacci(n))
print(cnt)

### 반복문 ###
n = int(input())
arr = [-1] * (n+2) # 배열 크기 확장 및 초기화
arr[0] = 0
arr[1] = 1

for i in range(2, n+1):
	arr[i] = arr[i-1] + arr[i-2]
print(arr[n])

### 재귀함수 + 메모이제이션 ###
def fibonacci(n):
	global arr, cnt
	cnt += 1

	# base case
	if arr[n] != -1:
		return arr[n]

	# recursuve case
	arr[n] = fibonacci(n-1) + fibonacci(n-2)
	return arr[n]

cnt = 0
n = int(input())
arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

print(fibonacci(n))
print(cnt)
