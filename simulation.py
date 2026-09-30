import random

'''This is the code for a signle journey across N lily pads. The user can input N.'''
def individual_outcome():
    # remaining_lilypads = int(input("How many lily pads would you like?: "))
    remaining_lilypads = 10
    num_of_jumps = 0

    while (remaining_lilypads != 0):
        jump_distance = random.randint(1, remaining_lilypads)
        # jump_distance = 1
        remaining_lilypads = remaining_lilypads - jump_distance
        num_of_jumps = num_of_jumps + 1
        print("Jump distance: " + str(jump_distance))
        print("Remaining Lilypads: " + str(remaining_lilypads))
        print("Number of jumps: " + str(num_of_jumps))
        print("\n")

    print("Total frog jumps: " + str(num_of_jumps))

individual_outcome()


