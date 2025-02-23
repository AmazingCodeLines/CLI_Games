
import random
# Wecome message

print("--------------------")
print("Welcome to Higher-Lower-Same!")
print("--------------------")

# User chooses number of decks
def number_of_decks():
    num_decks = input("How many decks would you like to play with?").strip()
    try:
        num_decks = int(num_decks)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return number_of_decks()
    if num_decks < 1:
        print("Invalid input. Please enter a number greater than 0.")
        return number_of_decks()
    return num_decks

# Buld Paying Deck with the choosen number of decks & shuffle the deck
def build_deck(num_decks):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for _ in range(num_decks):
        for suit in suits:
            for value in values:
                deck.append((value, suit))
    random.shuffle(deck)
    return deck


# Present Card to the User and get the next card
def get_card(playing_deck):
    return playing_deck.pop()


# User chooses Higher, Lower, Same or Quit
def user_choice():
    choice = input("Take a guess: [H]igher, [L]ower, [S]ame or [Q]uit?").strip().lower()
    if choice not in ['h', 'l', 's', 'q']:
        print("Invalid choice. Please enter: [H]igher, [L]ower, [S]ame or [Q]uit.")
        return user_choice()
    return choice

# get card value
def get_card_value(card):
    values = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10,
        "A": 11
        }
    return values[card[0]]


# Check if the user is correct
    # If correct:
        # user gets the points of the current card
    # If incorrect:
        # user loses the points of the current card
def check_guess_and_points(card, next_card, choice):
    points = 0
    card_value = get_card_value(card)
    next_card_value = get_card_value(next_card)
    if next_card_value > card_value and choice == 'h':
        points += card_value
    elif next_card_value < card_value and choice == 'l':
        points += card_value
    elif next_card_value == card_value and choice == 's':
        points += card_value
    else:
        points -= card_value
    return points


def play_game():
    num_decks = number_of_decks()
    deck = build_deck(num_decks)
    score = 0
    turn = 1

    print(f"-     Turn: {turn}     -")

    # Get the first card
    current_card = get_card(deck)
    print(f"Current card: {current_card[0]} of {current_card[1]}")

    # Main game loop
    while True:
        choice = user_choice()
        if choice == 'q':
            print(f"Game over! Your final score is: {score}")
            break

        # Get the next card
        next_card = get_card(deck)

        # Check if the user guessed correctly and update the score and the turn
        points = check_guess_and_points(current_card, next_card, choice)
        score += points
        turn += 1

        # Show results
        if points > 0:
            print("--------------------")
            print(f">>> Correct! <<< \nScore: {score}")
            print(f"Cards remaining: {len(deck)}")
            print("--------------------")
        else:
            print("--------------------")
            print(f">>> Incorrect! <<< \nScore: {score}")
            print(f"Cards remaining: {len(deck)}")
            print("--------------------")
        
        # Player keeps the card (previous next_card) and the next_card becomes the current_card
        current_card = next_card
        print(f"-     Turn: {turn}     -")
        print(f"Current card: {current_card[0]} of {current_card[1]}")
    
    # The game is over
    print("Thanks for playing!")
    print(f"Your final score is: {score}")


if __name__ == '__main__':
    play_game()





