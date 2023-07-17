import random

print( """  __      __       .__                                  __           ___________                    __________         __    __  .__  
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   \__    ___/___   ____   ____   \______   \_____ _/  |__/  |_|__| 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \    |    |_/ __ \_/ __ \ /    \   |     ___/\__  \\   __\   __\  | 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )   |    |\  ___/\  ___/|   |  \  |    |     / __ \|  |  |  | |  | 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/    |____| \___  >\___  >___|  /  |____|    (____  /__|  |__| |__| 
       \/       \/          \/            \/     \/                              \/     \/     \/                  \/                 """)


print(" \n The Rules are Simple, Two players draw 3 cards each, the player with highest card values wins the round, game continues until 1 losses all his money")
Bet_Amount = int(input("\n Enter the Bet Amount : "))
if Bet_Amount > 10000:
    print("Error, Please Run again")
my_bank = 10000
player2_bank = 10000

Card_Symbols = ["Spades", "Diamond", "Hearts", "Clubs"]
Card_Numbers = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
Card_Values =  [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Cards_Spades = [[cards_number + ' of ' + Card_Symbols[0]]  for cards_number in Card_Numbers]
Cards_Spades_Segreagated = [(cards_number + ' of ' + Card_Symbols[0])  for cards_number in Card_Numbers]
Cards_Spades_Dict = {key: value for key, value in zip((cards for cards in Cards_Spades_Segreagated),Card_Values)}

Cards_Diamonds = [[cards_number + ' of ' + Card_Symbols[1]]  for cards_number in Card_Numbers]
Cards_Diamonds_Segreagated = [(cards_number + ' of ' + Card_Symbols[1])  for cards_number in Card_Numbers]
Cards_Diamonds_Dict = {key: value for key, value in zip((cards for cards in Cards_Diamonds_Segreagated),Card_Values)}

Cards_Hearts = [[cards_number + ' of ' + Card_Symbols[2]]  for cards_number in Card_Numbers]
Cards_Hearts_Segreagated = [(cards_number + ' of ' + Card_Symbols[2])  for cards_number in Card_Numbers]
Cards_Hearts_Dict = {key: value for key, value in zip(Cards_Hearts_Segreagated,Card_Values)}

Cards_Clubs = [[cards_number + ' of ' + Card_Symbols[3]]  for cards_number in Card_Numbers]
Cards_Clubs_Segreagated = [(cards_number + ' of ' + Card_Symbols[3])  for cards_number in Card_Numbers]
Cards_Clubs_Dict = {key: value for key, value in zip(Cards_Clubs_Segreagated,Card_Values)}

All_Cards = Cards_Spades + Cards_Diamonds + Cards_Hearts + Cards_Clubs
All_Cards_Dict = {}
All_Cards_Dict.update(Cards_Spades_Dict)
All_Cards_Dict.update(Cards_Diamonds_Dict)
All_Cards_Dict.update(Cards_Hearts_Dict)
All_Cards_Dict.update(Cards_Clubs_Dict)

 
game_cards = random.choices(All_Cards, k=6)
My_cards = [game_cards[0],game_cards[1], game_cards[2]]
Player2_cards = [game_cards[3],game_cards[4], game_cards[5]]


count1 = 0
count2 = 0

def winner(my_cards, player2_cards):
    global count1
    global count2
    global game_cards
    global My_cards
    global Player2_cards
    game_cards = random.choices(All_Cards, k=6)
    My_cards = [game_cards[0],game_cards[1], game_cards[2]]
    Player2_cards = [game_cards[3],game_cards[4], game_cards[5]]
    
    game_cards = random.choices(All_Cards, k=6)
    count1 += All_Cards_Dict[my_cards[0][0]] +  All_Cards_Dict[my_cards[0][0]] +  All_Cards_Dict[my_cards[0][0]]
    count2 += All_Cards_Dict[player2_cards[0][0]] +  All_Cards_Dict[player2_cards[0][0]] +  All_Cards_Dict[player2_cards[0][0]] 

winner(My_cards, Player2_cards)

while (my_bank > 0 and player2_bank < 20000) or (player2_bank > 0 and my_bank > 20000):
    if(input("\n Play next round? Y/N : ")) == "Y":
        print("\n Your cards are" + str(My_cards))
        print("\n Your opponents cards are" + str(Player2_cards))
        winner(My_cards, Player2_cards)
        if count1 > count2:
            my_bank += Bet_Amount
            player2_bank -= Bet_Amount
            print("\n You win this round \n\n Your total balance = {}".format(my_bank))

        elif count2 > count1:
            player2_bank += Bet_Amount
            my_bank -= Bet_Amount
            print("\n Player2 wins this round \n\n Your total balance = {}".format(my_bank))
        elif count1 == count2:
            print("\n This round tied")
    else:
        break
    continue
         
    









    

































