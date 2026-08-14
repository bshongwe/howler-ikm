# Programming Challenges Solutions

Solutions to a set of algorithmic programming challenges (Kattis / NCPC style).

Each problem lives in its own subdirectory and contains implementations in **Python** and **Ruby**.

---

## Problem A – Airport Coffee

**What it asks**  
Jonna must walk a long distance `L` through an airport.  
She walks slowly by default, but buying coffee lets her walk faster for a limited time (after a short cool-down).  
Coffee carts are scattered along the path. She can carry only one cup at a time and may throw unfinished coffee away.

Decide which carts she should buy from so she reaches the departure gate as quickly as possible.

**Solution**  
Dynamic programming from the end of the corridor backwards.  
For every cart we only need to examine three candidate “next” carts (found with binary search):
1. the furthest cart still reachable during cool-down,
2. the furthest cart reachable while drinking,
3. the nearest cart after the coffee is finished.

This yields an optimal set of purchases in \(O(n \log n)\) time.

---

## Problem B – Most Likely Dice Sums

**What it asks**  
Given two dice with `N` and `M` faces (faces numbered 1…N and 1…M), output the sum(s) that occur most frequently.  
If several sums share the highest probability, list them in ascending order (one per line).

**Key insight**  
The distribution of sums forms a trapezoid. The flat maximum runs exactly from `min(N,M)+1` to `max(N,M)+1`.

**Solution**  
Simply print every integer in that inclusive range.

---

## Problem C – Disk Defragmentation

**What it asks**  
You receive one or more disk maps (grids of `.` and `*`).  
Each row is a file (highest priority first).  
The disk is completely full.  

Re-arrange the data so that:
- every file becomes a single contiguous block of `*`s, and
- higher-priority files sit as far to the **right** as possible (the fastest part of the disk).

Print the new layout for each map, with a blank line between maps.

**Solution**  
Count the number of blocks each file needs, then pack the files from the right in priority order.

---

## Running the solutions

Each subdirectory contains both a Python and a Ruby implementation.

```bash
# Example
cd dice-sums
python3 solution.py < sample.in
ruby solution.rb < sample.in
```

---

## Notes

- Positions in Airport Coffee are measured from the arrival gate (start = 0), matching the official samples and figure.
- All solutions are accepted by the respective judges (absolute/relative error tolerance of \(10^{-9}\) is respected for the floating-point problem).