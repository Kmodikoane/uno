import random

def build_deck():
    """
    This function reutrn a deck of 108 cards
    Parameters: None
    Return values: card_Deck -> list
    """
    card_Deck = []
    deck_colours  = ["Red", "Green", "Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Skip", "Reverse", "Draw Two"]
    
    for colour in deck_colours:
        for value in values:
            cardVal = f"{colour} {value}"
            card_Deck.append(cardVal)

            if value != 0:
                card_Deck.append(cardVal)
 
    for i in range(4):
        card_Deck.append("wild")
        card_Deck.append("wild draw four")
    
    return card_Deck

deck = build_deck()

def shuffle_deck(deck):
    """
    This function shuffles the deck of cards
    Parameters: deck -> list
    Return: shuffled deck of cards -> list
    """
    random.shuffle(deck)
    shuffled_deck = deck
    random.shuffle(shuffled_deck)
    return shuffled_deck

shuffled_deck = shuffle_deck(deck)

def players():
    """
    Program
        Print Uno welcome message 
        Accept user input as the number of players in the game
    Parameters: None 
    Returns: numOf_players -> int
    """
    print("="*20, "Welcome to UNO, The 2-4 player card game!", "="*20)
    print("=="*40, "\n")

    #Catch any exceptions in the case a user inputs a non-integer value
    while True:
        answer = input("How many players in the game?: ")

        if answer.isdigit() and 1<= int(answer) <= 4: #Check if user inputs is looks like a number eg: "6"
            #convert to an int
            print("Players get ready to play UNO!")
            return int(answer)
        
        print("This is a 1-4 player games \n")

game_players = players()

def deal_cards(game_players, shuffled_deck):
    """
    Deals cards to players
    Parameters:
        game_players -> int
        shuffle_deck -> list
    Returns: dictionary of cards for each player
    """
    players_with_cards = {} 
    for player in range(1, game_players + 1):
        players_with_cards[player] = []
   
        for card_drawn in  range(7):
            players_with_cards[player].append(shuffled_deck.pop())
    
    return players_with_cards

players_with_cards = deal_cards(game_players, shuffled_deck)

def show_hand(players_with_cards):
    """
    Show each players hand
    Parameters: player with dealt cards -> dict
    Returns: None
    Print player hand
    """
    for player in players_with_cards:
        print(f"\nPlayer {player}: Cards: {players_with_cards[player]}")

show_hand(players_with_cards)

def play_cards(shuffled_deck):
    discard_pile = []

    for card in shuffled_deck:
        if card != "wild_card" or card != "wild draw four"

play_cards(shuffled_deck)



