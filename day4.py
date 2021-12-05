import numpy as np

# ---- LOAD DATA ----
draws = np.genfromtxt('data/day4_draws.txt', dtype=int, delimiter=',')
card_data = np.genfromtxt('data/day4_cards.txt', dtype=int)
card_rows, card_cols = card_data.shape
num_cards = int(card_rows / card_cols)
cards_split = np.split(card_data, num_cards)
winners_eligible = np.full(num_cards, 1, dtype=np.int)

# Checks whether a card is a winner
def check_is_winner(c):
    cols = np.max(np.sum(c == -1, axis=0))
    rows = np.max(np.sum(c == -1, axis=1))
    if max(rows, cols) >= card_cols:
        return 1
    else:
        return 0

# Calls a single bingo number and looks for winning cards
def call_number(n):
    card_data[card_data == n] = -1
    winners_total = np.fromiter(map(check_is_winner, cards_split), dtype=np.int)
    winners_new = np.multiply(winners_total, winners_eligible)
    winners_eligible[np.where(winners_new==1)] = 0
    winners_new_indices = np.argwhere(winners_new == 1)
    if len(winners_new_indices) > 0:
        winner_index = winners_new_indices[0][0]
        winner_card = cards_split[winner_index]
        unmarked = np.where(winner_card > -1 ,winner_card,0)
        return(np.sum(unmarked) * n)
    return(0)

# ---- MAIN ITERATOR ----
result = np.fromiter(map(call_number, draws), dtype=np.int)
print('Part One Answer:', result[np.where(result > 0)[0][0]])
print('Part Two Answer:', result[np.where(result > 0)[0][-1]])
