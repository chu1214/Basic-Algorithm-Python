'''
# 개요
  정해진 룰을 지키며 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
  * 룰
    1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
    2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
    3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
    4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
# 입력 조건
  첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다(1 <= N, M <= 100)
  둘때 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다
# 출력 조건 
  첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
# 시간 제한 1초, 메모리 제한 128MB
'''

'''
# 1차 풀이 >> O(NlogN)
N, M = map(int, input().split())
minList = []
for i in range(N):
    card = list(map(int, input().split()))
    num = min(card)
    minList.append(num)
minList.sort(reverse=True)
print(minList[0])

# 각 행의 최소값 중 최대값을 구한다는 생각에 각 행의 값을 모두 저장하는 리스트를 만들고 정렬을 하였는데, 각 행이 입력될 때마다 최대값을 갱신해주면 소요시간을 단축시킬 수 있었다.
'''

# 2차 풀이 >> O(N)

N, M = map(int, input().split())
result = 0
for i in range(N):
    card = list(map(int, input().split()))
    min_value = min(card)
    result = max(result, min_value)
print(result)