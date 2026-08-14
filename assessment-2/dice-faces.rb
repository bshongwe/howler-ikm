n, m = gets.split.map(&:to_i)
l = [n, m].min
h = [n, m].max
start = l + 1
end_ = h + 1

(start..end_).each do |total|
  puts total
end