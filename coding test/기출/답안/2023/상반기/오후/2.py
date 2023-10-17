## 이거는 선택적 포기

from sortedcontainers import SortedSet, SortedDict
import heapq
import sys

class PriorityQueue:
    def __init__(self):          # 빈 Priority Queue 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, item)
                
    def empty(self):             # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
            
        return heapq.heappop(self.items)
                
    def top(self):               # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
                        
        return self.items[0]

MAX_D = 300
MAX_N = 50000
INF = sys.maxsize

# 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리해줍니다.
is_in_readyq = [SortedSet() for _ in range(MAX_D + 1)]

# 현재 쉬고 있는 채점기들을 관리해줍니다.
rest_judger = PriorityQueue()

# 각 채점기들이 채점할 때, 도메인의 인덱스를 저장합니다.
judging_domain = [0 for _ in range(MAX_N + 1)]

# 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리합니다.
s = [0 for _ in range(MAX_D + 1)]
g = [0 for _ in range(MAX_D + 1)]
e = [0 for _ in range(MAX_D + 1)]

# 도메인을 관리하기 위해 cnt를 이용합니다.
# 도메인 문자열을 int로 변환해주는 map을 관리합니다.
domainToIdx = SortedDict()
global cnt
cnt = 0

# 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
global ans
ans = 0

# 각 도메인별로 priority queue를 만들어
# 우선순위가 가장 높은 url을 뽑아줍니다.
url_pq = [PriorityQueue() for _ in range(MAX_D + 1)]


# 채점기를 준비합니다.
def Init(query):
    global n
    (empty, n, url) = query
    n = int(n)

    global cnt

    for i in range(1, n + 1): rest_judger.push(i)

    # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
    idx = 0
    for i in range(len(url)):
        if url[i] == '/': idx = i

    domain = url[:idx]
    num = int(url[idx + 1:])

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
    is_in_readyq[domain_idx].add(num)

    # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
    # id, tme, num
    newUrl = (1, 0, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
    global ans
    ans += 1


# 새로운 url을 입력받아 레디큐에 추가해줍니다.
def NewUrl(query):
    (empty, tme, id, url) = query
    tme = int(tme)
    id = int(id)

    global cnt

    # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
    idx = 0
    for i in range(len(url)):
        if url[i] == '/':
            idx = i

    domain = url[:idx]
    num = int(url[idx + 1:])

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
    if domain not in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt

    domain_idx = domainToIdx[domain]

    # 만약 숫자 부분이 이미 레디큐에 있으면 중복되므로 넘어갑니다.
    if num in is_in_readyq[domain_idx]:
        return
    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
    is_in_readyq[domain_idx].add(num)

    # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
    # id, tme, num
    newUrl = (id, tme, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
    global ans
    ans += 1


# 다음 도메인을 찾아 assign합니다.
def Assign(query):
    (empty, tme) = query
    tme = int(tme)

    # 쉬고 있는 채점기가 없다면 넘어갑니다.
    if rest_judger.empty(): return

    # 가장 우선순위가 높은 url을 찾습니다.
    min_domain = 0
    minUrl = (INF, 0, 0)

    global cnt

    for i in range(1, cnt + 1):
        # 만약 현재 채점중이거나, 현재 시간에 이용할 수 없다면 넘어갑니다.
        if e[i] > tme: continue

        # 만약 i번 도메인에 해당하는 url이 존재한다면
        # 해당 도메인에서 가장 우선순위가 높은 url을 뽑고 갱신해줍니다.
        if not url_pq[i].empty():
            curUrl = url_pq[i].top()

            if minUrl > curUrl:
                minUrl = curUrl
                min_domain = i

    # 만약 가장 우선순위가 높은 url이 존재하면
    # 해당 도메인과 쉬고 있는 가장 낮은 번호의 채점기를 연결해줍니다.
    if min_domain:
        judger_idx = rest_judger.top()
        rest_judger.pop()

        # 해당 도메인의 가장 우선순위가 높은 url을 지웁니다.
        url_pq[min_domain].pop()

        # 도메인의 start, end를 갱신해줍니다.
        s[min_domain] = tme
        e[min_domain] = INF

        # judger_idx번 채점기가 채점하고 있는 도메인 번호를 갱신해줍니다.
        judging_domain[judger_idx] = min_domain

        # 레디큐에서 해당 url의 숫자를 지워줍니다.
        is_in_readyq[min_domain].remove(minUrl[2])

        # 채점 대기 큐에 값이 지워졌으므로 개수를 1 감소합니다.
        global ans
        ans -= 1


# 채점 하나를 마무리합니다.
def Finish(query):
    (empty, tme, id) = query
    tme = int(tme)
    id = int(id)

    # 만약 id번 채점기가 채점 중이 아닐 경우 스킵합니다.
    if judging_domain[id] == 0: return

    # id번 채점기를 마무리합니다.
    rest_judger.push(id)
    domain_idx = judging_domain[id]
    judging_domain[id] = 0

    # 해당 도메인의 gap, end 값을 갱신해줍니다.
    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]


# 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
def Check(query):
    (empty, tme) = query
    tme = int(tme)

    global ans
    print(ans)


q = int(input())

for _ in range(q):
    query = input().split()

    if int(query[0]) == 100:
        # 채점기를 준비합니다.
        Init(query)
    if int(query[0]) == 200:
        # 새로운 url을 입력받아 레디큐에 추가해줍니다.
        NewUrl(query)
    if int(query[0]) == 300:
        # 다음 도메인을 찾아 assign합니다.
        Assign(query)
    if int(query[0]) == 400:
        # 채점 하나를 마무리합니다.
        Finish(query)
    if int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
        Check(query)