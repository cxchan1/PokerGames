from deck import *
from result import *

deck = Deck()
deck.shuffle()
# initialize empty hand
you = None
computer = None

print("""
Let's play poker.
\tp(play): Start the game by draw 5 random cards between you and the computer
\ts(huffle): return all cards to the deck and reshuffle
\tq(uit): quit the program""")

while True:
    user_input = input(">>> ")
    if user_input.lower() in ["q","quit"]:
        break
    elif user_input.lower() in ["s","shuffle"]:
        deck.shuffle()
        you.cards = []
        computer.cards = []
        print("Shuffled the deck")
    elif user_input.lower() in ["p","play"]:
        drawCount = 5
        if deck.countRemaining < drawCount:
            print("Only {} cards are left in the deck. Return all cards to the deck and shuffled the deck.".format(deck.countRemaining))
            deck.shuffle()
            you.cards = []
            computer.cards = []

            you = deck.draw(5)
            computer = deck.draw(5)
            result = Result(you, computer)
            print("You: {} {} vs Computer: {} {}".format(you.toConsole(), you.classify().name.replace("_"," "),
                                                                                  computer.toConsole(), computer.classify().name.replace("_"," ")))
            if result.compare() == 1:
                print("You Win!")
            elif result.compare() == 0:
                print("You Lose!")
            else:
                print("It's a Ties")
            print("{} cards left in the deck.".format(deck.countRemaining))
        else:
            you = deck.draw(5)
            computer = deck.draw(5)
            result = Result(you, computer)
            print("You: {} {} vs Computer: {} {}".format(you.toConsole(), you.classify().name.replace("_"," "),
                                                                                  computer.toConsole(), computer.classify().name.replace("_"," ")))
            if result.compare() == 1:
                print("You Win!")
            elif result.compare() == 0:
                print("You Lose!")
            else:
                print("It's a Ties")
            print("{} cards left in the deck.".format(deck.countRemaining))
    else:
        print("Unknown command")
