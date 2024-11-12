import random
from art import *
# Function to deal a card
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the score of a hand
def calculate_score(cards):
    """
    Calculates the score for a given hand.
    Returns 0 for a Blackjack, or the total score with Ace adjustments.
    """
    # Check for a Blackjack (Ace + 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents a Blackjack

    # Adjust Aces if the score is over 21
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)

# Function to display the hands
def display_hands(user_cards, dealer_cards, hide_dealer_card=True):
    """
    Displays the player's hand and the dealer's first card.
    If hide_dealer_card is False, shows the dealer's full hand and score.
    """
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    if hide_dealer_card:
        print(f"Dealer's first card: {dealer_cards[0]}")
    else:
        print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

# Function to determine the winner
def determine_winner(user_score, dealer_score):
    """
    Determines the winner based on the final scores.
    """
    if dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif user_score == dealer_score:
        return "It's a tie!"
    elif user_score == 0:
        return "You got a Blackjack! You win!"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You lose."
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

# Main function to play Blackjack
def play_blackjack():
    tprint("blackjack")
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    # Flag to determine if the game is over
    game_over = False

    # User's turn
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        display_hands(user_cards, dealer_cards)

        # Check if the user has gone over 21
        if user_score > 21:
            print("You went over 21. You lose!")
            return  # Immediately terminate the game

        # Check for game-ending conditions
        if user_score == 0 or dealer_score == 0:
            game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer's turn: draw until reaching a score of at least 17
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    # Show final hands and determine the result
    display_hands(user_cards, dealer_cards, hide_dealer_card=False)
    final_result = determine_winner(calculate_score(user_cards), calculate_score(dealer_cards))
    print(final_result)

# Run the game
play_blackjack()
