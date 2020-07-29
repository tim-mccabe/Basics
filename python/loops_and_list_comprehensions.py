# This file contains a few basic functions of lists and loops to refer back to when writing new code

# Return whether the given list of numbers is lucky. A lucky list contains
# at least one number divisible by 7.

def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

# another way of writing the same functions with a bit less code
# def has_lucky_number(nums):
#     for num in nums:
#         if num % 7 == 0:
#             return True
#     return False

# Return a list with the same length as L, where the value at index i is 
# True if L[i] is greater than thresh, and False otherwise.
    
# >>> elementwise_greater_than([1, 2, 3, 4], 2)
# [False, False, True, True]


def elementwise_greater_than(L, thresh):
    res = []
    for num in L:
        res.append(num > thresh)
    return res

# Run the slot machine n_runs times and return the average net profit per run.
# Example calls (note that return value is nondeterministic!):
# >>> estimate_average_slot_payout(1)
# -1
# >>> estimate_average_slot_payout(1)
# 0.5

# play_slot_machine()#built in function from kaggle to get results from a slot machine

def estimate_average_slot_payout(n_runs):
    winnings = []
    for i in range(n_runs):
        winnings.append(play_slot_machine()-1)
    avg_winnings = sum(winnings)/len(winnings)
    return avg_winnings
estimate_average_slot_payout(1000)

