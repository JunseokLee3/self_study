n = input()

k = len(n)
mid = int(k/2)

before = 0
for i in range(mid):
    before += n[i]

after = 0
for i in range(mid, k):
    after += n[i]

if before == after:
    print("LUCKY")
else:
    print("READY")


n = input()
length = len(n)
summary= 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length//2, length):
    summary += int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")