import random

print( """  __      __       .__                                  __           ___________                    __________         __    __  .__  
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   \__    ___/___   ____   ____   \______   \_____ _/  |__/  |_|__| 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \    |    |_/ __ \_/ __ \ /    \   |     ___/\__  \\   __\   __\  | 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )   |    |\  ___/\  ___/|   |  \  |    |     / __ \|  |  |  | |  | 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/    |____| \___  >\___  >___|  /  |____|    (____  /__|  |__| |__| 
       \/       \/          \/            \/     \/                              \/     \/     \/                  \/                 """)


print(" \n The Rules are Simple, Two players draw 3 cards each, the player with highest card wins the round, game continues until 1 losses all his money")
Bet_Amount = input("Bet Amount")

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
#print(game_cards)
My_cards = [game_cards[0],game_cards[1], game_cards[2]]
Player2_cards = [game_cards[3],game_cards[4], game_cards[5]]
print("Your cards are" + str(My_cards))
print(Player2_cards)



count1 = 0
count2 = 0



def set1(my_cards):
    global count1
    global count2
    if my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "A":
        count1 += 100
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "K":
        count1 += 99
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "Q":
        count1 += 98
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "J":
        count1 += 97
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "10":
        count1 += 96
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "9":
        count1 += 95
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "8":
        count1 += 94
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "7":
        count1 += 93
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "6":
        count1 += 92
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "5":
        count1 += 91
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "4":
        count1 += 90
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "3":
        count1 += 89
        return True
    elif my_cards[0][0][0] == my_cards[1][0][0] == my_cards[2][0][0] == "2":
        count1 += 88
        return True
    return False

def set2(player2_cards):
    global count1
    global count2
    if player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "A":
        count2 += 100
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "K":
        count2 += 99
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "Q":
        count2 += 98
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "J":
        count2 += 97
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "10":
        count2+= 96
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "9":
        count2 += 95
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "8":
        count2 += 94
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "7":
        count2 += 93
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "6":
        count2 += 92
        return True
    elif player2_cards[0][0][0] == player2_cards[1][0][0] == player2_cards[2][0][0] == "5":
        count2 += 91
        return True
    elif player2_cards[0][0] == player2_cards[1][0] == player2_cards[2][0] == "4":
        count2 += 90
        return True
    elif player2_cards[0][0] == player2_cards[1][0] == player2_cards[2][0] == "3":
        count2 += 89
        return True
    elif player2_cards[0][0] == player2_cards[1][0] == player2_cards[2][0] == "2":
        count2 += 88
        return True
    return False

def pure_sequence1(my_cards):
    global count1
    global count2
    if (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Spades" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Diamond" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Hearts" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Clubs" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Spades" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Diamond" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Hearts" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]) and ("Clubs" in (my_cards[0][0] and my_cards[1][0] and my_cards[2][0])):
        count1 += 87
        return True
    return False

def pure_sequence2(player2_cards):
    global count1
    global count2
    if (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Spades" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Diamond" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Hearts" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Clubs" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Spades" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Diamond" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Hearts" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]) and ("Clubs" in (player2_cards[0][0] and player2_cards[1][0] and player2_cards[2][0])):
      count2 += 87
      return True
    return False

def sequence1(my_cards):
    global count1
    global count2
    if (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    elif (All_Cards_Dict[my_cards[0][0]] == 1 + All_Cards_Dict[my_cards[1][0]] == 2 + All_Cards_Dict[my_cards[2][0]]):
      count1 += 87
      return True
    return False

def sequence2(player2_cards):
    global count1
    global count2
    if (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    elif (All_Cards_Dict[player2_cards[0][0]] == 1 + All_Cards_Dict[player2_cards[1][0]] == 2 + All_Cards_Dict[player2_cards[2][0]]):
      count2 += 87
      return True
    return False

def colour1(my_cards):
    global count1
    global count2
    count = 0
    for card in my_cards[0]:
        if card[0] == "Spades" or "Diamond" or "Clubs" or "Hearts":
            count += 1
    if  count == 3:
        count1 += 86
        return True
    return False

def colour2(player2_cards):
    global count1
    global count2
    count = 0
    for card in player2_cards[0]:
        if card[0] == "Spades" or "Diamond" or "Clubs" or "Hearts":
            count += 1
    if  count == 3:
        count2 += 86
        return True
    return False

def pair1(my_cards):
    global count1
    global count2
    for num in list(range(3)):
        for card in my_cards[num]:
            if card[0][0] in (card[1][0] or card[2][0]): 
                count1 += 85
                return True
    return False

def pair2(player2_cards):
    global count1
    global count2
    for num in list(range(3)):
        for card in player2_cards[num]:
            if card[0][0] in (card[1][0] or card[2][0]):
                count2 += 85 
                return True
    return False

def highest_card1(my_cards):
    global count1
    global count2
    if my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "A":
        count1 += 73
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "K":
        count1 += 72
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "Q":
        count1 += 71
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "J":
        count1 += 70
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "10":
        count1 += 69
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "9":
        count1 += 68
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "8":
        count1 += 67
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "7":
        count1 += 66
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "6":
        count1 += 65
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "5":
        count1 += 64
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "4":
        count1 += 63
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "3":
        count1 += 62
        return True
    elif my_cards[0][0][0] or my_cards[1][0][0] or my_cards[2][0][0] == "2":
        count1 += 61
        return True
    return False

def highest_card2(player2_cards):
    global count1
    global count2
    if player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "A":
        count2 += 73
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "K":
        count2 += 72
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "Q":
        count2 += 71
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "J":
        count2 += 70
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "10":
        count2 += 69
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "9":
        count2 += 68
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "8":
        count2 += 67
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "7":
        count2 += 66
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "6":
        count2 += 65
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "5":
        count2 += 64
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "4":
        count2 += 63
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "3":
        count2 += 62
        return True
    elif player2_cards[0][0][0] or player2_cards[1][0][0] or player2_cards[2][0][0] == "2":
        count2 += 61
        return True
    return False


print([set1(My_cards), set2(Player2_cards)])
print([pure_sequence1(My_cards), pure_sequence2(Player2_cards)])
print([sequence1(My_cards), sequence2(Player2_cards)])
print([colour1(My_cards), colour2(Player2_cards)])
print([pair1(My_cards), pair2(Player2_cards)])
if set1(My_cards) or set2(Player2_cards) == True:
    if count1 > count2:
        print("You are the winner")
    elif count2 > count1:
        print("Player2 is the winner")
elif pure_sequence1(My_cards) or pure_sequence2(Player2_cards) == True:
    if count1 > count2:
        print("You are the winner")
    elif count2 > count1:
        print("Player2 is the winner")
elif sequence1(My_cards) or sequence2(Player2_cards) == True:
    if count1 > count2:
        print("You are the winner")
    elif count2 > count1:
        print("Player2 is the winner")
elif colour1(My_cards) or colour2(Player2_cards) == True:
    print([colour1(My_cards), colour2(Player2_cards)])
    if count1 > count2:
        print("You are the winner")
    elif count2 > count1:
        print("Player2 is the winner")
elif highest_card1(My_cards) or highest_card2(Player2_cards) == True:
    print([count1, count2])
    if count1 > count2:
        print("You are the winner")
    elif count2 > count1:
        print("Player2 is the winner")
