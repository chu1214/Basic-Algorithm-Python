'''
# 개요
  N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
  구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
  이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 
# 입력 조건
  첫 번째 줄에 얼음 틀의 세로길이 N과 가로 길이 M이 주어진다.(1 <= N, M <= 1,000)
  두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
  이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 출력 조건 
  한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
# 시간 제한 1초, 메모리 제한 128MB
'''

# 1차 풀이

# N, M 입력 받기
N, M = map(int, input().split())

# 얼음 틀 입력 받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split)))

# DFS 함수 정의
def dfs(x, y):
# 범위를 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
# graph[x][y]에 방문한 적이 없는 경우
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
# graph[x][y]에 방문한 적이 있는 경우
    return False

# 아이스크림의 개수
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)

'''
# DFS를 활용하여 구현하였다
  서로 연결되어있는 영역 내부를 탐색하여 그 영역을 모두 방문 처리를 하고, 결과값에 1을 더해주려고 생각했다.
  이 과정에서 네 방향을 고려해야 하므로 코드의 간결성 등을 생각하였을 때 DFS가 효율적일 것으로 판단하였다.
  다만 이전 예제들과 달리 graph 리스트 내에 다른 노드와의 관계 등의 정보가 포함되어 있지 않았다.
  따라서 visited 리스트를 만들지 않고도, 방문하고 난 graph 리스트의 정보를 방문할 수 없는 조건으로 변경해주면 메모리를 절약할 수 있었다.
  이 부분에 대해서 코드 작성 중 깨닫고 수정하였다. 코드 작성 전에 해당 변수가 필요성에 대해 확인을 잘 해주어야 겠다.
'''