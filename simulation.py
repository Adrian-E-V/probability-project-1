import random

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
large_amount_of_trials = 100000
trials_with_3_jumps = 0
for _ in range(0, large_amount_of_trials):
    if individual_outcome(10) == 3:
        trials_with_3_jumps += 1
print(trials_with_3_jumps)
