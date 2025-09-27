import random

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
    
    def translate_ranks(self, deck):
        translated_deck = []
        for i in range(len(deck)):
            if deck[i][0] == 'Jack' or deck[i][0] == 'Queen' or deck[i][0] == 'King':
                translated_deck.append((10, deck[i][1]))
            elif deck[i][0] == 'Ace':
                translated_deck.append((1, deck[i][1]))
            else:
                translated_deck.append(deck[i])

        return translated_deck
    
    def pretty_deck(self, deck):
        pretty_deck = []
        for i in range(len(deck)):
            pretty_deck.append(f"{deck[i][0]} of {deck[i][1]}")

        return pretty_deck
    

class Blackjack:
    def __init__(self):
        self.deck_of_cards = DeckOfCards()
        self.shuffled_deck = self.deck_of_cards.shuffle_deck()
        self.translated_deck = self.deck_of_cards.translate_ranks(self.shuffled_deck)
        self.pretty_deck = self.deck_of_cards.pretty_deck(self.shuffled_deck)
        
        self.card_count = 0
        self.player_stand = False

        self.player_hand = []
        self.calc_player_hand = []
        self.player_score = 0

        self.dealer_hand = []
        self.calc_dealer_hand = []
        self.dealer_score = 0


    def setup(self):
        while len(self.player_hand) < 2:
            self.hit(self.player_hand, self.calc_player_hand)

        while len(self.dealer_hand) < 2:
            self.hit(self.dealer_hand, self.calc_dealer_hand)
    

    def player_loop(self):

        player_loop_running = True
        while player_loop_running:

            self.player_score, second_score = self.calculate_cards(self.calc_player_hand)
            if second_score > self.player_score:
                self.player_score = second_score

            if self.player_score >= 21:
                player_loop_running = False
                break

            print("----------------------------------")
            print(f"Your hand: {', '.join(self.player_hand)}")
            print(f"Your score: {self.player_score}")
            print("----------------------------------")
            print(f"Dealers Hand: {self.dealer_hand[0]}, Hole Card")
            print(f"Dealers score: {self.calc_dealer_hand[0][0]}")
            print("----------------------------------")
            
            print("What to do? Hit or stand")
            
            choice = input(":/> ")
            if choice == 'hit':
                self.hit(self.player_hand, self.calc_player_hand)
            elif choice == 'stand':
                player_loop_running = False
            else:
                print("ONLY HIT OR STAND U DUMBITCH")

    
    def dealer_loop(self):
        running = True
        while running:

            self.dealer_score, second_score = self.calculate_cards(self.calc_dealer_hand)
            if second_score > self.dealer_score:
                self.dealer_score = second_score
            print("----------------------------------")
            print(f"Your hand: {', '.join(self.player_hand)}")
            print(f"Your score: {self.player_score}")
            print("----------------------------------")
            print(f"Dealers Hand: {', '.join(self.dealer_hand)}")
            print(f"Dealers score: {self.dealer_score}")
            print("----------------------------------")

            if self.dealer_score >= 16:
                running = False
            else:
                self.hit(self.dealer_hand, self.calc_dealer_hand)

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

    def hit(self, hand, calc_hand):
        hand.append(self.pretty_deck[self.card_count])
        calc_hand.append(self.translated_deck[self.card_count])
        self.card_count += 1

    def calculate_cards(self, hand):
        second_score = 0
        calculated_score = 0
        for i in range(len(hand)):
            calculated_score += hand[i][0]
            if hand[i][0] == 1:
                second_score += 11
            else:
                second_score += hand[i][0]
            
            if second_score > 21:
                second_score = calculated_score
        
        return calculated_score, second_score
            


def main():
    blackjack = Blackjack()

    running = True

    while running:

        blackjack.setup()
        blackjack.player_loop()
        blackjack.dealer_loop()
        winner = blackjack.check_winnings()

        if winner == 'player':
            print("CONGRATZ YOU WON!!")
        else:
            print("YOU LOST!! LOSERRR")


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