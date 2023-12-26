import sys
from icecream import ic
from collections import Counter, defaultdict

with open(f"2023/7/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]


card_ranking = {
    "A": 14, 
    "K": 13, 
    "Q": 12, 
    "J": 11,
    "T": 10
}

def get_card_rank(card):
    if card in card_ranking:
        return card_ranking[card]

    return int(card)

def get_hand_raw_rank(hand):
    return [get_card_rank(c) for c in list(hand)]

def get_hand_rank(hand):
    card_counts = Counter(hand)
    most_common = card_counts.most_common(2)

    if most_common[0][1] >= 4: # five/four of a kind
        return most_common[0][1]+1 # 5/6

    if most_common[0][1] == 3:
        if most_common[1][1] == 2: # full house
            return 4
        
        return 3 # three of a kind

    if most_common[0][1] == 2:
        if most_common[1][1] == 2: # 2 pairs
            return 2
        
        return 1
    
    return 0

def settle_ties(hands):
    ranked_hands = []
    char_ix = 0
    hand_values = []
    for hand in hands:
        hand_values.append((hand, get_hand_raw_rank(hand)))

    hv_sorted = sorted(hand_values, key=lambda k: k[1], reverse=True)

    return [hv[0] for hv in hv_sorted]


hand_bids = {}
for line in lines:
    hand, bid = line.strip().split(" ")
    hand_bids[hand] = int(bid)

hand_ranks = defaultdict(list)
for hand, bid in hand_bids.items():
    hand_ranks[get_hand_rank(hand)].append(hand)
    #input(f"{hand=} ranked as {get_hand_rank(hand)}")

final_ranking = []
for i, ranking in enumerate(sorted(hand_ranks.keys())):
    _hands = hand_ranks[ranking]
    if len(hand_bids) == 1:
        final_ranking.append(_hands[0])
        continue
    
    ranked_hands = settle_ties(_hands)
    final_ranking = ranked_hands + final_ranking
    
print(final_ranking[:10])
score = 0
for i, hand in enumerate(final_ranking[::-1]):
    #input(f"hand: {hand}, hb: {hand_bids[hand]}")
    score += ((i+1) * hand_bids[hand])

print(score, file=sys.stderr)
