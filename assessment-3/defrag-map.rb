def process_map(lines)
  return if lines.empty?

  width = lines[0].length
  sizes = lines.map { |line| line.count('*') }

  result = Array.new(lines.size) { Array.new(width, '.') }
  pos = width

  sizes.each_with_index do |size, i|
    next if size == 0
    pos -= size
    (pos...pos + size).each do |j|
      result[i][j] = '*'
    end
  end

  result.each { |row| puts row.join }
end

maps = []
current = []

STDIN.each_line do |line|
  line = line.chomp
  if line.empty?
    if !current.empty?
      maps << current
      current = []
    end
  else
    current << line
  end
end

maps << current unless current.empty?

maps.each_with_index do |m, i|
  process_map(m)
  puts if i < maps.size - 1
end