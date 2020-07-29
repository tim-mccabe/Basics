# This file contains a few basic functions of external libraries to refer back to when writing new code

# Given a list of racer dictionaries, return a dictionary mapping items to the number
# of times those items were picked up by racers who finished in first place.

def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
best_items(sample)

# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for x in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if x not in winner_item_counts:
                    winner_item_counts[x] = 0
                winner_item_counts[x] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)

# Return True if hand_1 beats hand_2, and False otherwise.

# In order for hand_1 to beat hand_2 the following must be true:
# - The total of hand_1 must not exceed 21
# - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

# Hands are represented as a list of cards. Each card is represented by a string.

# When adding up a hand's total, cards with numbers count for that many points. Face
# cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

# When determining a hand's total, you should try to count aces in the way that 
# maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
# the total of ['A', 'A', '9', '3'] is 14.

# Examples:
# >>> blackjack_hand_greater_than(['K'], ['3', '4'])
# True
# >>> blackjack_hand_greater_than(['K'], ['10'])
# False
# >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
# False

def hand_total(hand):
# Helper function to calculate the total points of a blackjack hand.

    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total
    
def blackjack_hand_greater_than(hand_1, hand_2):

    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)