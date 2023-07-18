import random

def get_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return (rank, suit)

def calculate_score(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    score = sum(values[rank] for rank, _ in hand)
    # Adjusting the score for Aces (if the total score is greater than 21)
    num_aces = sum(rank == 'Ace' for rank, _ in hand)
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

def show_hand(hand, owner):
    print(f"{owner}'s Hand: ", end='')
    for card in hand:
        print(f"{card[0]} of {card[1]}", end=', ')
    print()

def player_turn(player_hand):
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(get_card())
            show_hand(player_hand, "Player")
            score = calculate_score(player_hand)
            print("Player's Score:", score)
            if score > 21:
                print("Bust! You lose!")
                return False
        elif choice == 's':
            return True
        else:
            print("Invalid choice. Please enter 'h' for hit or 's' for stand.")

def dealer_turn(dealer_hand):
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(get_card())
        show_hand(dealer_hand, "Dealer")
        score = calculate_score(dealer_hand)
        print("Dealer's Score:", score)
    if calculate_score(dealer_hand) > 21:
        print("Dealer busts! You win!")
        return False
    return True

def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    if player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def play_blackjack():
    print("Welcome to Blackjack!")
    player_hand = [get_card(), get_card()]
    dealer_hand = [get_card(), get_card()]
    
    show_hand(player_hand, "Player")
    show_hand(dealer_hand[:1], "Dealer")
    
    if calculate_score(player_hand) == 21:
        print("Blackjack! You win!")
        return
    
    if not player_turn(player_hand):
        return
    
    if not dealer_turn(dealer_hand):
        return
    
    determine_winner(player_hand, dealer_hand)

if __name__ == "__main__":
    play_blackjack()
