############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from replit import clear
from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# we code this hint later

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns thca ae score.
#Look up the sum() function to help you do this.


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.



#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare (user_score, computer_score):
    if user_score >21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21: 
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

# Hint 5

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

# Hint 11:
    while not is_game_over:
        

# Hint 9:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current_score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards list. If no, the game has ended. 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.          
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()


# from replit import clear
# from art import logo
# import random

# if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     clear()
#     should_continue = True

# else:
#     should_continue = False

# # Hint


# def black_jack_start():
#     print(logo)
#     if should_continue == True:
#         cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         total_hand = random.sample((cards), 2)
#         first_hand_dealer = random.sample((cards), 2)
#         if total_hand == [10, 11]:
#             print("black jack")
#         elif first_hand_dealer == [10, 11]:
#             print("black jack")

#         sum_score_initial = total_hand[0] + total_hand[1]
#         print(
#             f"   Your cards: {total_hand}, current score: {sum_score_initial}")
#         print(f"   Computer's first card: {first_hand_dealer[0]}")
#         while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
#             second_hand = random.choice(cards)
#             total_hand.append(second_hand)
#             sum_score_final = 0
#             for score in total_hand:
#                 if sum_score_final > 21 and score == 11:
#                     score = 1
#                 sum_score_final += score
#             print(
#                 f"   Your cards: {total_hand}, current score: {sum_score_initial}"
#             )
#             print(f"   Computer's first card: {first_hand_dealer[0]}")
#             print(
#                 f"   Your final hand: {total_hand}, final score: {sum_score_final}"
#             )

#             if sum_score_final > 21:
#                 print(f"   You went over. You lose ")

#         dealer_sum = 0
#         while dealer_sum < 17:
#             second_hand_dealer = random.choice(cards)
#             first_hand_dealer.append(second_hand_dealer)
#             for dealer_score in first_hand_dealer:
#                 if dealer_sum > 21 and dealer_score == 11:
#                     dealer_score = 1
#                 dealer_sum += dealer_score
#                 # ok so here I have to deal cards to the dealer until it reaches 21 or more.
#         print(
#             f"   Computer's final hand: {first_hand_dealer}, final score: {dealer_sum}"
#         )
#     # else:
#     #     should_continue = False


# black_jack_start()
