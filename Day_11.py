import random

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return"Lose, opponent has Blackjack"
    elif u_score == 0:
        return"Win with Blackjack"
    elif u_score > 21:
        return "You went over 21"
    elif c_score > 21:
        return "Opponent went over 21, You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def dealcard():
    """Retrun a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_card = []
computer_card = []

def calculation(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

for _ in range(2):
    user_card.append(dealcard())
    computer_card.append(dealcard())
computer_score = -1
user_score = -1
game_over = False
while not game_over:
    user_score = calculation(user_card)
    computer_score = calculation(computer_card)

    print(f"Your new card is: {user_card}",f"Current score is {user_score}")
    print(f"Computer new card is: {computer_card}",f"Current score is {computer_score}")

    if user_score == 0 or computer_score == 0 or user_score >21:
        game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
        if user_should_deal == 'y':
            user_card.append(dealcard())
        else:
            game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(dealcard())
    computer_score = calculation(computer_card)

print(f"Your new card is: {user_card}",f"Current score is {user_score}")
print(f"Computer score is {computer_card}, final score is {computer_score}")
print(compare(user_score, computer_score))