import random

notes = '''
            - Problemer hvis der er mere end 1 ace            
'''

class DeckOfCards:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.rank_translate = {1: 'Ace', 10: 'Jack', 10: 'Queen', 10: 'Kings'}

    def shuffle_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append((rank, suit))
        random.shuffle(deck)

        return deck

    

class Blackjack:
    def __init__(self):
        self.deck_of_cards = DeckOfCards()
        self.shuffled_deck = self.deck_of_cards.shuffle_deck()
        
        self.card_count = 0
        self.player_stand = False

        self.player_hand = []
        self.player_score = 0

        self.dealer_hand = []
        self.dealer_score = 0


    def setup(self):
        print("Cards are being dealt..")
        while len(self.player_hand) < 2:
            self.hit(self.player_hand)
            print(f"Player got: {self.player_hand[len(self.player_hand)-1][0]} of {self.player_hand[len(self.player_hand)-1][1]}")

        while len(self.dealer_hand) < 1:
            self.hit(self.dealer_hand)
            print(f"Dealer got: {self.player_hand[0][0]} of {self.player_hand[0][1]}")

    def player_loop(self):

        while True:

            self.player_score, second_score = self.calculate_cards(self.player_hand)
            if second_score > self.player_score:
                self.player_score = second_score

            self.dealer_score, second_score = self.calculate_cards(self.dealer_hand)
            if second_score > self.dealer_score:
                self.dealer_score = second_score

            
            player_hand = self.pretty_hand(self.player_hand)
            dealer_hand = self.pretty_hand(self.dealer_hand)
            print("----------------------------------")
            print(f"Your hand: {', '.join(player_hand)}")
            print(f"Your score: {self.player_score}")
            print("----------------------------------")
            print(f"Dealers Hand: {dealer_hand[0]}, Hole Card")
            print(f"Dealers score: {self.dealer_score}")
            print("----------------------------------")
            
            if self.player_score == 21:
                return False
            elif self.player_score > 21:
                return True

            print("What to do? Hit or stand")
            
            choice = input(":/> ")
            if choice == 'hit':
                self.hit(self.player_hand)
            elif choice == 'stand':
                return False
            else:
                print("ONLY HIT OR STAND U DUMBITCH")

            

    
    def dealer_loop(self):
        running = True
        while running:

            self.dealer_score, second_score = self.calculate_cards(self.dealer_hand)
            if second_score > self.dealer_score:
                self.dealer_score = second_score

            player_hand = self.pretty_hand(self.player_hand)
            dealer_hand = self.pretty_hand(self.dealer_hand)

            print("----------------------------------")
            print(f"Your hand: {', '.join(player_hand)}")
            print(f"Your score: {self.player_score}")
            print("----------------------------------")
            print(f"Dealers Hand: {', '.join(dealer_hand)}")
            print(f"Dealers score: {self.dealer_score}")
            print("----------------------------------")

            if self.dealer_score >= 16:
                running = False
            else:
                self.hit(self.dealer_hand)

    def check_winnings(self):
        if self.player_score > 21:
            return 'dealer'
        elif self.dealer_score > 21:
            return 'player'

        if self.player_score > self.dealer_score:
            return 'player'
        elif self.player_score == self.dealer_score:
            return 'draw'
        else:
            return 'dealer'

    def hit(self, hand):
        hand.append(self.shuffled_deck[self.card_count])
        self.card_count += 1

    def calculate_cards(self, hand):
        translated_hand = self.translate_hand(hand)
        second_score = 0
        calculated_score = 0
        for card in translated_hand:
            calculated_score += card[0]
            if card[0] == 1:
                second_score += 11
            else:
                second_score += card[0]
            
            if second_score > 21:
                second_score = calculated_score
        
        return calculated_score, second_score
    
    def translate_hand(self, hand):
        translated_hand = []
        for card in hand:
            if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
                translated_hand.append((10, card[1]))
            elif card[0] == 'Ace':
                translated_hand.append((1, card[1]))
            else:
                translated_hand.append(card)

        return translated_hand
    
    def pretty_hand(self, hand):
        pretty_hand = []
        for card in hand:
            pretty_hand.append(f"{card[0]} of {card[1]}")

        return pretty_hand
            


def main():
    blackjack = Blackjack()

    running = True

    while running:

        blackjack.setup()
        busted = blackjack.player_loop()
        if busted != True:
            blackjack.dealer_loop()
            winner = blackjack.check_winnings()

            if winner == 'player':
                print("CONGRATZ YOU WON!!")
            elif winner == 'draw':
                print("DRAW!!")
            else:
                print("YOU LOST!! LOSERRR")
        else:
            print("YOU BUSTED A NUT!!")


        print("You want to play again? y/n")
        restart = input(":/> ")
        if restart == 'n':
            running = False
            print("Thanks for playing :D")
        elif restart == 'y':
            blackjack = Blackjack()
        else:
            print("Only y/n")
        

if __name__ == '__main__':
    main()