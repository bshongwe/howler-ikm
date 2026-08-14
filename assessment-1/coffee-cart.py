import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx += 1
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    n = int(data[idx]); idx += 1
    dist_from_departure = [int(data[idx+i]) for i in range(n)]
    idx += n

    # Convert to positions measured from arrival gate (0 -> L)
    pos = [L - x for x in dist_from_departure]

    # Sort carts by position ascending, keep original indices
    # ascending positions
    order = sorted(range(n), key=lambda i: pos[i])
    p = [pos[i] for i in order]

    INF = float('inf')

    # S(i) = min time from cart i (just bought coffee at p[i])
    #           to destination L
    # Compute S for all carts, plus handle the "no coffee ever"
    #           / "before first coffee" case.

    # next cart index chosen (in 'order'/'p' indexing), or
    #           None if go straight to L
    S = [0.0] * n
    nxt = [None] * n

    # Process carts from rightmost (closest to L) to leftmost
    # None means go straight to destination after purchase
    for i in range(n - 1, -1, -1):
        pi = p[i]
        p1 = min(pi + a * c, L)
        p2 = min(p1 + b * d, L)

        best_time = INF
        best_next = None

        # Option A: go straight to destination after this purchase
        # time = distance to L (no more coffee)
        # time = c (cooldown, if p1 < L fully realized) + drink time
        #      = c + d (partial or full) + slow walk remainder
        if p1 >= L:
            # cooldown itself doesn't finish before reaching L
            t = (L - pi) / a
        else:
            if p2 >= L:
                # drink doesn't finish before reaching L
                t = c + (L - p1) / b
            else:
                # full cooldown + full drink + remaining slow walk to L
                t = c + d + (L - p2) / a
        if t < best_time:
            best_time = t
            best_next = None

        # Option B: rightmost cart with position <= p1
        # (p[i] <= pi, (still in cooldown), position > pi
        # search in p[i+1 .. n-1] for largest value <= p1
        hi_idx = bisect_right(p, p1, i + 1, n) - 1
        if hi_idx >= i + 1:
            j = hi_idx
            # time to reach cart j: entirely within cooldown
            # (p[j] - pi) / a = time in cooldown phase (speed a)
            t = (p[j] - pi) / a + S[j]
            if t < best_time:
                best_time = t
                best_next = j

        # Option C: rightmost cart with position in (p1, p2) i.e.,
        # position > p1 and < p2 during drink phase
        lo_idx = bisect_right(p, p1, i + 1, n)
        hi_idx2 = bisect_left(p, p2, i + 1, n) - 1
        if lo_idx <= hi_idx2:
            j = hi_idx2
            # time to reach cart j:
            #       full cooldown (c) + partial drink
            t = c + (p[j] - p1) / b + S[j]
            if t < best_time:
                best_time = t
                best_next = j

        # Option D: leftmost cart with position >= p2
        # (after drink fully finishes)
        lo_idx2 = bisect_left(p, p2, i + 1, n)
        if lo_idx2 <= n - 1:
            j = lo_idx2
            # time: full cooldown + full drink + slow walk
            # from p2 to p[j]
            t = c + d + (p[j] - p2) / a + S[j]
            if t < best_time:
                best_time = t
                best_next = j

        S[i] = best_time
        nxt[i] = best_next

    # Now handle the very start: from position 0 (arrival gate), before any coffee.
    # We consider: go straight to destination without any coffee,
    # or walk to some cart i and buy coffee there (only carts with p[i] reachable,
    # i.e. all of them, since p is increasing and >=0)
    # Candidates: leftmost cart overall (to start coffee ASAP), OR direct to
    # destination

    best_total = (L - 0) / a  # no coffee at all
    best_start = None

    if n > 0:
        # starting fresh, we may walk to any cart, but only the very first cart
        # is ever optimal as a "first purchase" candidate, since walking further
        #   first (without benefit) is wasteful(leftmost) 
        # is ever optimal as a "first purchase" candidate, since walking further
        #   first (without benefit) is wasteful
        j = 0
        t = (p[j] - 0) / a + S[j]
        if t < best_total:
            best_total = t
            best_start = j

    # Reconstruct path
    result = []
    if best_start is not None:
        i = best_start
        while i is not None:
            result.append(order[i])
            i = nxt[i]

    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()