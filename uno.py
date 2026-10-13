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

        if answer.isdigit() and 1< int(answer) <= 4: #Check if user inputs is looks like a number eg: "6"
            #convert to an int
            print("Players get ready to play UNO!")
            return int(answer)
        
        print("This is a 2-4 player games \n")

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
    for player in  range(game_players):
        player
    return



