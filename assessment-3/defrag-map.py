import sys

def process_map(lines):
    if not lines:
        return
    width = len(lines[0])
    sizes = [line.count('*') for line in lines]
    
    # Place files from the right (fastest) in priority order
    result = [['.' for _ in range(width)] for _ in lines]
    pos = width  # next free position (from the right)
    
    for i, size in enumerate(sizes):
        if size == 0:
            continue
        pos -= size
        for j in range(pos, pos + size):
            result[i][j] = '*'
    
    for row in result:
        print(''.join(row))

def main():
    maps = []
    current = []
    
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == '':
            if current:
                maps.append(current)
                current = []
        else:
            current.append(line)
    
    if current:
        maps.append(current)
    
    for i, m in enumerate(maps):
        process_map(m)
        if i < len(maps) - 1:
            print()

if __name__ == "__main__":
    main()