n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = m / (k + 1) * k
count += m % (k + 1)

result = 0
result += int(count) * first
result += int(m - count) * second

print(result)

#   n m k
#   5 8 3
#   2 4 5 4 6
#   46