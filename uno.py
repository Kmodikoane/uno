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
    print(len(card_Deck))
    return card_Deck

build_deck()