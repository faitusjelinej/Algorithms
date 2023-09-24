# 207. Course Schedule
import collections

def canFinish(n, prerequisites):
    child = collections.defaultdict(list)
    branch = [0]*n
    for i,j in prerequisites:
        child[j].append(i)
        branch[i]+=1
    q = collections.deque()
    for i in range(n):
        if branch[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for i in child[node]:
            branch[i]-=1
            if branch[i]==0:
                q.append(i)
    for i in branch:
        if i!=0:
            return False
    return True


numCourses = 4
prerequisites = [[0,1],[0,2],[1,3]]
print(canFinish(numCourses, prerequisites))
