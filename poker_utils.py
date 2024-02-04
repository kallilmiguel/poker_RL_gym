import numpy as np

ORDER = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    '10': 8,
    'Jack': 9,
    'Queen': 10,
    'King': 11,
    'Ace': 12
}

def evaluate_hand(cards):
    """
    Evaluate the given hand of cards and return its rank and the best hand.
    cards: A list of tuples, each representing a card as (rank, suit)
    """
    if is_royal_flush(cards):
        return (10, "Royal Flush")
    elif is_straight_flush(cards):
        return (9, "Straight Flush")
    elif is_four_of_a_kind(cards):
        return (8, "Four of a Kind")
    elif is_full_house(cards):
        return (7, "Full House")
    elif is_flush(cards):
        return (6, "Flush")
    elif is_straight(cards):
        return (5, "Straight")
    elif is_three_of_a_kind(cards):
        return (4, "Three of a Kind")
    elif is_two_pair(cards):
        return (3, "Two Pair")
    elif is_one_pair(cards):
        return (2, "One Pair")
    else:
        return (1, "High Card", high_card(cards))
    
def is_royal_flush(cards):
    pass

def is_straight_flush(cards):
    pass

def is_four_of_a_kind(cards):
    pass

def is_full_house(cards):
    pass

def is_flush(cards):
    pass

def is_straight(cards):
    pass

def is_three_of_a_kind(cards):
    pass

def is_two_pair(cards):
    pass

def is_one_pair(cards):
    pass

def high_card(cards):
    pass