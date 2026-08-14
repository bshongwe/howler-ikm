def bisect_left(arr, x, lo = 0, hi = arr.size)
  while lo < hi
    mid = (lo + hi) / 2
    if arr[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

def bisect_right(arr, x, lo = 0, hi = arr.size)
  while lo < hi
    mid = (lo + hi) / 2
    if arr[mid] <= x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

data = STDIN.read.split.map(&:to_i)
L, a, b, t, r, n = data[0, 6]
pos = data[6, n]

pos << L
n += 1
idx = (0...n-1).to_a + [-1]

S = Array.new(n, 0.0)
nxt = Array.new(n, -1)

(n-2).downto(0) do |i|
  pi = pos[i]
  p1 = [pi + a * t, L].min
  p2 = [p1 + b * r, L].min

  best = Float::INFINITY
  best_j = -1

  # go straight to destination
  if p1 >= L
    cur = (L - pi).to_f / a
  elsif p2 >= L
    cur = t + (L - p1).to_f / b
  else
    cur = t + r + (L - p2).to_f / a
  end
  if cur < best
    best = cur
    best_j = n - 1
  end

  # right-most cart still in cool-down
  j = bisect_right(pos, p1, i + 1, n) - 1
  if j > i
    cur = (pos[j] - pi).to_f / a + S[j]
    if cur < best
      best = cur
      best_j = j
    end
  end

  # right-most cart inside drinking phase
  lo = bisect_right(pos, p1, i + 1, n)
  hi = bisect_left(pos, p2, i + 1, n) - 1
  if lo <= hi
    j = hi
    cur = t + (pos[j] - p1).to_f / b + S[j]
    if cur < best
      best = cur
      best_j = j
    end
  end

  # left-most cart after drinking finishes
  j = bisect_left(pos, p2, i + 1, n)
  if j < n
    cur = t + r + (pos[j] - p2).to_f / a + S[j]
    if cur < best
      best = cur
      best_j = j
    end
  end

  S[i] = best
  nxt[i] = best_j
end

# start from position 0
best_total = L.to_f / a
start = -1

(0...n-1).each do |i|
  cur = pos[i].to_f / a + S[i]
  if cur < best_total - 1e-12
    best_total = cur
    start = i
  end
end

ans = []
i = start
while i != -1 && i != n - 1
  ans << idx[i]
  i = nxt[i]
end

puts ans.size
puts ans.join(' ') unless ans.empty?