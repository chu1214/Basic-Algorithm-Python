'''
# 삽입 정렬(Insertion Sort)
  데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
  특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
  두 번째 데이터부터 시작(첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문)
  시간 복잡도 >> 최악: O(N^2), 최선: O(N), 데이터가 거의 정렬되어있는 경우에는 퀵 정렬보다도 효율적이다.
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)