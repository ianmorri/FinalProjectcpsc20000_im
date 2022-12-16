# =====================================================================
# Ian Morrison
# cpsc-20000 Final Project
# The Python Games
# =====================================================================
# Imports/Variable
import random
import time

players = []

#=====================================================================
# Intro
print("===================================================")
print("Welcome to The Python Games!\n")
print("Players will fight until there is one remaining!")
print("===================================================")

# =====================================================================
# Functions
## allows player to add players to game

def addplayers():

    while True:
        num_players = input("How many players are there?: ")
        
        try: 
            num_players = int(num_players)
            if num_players > 1: 
                break
        except: 
            continue

    for i in range(num_players):
        name = input("Enter the name of player {}: ".format(i+1))
        players.append(name)

# -----------------------------------------------------------------------------
## restarts game

def restart():
    players.clear()
    restartgame = input("Would you like to play again(Type 'yes' or 'no'): " )
    restartgame = restartgame.lower()
    if restartgame == "yes":
        main()

# =====================================================================
# main()
def main():

    addplayers()

    
    print("Current players:{}".format(players))
    
    time.sleep(.5)

    while len(players) > 1: 
        player1 = random.choice(players)
        player2 = random.choice(players)

        while player1 == player2:
            player2 = random.choice(players)
  
        print(f"\n{player1} will fight against {player2}.")
        
        time.sleep(.5)
  
        if random.random() < 0.5:
    
            print(f"{player1} wins the battle!")
            players.remove(player2)
        else:
            print(f"{player2} wins the battle!")
            players.remove(player1)
        time.sleep(.5)
    print("\nThe last remaining player is the winner:")
    print(players[0])
    print("")

    restart()
# ====================================================================

main()