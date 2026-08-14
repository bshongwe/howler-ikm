import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    L = int(input_data[idx]); idx += 1
    a = int(input_data[idx]); idx += 1
    b = int(input_data[idx]); idx += 1
    c = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1
    n = int(input_data[idx]); idx += 1
    pos = [int(input_data[idx+i]) for i in range(n)]
    idx += n

    # pos[i] = distance from departure gate (0). Arrival gate is at L.
    # She walks from L down to 0.
    # We simulate walking from L to 0, and at each cart decide whether to buy coffee.
    # State: current position (continuous), whether mid-cooldown or mid-drink.
    # We greedily decide: since throwing away wastes progress, only buy fresh coffee
    # when not already benefiting from a fast-walk window, and it must actually help
    # (i.e., there's enough distance left to make use of the speed boost).

    # Sort carts by position descending (from arrival towards departure)
    order = sorted(range(n), key=lambda i: -pos[i])

    chosen = []
    current_pos = L  # start position
    busy_until_time = 0.0  # not used directly; we track via position and mode
    mode = 'slow'  # current walking mode
    # We'll track the "time-equivalent" position marker for when current effect ends
    # effect_end_pos = position at which current cooldown/drink cycle finishes affecting speed
    effect_end_pos = None  # None means not in a coffee cycle
    cycle_stage = None  # 'cooldown' or 'drink'
    cycle_remaining_time = 0.0

    # Simple greedy: walk cart by cart, tracking elapsed "cycle" via distance,
    # since speed during cooldown = a, and speed during drink = b.
    # We maintain: time_left_in_current_stage, and stage type.
    stage = None  # None, 'cooldown', 'drink'
    stage_time_left = 0.0

    for i in order:
        p = pos[i]
        dist_to_cart = current_pos - p  # positive, since carts sorted descending
        # Simulate walking this distance, consuming current stage first
        remaining_dist = dist_to_cart
        while remaining_dist > 1e-12 and stage is not None:
            speed = a if stage == 'cooldown' else b
            time_for_remaining = remaining_dist / speed
            if time_for_remaining <= stage_time_left + 1e-12:
                # finish this segment within current stage
                stage_time_left -= time_for_remaining
                remaining_dist = 0
                if stage_time_left <= 1e-9:
                    if stage == 'cooldown':
                        stage = 'drink'
                        stage_time_left = d
                    else:
                        stage = None
                        stage_time_left = 0.0
            else:
                # consume entire stage_time_left, move to next stage
                dist_covered = stage_time_left * speed
                remaining_dist -= dist_covered
                if stage == 'cooldown':
                    stage = 'drink'
                    stage_time_left = d
                else:
                    stage = None
                    stage_time_left = 0.0
        current_pos = p

        # Decide whether to buy coffee here: only if not currently in an active stage
        # (buying while cooldown/drink active would waste the remaining benefit)
        if stage is None:
            chosen.append(i)
            stage = 'cooldown'
            stage_time_left = c

    print(len(chosen))
    print(' '.join(map(str, chosen)))

if __name__ == '__main__':
    main()