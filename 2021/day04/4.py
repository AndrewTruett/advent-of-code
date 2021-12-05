import os
import re
sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    data = file.readlines()


def create_bingo_cell(num):
    return [num, False]

def print_2d_list(list_2d):
    for r in list_2d:
        for c in r:
            print(c, end = " ")
        print()

def get_value(cell):
    return cell[0]

def is_marked(cell):
    return cell[1]

def mark_card(card, val):
    for r in range(len(card)):
        for c in range(len(card[r])):
            if card[r][c][0] == val:
                card[r][c][1] = True
    return card

def get_marked_card(card):
    marked_values = []
    for r in card:
        new_row = []
        for c in r:
            new_row.append(card[r][c][1])
        marked_values.append(new_row)
    return marked_values

def is_winner(card):

    def is_winner_rows(card):
        # check rows
        for r in card:
            result_so_far = True
            for c in r:
                result_so_far = result_so_far and c[1]
            
            if result_so_far:
                return True
    
    return is_winner_rows(card) or is_winner_rows(transpose(card))

def sum_unmarked_cells(card):
    sum = 0
    for r in card:
        for c in r:
            if not c[1]:
                sum += c[0]

    return sum

def transpose(matrix):
    return zip(*matrix)            

def get_first_winning_card(cards, numbers):
    for draw in numbers:
        for card in cards:
            card = mark_card(card, draw)
            if is_winner(card):
                return card, draw


numbers = [int(num.strip()) for num in data[0].split(",")]

# Remove the numbers
data.remove(data[0])

# Remove newline elements
data = list(filter(("\n").__ne__, data))

cards = []
current_card = []
curr_row = 1
CARD_ROWS = 5
for line in data:

    patterns = [r"^ ", r"\n"]
    combined_pat = r"|".join(patterns)
    line = re.sub(combined_pat, '', line).replace("  ", " ")
            
    row_nums = [int(num.strip()) for num in line.split(" ")]
    current_card.append([create_bingo_cell(num) for num in row_nums])

    if curr_row >= CARD_ROWS:
        cards.append(current_card)
        current_card = []
        curr_row = 1
    else:
        curr_row += 1


# Part 1
winning_card, winning_draw = get_first_winning_card(cards, numbers)
unmarked_sum = sum_unmarked_cells(winning_card)

print(unmarked_sum * winning_draw)


# Part 2
found_winner = False
winning_card = None
winning_draw = None

i = 0
print("Num cards:", len(cards))
while len(cards) > 1:
    draw = numbers[i]
    for card in cards:
        card = mark_card(card, draw)
        
    for card in cards:
        if is_winner(card):
            cards.remove(card)
    i += 1

# Start from where we left off in the drawing
#numbers = numbers[i:]

winning_card, winning_draw = get_first_winning_card(cards, numbers)
print_2d_list(winning_card)
print(winning_draw)
unmarked_sum = sum_unmarked_cells(winning_card)


print(unmarked_sum * winning_draw)
