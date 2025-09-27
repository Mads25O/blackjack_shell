import random

class Deck_Of_Cards:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.rank_translate = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'Kings'}

    def randomize_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append((rank, suit))
        random.shuffle(deck)

        return deck

class Blackjack:
    def __init__(self):
        deck_of_cards = Deck_Of_Cards()
        self.randomized_deck = deck_of_cards.randomize_deck()
        self.card_count = 0
        self.player_stand = False

    def calculate_cards(self, hand):
        total = 0
        for rank in hand:
            total += rank[0]
        return total
    
    def reset_game(self):
        pass

    def reset_deck(self):
        pass
    
    def game_over(self, player_hand):
        if self.calculate_cards(player_hand) > 21:
            return True
        else:
            return False
        
    def check_winning_conditions(self, player_hand, dealer_hand):
        player_score = self.calculate_cards(player_hand)
        dealer_score = self.calculate_cards(dealer_hand)
        
        if player_score > dealer_score:
            return True
        else:
            return False

        

    def game_start(self, player_hand, dealer_hand):
        ### START ###
        while len(player_hand) < 2:
            self.hit(player_hand)

        while len(dealer_hand) < 2:
            self.hit(dealer_hand)
            

    def game_loop(self, player_hand, dealer_hand):
        ### ACTUAL GAME LOOP ###        
        print(f"Your hand: {player_hand}")
        print("What to do? Hit or stand")
        choice = input(":/> ")
        if choice == 'hit':
            self.hit(player_hand)
        elif choice == 'stand':
            self.player_stand = True
        else:
            print("ONLY HIT OR STAND U DUMBITCH")

        #print(f"PLAYER {player_hand} TOTAL {self.calculate_cards(player_hand)} DEALER {dealer_hand} TOTAL {self.calculate_cards(dealer_hand)}")

    def hit(self, hand):
        hand.append(self.randomized_deck[self.card_count])
        self.card_count += 1
        if self.card_count == 53:
            self.reset_deck()
            


def main():
    deck = Deck_Of_Cards()
    blackjack = Blackjack()

    randomized_deck = deck.randomize_deck()
    player_hand = []
    dealer_hand = []
#    print(randomized_deck)

    running = True

    while running:
        if blackjack.player_stand == True:
            winning_conditions = blackjack.check_winning_conditions(player_hand, dealer_hand)
            if winning_conditions == True:
                print("PLAYER WON")
            else:
                print("DEALER WON")
    
        blackjack.game_start(player_hand, dealer_hand)
        blackjack.game_loop(player_hand, dealer_hand)
        
        #game_over = blackjack.game_over(player_hand)
        #if game_over == True:
        #    print("lost bitch")
        #    running = False

if __name__ == '__main__':
    main()