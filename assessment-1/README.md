# Problem Analysis
Jonna walks from position L (arrival gate) to 0 (departure gate). She walks slow at speed a,
but when drinking coffee walks at speed b > a. Buying coffee at a cart: she keeps walking
slow for c seconds (cooldown), then walks fast for d seconds (drinking), then reverts to slow.

##Key Insight
The total distance is fixed. The total time = (time spent walking slow) + (time spent walking
fast). Since fast distance is covered at speed b and slow distance at speed a, and total
distance is fixed, minimizing time is equivalent to maximizing the total distance covered
while walking fast (since that's the more efficient speed).

Each coffee purchase gives a fixed fast-walking duration of d seconds, contributing b*d
centimeters of "fast progress" — but only if there's enough remaining distance to actually
walk that far, and purchases can't overlap wastefully.

Since buying a new coffee cancels the effect of the previous one immediately (she throws it
away), the only thing that matters is: at each cart she uses, does she get a fresh full d
seconds of fast walking (as long as she doesn't run out of road, and cart positions don't
force overlaps in a way that wastes drinking time).

Since throwing away and rebuying is allowed, buying coffee at multiple carts spaced closely
is never beneficial (it wastes the d seconds already accrued). So the optimal strategy is to
choose a subset of carts, spaced far enough apart, to maximize total fast-walking distance,
which is min(d, time until next chosen purchase or destination) * b for each purchase -
essentially each purchase should be allowed to run its full d seconds before the next one
starts.

This becomes a greedy / DP problem: choose carts to buy coffee at, such that consecutive
purchases are spaced enough that each coffee's d-second fast window isn't cut short by the
next purchase's cooldown, maximizing total distance covered at speed b.

My Approach (Greedy simulation)
A common accepted strategy for this exact Kattis problem (airportcoffee) is:

	1. Process carts from the arrival gate towards departure gate (i.e., in order of
    decreasing distance from departure, meaning simulate from position L down to 0).
	2. Maintain current position and whether currently "busy" with a coffee cycle
    (cooldown+drink).
	3. Greedily buy coffee whenever possible, as long as buying at this cart does not waste
    time compared to not buying (i.e., only buy if you're currently in "slow" mode and the
    cart is not within an already active drink period).

Since coding the full solution requires careful simulation and DP, here is a Python solution
that implements a DP over cart positions, computing maximum "fast distance" achievable