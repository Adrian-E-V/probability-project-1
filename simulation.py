import random
import matplotlib.pyplot as plt

'''This is the code for a signle journey across N lily pads.'''
def individual_outcome(n: int) -> int:
    remaining_lilypads = n
    num_of_jumps = 0
    while (remaining_lilypads != 0):
        jump_distance = random.randint(1, remaining_lilypads)
        # jump_distance = 1
        remaining_lilypads = remaining_lilypads - jump_distance
        num_of_jumps = num_of_jumps + 1
        # print("Jump distance: " + str(jump_distance))
        # print("Remaining Lilypads: " + str(remaining_lilypads))
        # print("Number of jumps: " + str(num_of_jumps))
        # print("\n")
    return num_of_jumps


#2a) When N=10, what is the probability that it takes exactly three jumps? 
# we can find this by taking a large amount of individual outcomes, and choosing the ones that resulted in exactly 3 jumps.
large_amount_of_trials = 1000000

trials_with_3_jumps = 0
for _ in range(0, large_amount_of_trials):
    if individual_outcome(10) == 3:
        trials_with_3_jumps += 1
probability_of_3_jumps = trials_with_3_jumps / large_amount_of_trials
print(f"P[X=3] when N=10: {probability_of_3_jumps}")

#2b) When N=8, estimate the full PMF of the number 𝑋 of jumps. In other words, what are all the possible values of 𝑋, and what are all the corresponding probabilities? Your answer should be a table of values.
# we recorded the outcomes of a large numbers of trials and count the numbers of occurrence of each
outcomes = []
for _ in range(0, large_amount_of_trials):
    outcomes.append(individual_outcome(8))
print(f"{'X':<10} {'Estimated probability'}")
for x in range(1, 9):
    estimated_probability = outcomes.count(x) / large_amount_of_trials
    print(f"{x:<10} {estimated_probability}")
print(f"{'Otherwise':<10} {0}")


# 2c) When N=20, what is the expected number of jumps?
# Note: we use 21 instead of 20 for easier indexing. 20 provides indicies 0 -> 19; we'd be excluding the (rare) case when X = 20.
jump_frequency = [0] * 21
for _ in range(0, large_amount_of_trials):
    jump_frequency[individual_outcome(20)] += 1
total_jumps = 0
for i in range(1, 21):
    total_jumps += jump_frequency[i]*i
expected_value = total_jumps / large_amount_of_trials
print(f"E[X] when N=20: {expected_value}")

# 2d) How does this expected value change as N increases?
# we estimate E[X] for N from 1 to 100 to see the trend as N increases
expected_values = []
for n in range(1, 101):
    total_jumps = 0
    for _ in range(large_amount_of_trials):
        total_jumps += individual_outcome(n)
    expected_values.append(total_jumps / large_amount_of_trials)
print(f"{'N':<10} {'Estimated E[X]'}")
for n, expected_value in enumerate(expected_values, start=1):
    print(f"{n:<10} {expected_value}")
plt.plot(range(1, 101), expected_values)
plt.xlabel("N")
plt.ylabel("Estimated E[X]")
plt.title("Number of landing spot vs Expected number of jumps")
plt.grid(True)
plt.show()