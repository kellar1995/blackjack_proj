import random

class Game:
    def __init__(self):
        self.suits = ["clubs", "diamonds", "hearts", "spades"]
        self.deck = []
        self.your_cards = []
        self.dealer_cards = []

    def game_start(self):
        for card in self.suits:
            for i in range(1,14):
                self.deck.append((card,i))
        random.shuffle(self.deck)
        self.card1 = random.choice(self.deck)
        self.card2 = random.choice(self.deck)
        self.dealer_card1 = random.choice(self.deck)
        self.dealer_card2 = random.choice(self.deck)
        self.your_cards.append(self.card1)
        self.your_cards.append(self.card2)
        self.dealer_cards.append(self.dealer_card1)
        self.dealer_cards.append(self.dealer_card2)
        self.your_amount = sum([x[1] for x in self.your_cards])
        self.dealer_amount = sum([y[1] for y in self.dealer_cards])
        print(f'Your cards are a {self.card1} and a {self.card2} for a total of {self.your_amount}')
        print(f"The dealer's are a {self.dealer_card1}and HIDDEN")
        if self.your_amount == 21:
            print("Lucky blackjack! You win!")
        elif self.your_amount > 21:
            print("You lost!")
        elif self.dealer_amount > 21:
            print("The dealer lost.")
        elif self.dealer_amount == 21:
            print("The dealer got a blackjack!")

    def hit(self):
        random.shuffle(self.deck)
        self.card3 = random.choice(self.deck)
        self.dealer_card3 = random.choice(self.deck)
        self.your_cards.append(self.card3)
        self.dealer_cards.append(self.dealer_card3)
        self.your_amount = sum([x[1] for x in self.your_cards])
        self.dealer_amount = sum([y[1] for y in self.dealer_cards])
        print(f"Your cards are {self.your_cards} for a total of {self.your_amount}")
        print(f"The dealer's card is {self.dealer_card1} and HIDDEN")
        if self.your_amount > 21:
            print("You lost!")
        elif self.dealer_amount > 21:
            print("The dealer lost.")
        elif self.dealer_amount == 21:
            print("The dealer won!")

    def stand(self):
        self.your_amount = sum([x[1] for x in self.your_cards])
        self.dealer_amount = sum([y[1] for y in self.dealer_cards])
        print(f"Your cards were {self.your_cards} for a total of {self.your_amount}.")
        print(f"The dealer's cards were {self.dealer_cards} for a total of {self.dealer_amount}.")
        if self.your_amount > self.dealer_amount and self.your_amount <= 21:
            print("Congratulations! You won!")
        elif self.your_amount < self.dealer_amount and self.dealer_amount <= 21:
            print("The dealer won!")
        elif self.your_amount > 21 and self.dealer_amount < 21:
            print("The dealer won.")
        elif self.your_amount < 21 and self.dealer_amount > 21:
            print("Congratulations! You won!")


blackjack = Game()
while True:
    play = input("Hello, would you like to play? y/n").lower()
    if play == "n":
        break
    if play == "y":
        blackjack.game_start()
    choice = input("Would you like to hit or stand?")
    if choice == "hit":
        blackjack.hit()
    elif choice == "stand":
        blackjack.stand()
    choice = input("Would you like to hit or stand?")
    if choice == "hit":
        blackjack.hit()
    elif choice == "stand":
        blackjack.stand()
    choice = input("Would you like to hit or stand?")
    if choice == "hit":
        blackjack.hit()
    elif choice == "stand":
        blackjack.stand()
    choice = input("Would you like to hit or stand?")
    if choice == "hit":
        blackjack.hit()
    elif choice == "stand":
        blackjack.stand()
    choice = input("Would you like to hit or stand?")
    if choice == "hit":
        blackjack.hit()
    elif choice == "stand":
        blackjack.stand()