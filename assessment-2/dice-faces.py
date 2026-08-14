n, m = map(int, input().split())

lo = min(n, m)
hi = max(n, m)

# Most likely sums range from lo+1 to hi+1
start = lo + 1
end = hi + 1

for total in range(start, end + 1):
    print(total)