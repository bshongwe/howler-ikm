# Problem C — KattisFS Defragmenter

## Overview

This program solves the KattisFS disk defragmentation problem. Given a
fragmented disk layout, it reorganizes files so that:

1. Each file is stored **contiguously** on disk (no fragmentation).
2. Files are ordered by **priority**, with the highest-priority file
   placed at the **fastest** part of the disk (the right edge).

## Problem Description

A disk is represented as a grid of characters, where each row corresponds
to a file and each column corresponds to a disk block. A `*` at row `i`,
column `j` means file `i` occupies block `j`; a `.` means it does not.

- The disk is always completely full — every block belongs to exactly
  one file.
- Files are listed in priority order, from highest (first line) to
  lowest (last line).
- Access speed increases toward the right edge of the disk.
- A file may occupy zero blocks (an empty file).

The input may contain multiple disk maps, separated by a blank line.
Input ends at EOF.

## Approach

For each disk map:

1. Determine the disk `width` from the length of the first line.
2. Count each file's required block count by counting the `*` characters
   in its row (`size = line.count('*')`).
3. Rebuild the disk from right to left:
   - Start at the rightmost position (`pos = width`).
   - Place the highest-priority file's blocks immediately to the left of
     `pos`, then move `pos` further left by that file's size.
   - Repeat for each subsequent file in priority order.
4. Print the resulting grid, with files now defragmented and ordered by
   priority (highest priority = rightmost = fastest).

This runs in **O(N × W)** time per disk map, where `N` is the number of
files and `W` is the disk width — simply proportional to the input size.

## Usage


bash
python3 solution.py < input.txt

### Input Format

- One or more disk maps.
- Each map consists of several lines of `*`/`.` characters (one line per
  file, in priority order).
- Disk maps are separated by a single blank line.
- Input ends at EOF (no trailing blank line required after the last map).

### Output Format

- For each disk map, print the defragmented grid, one line per file, in
  the same priority order as the input.
- Print a blank line between consecutive disk maps.
- Do **not** print a trailing blank line after the last map.

## Example

**Input:**


...................
..................
.................
..........**....
..................
...................
.................
....................
..................
```

Output:

...................*
.................**.
..............***...
........******......
......**............
.....*..............
..***...............
....................
**..................

