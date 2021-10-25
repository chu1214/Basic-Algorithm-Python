'''
# 개요
  N개의 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수. 단, 특정한 인덱스에 해당하는 수가 연속해서 K번 더해질 수 없다. 
# 입력 조건
  첫째 줄에 배열의 크기 N(2 <= N <= 1,000), 숫자가 더해지는 횟수 M(1 <= M <= 10,000), 특정한 인덱스 최대 연속 횟수 K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
  둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
  입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 출력 조건 
  첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.
# 시간 제한 1초, 메모리 제한 128MB
'''

'''
# 1차 풀이 >> O(N)
N, M, K = map(int, input().split())) 
data = list(map(int, input().split()))
data.sort(reverse = True)
count = 0
result = 0
for i in range(M):
    if count == K:
        result += data[1]
        count = 0
    else:
        result += data[0]
        count += 1
print(result)

# 정해진 규칙에 따라 수를 더하기 위해 반복문을 사용하였으나, 연산의 규칙성을 찾으면 O(1)로 풀이가 가능했다.
'''

# 2차 풀이 >> O(1)
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse= True)
count = int(M / (K + 1)) * K + M % (K + 1)
result = count * data[0] + (M - count) * data[1]
print(result)