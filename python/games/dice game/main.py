import random as rand
import pygame as py
endGame = False
rolls = 30
maxScore = 30

def roll():
    value = rand.randint(1,6)
    return value

players = input("Enter the number of players: ")
while True:
    if players.isdigit():
        players = int(players)
        if 2<= players <=3:
            break
    else:
        print("Not valid amount of players. ")        
playerScore = [0 for i in range(len(players))]

def end(playerScore):
    if max(playerScore) >= maxScore:
        endGame = True
    return endGame

while not endGame:
    end(playerScore)
    for playerIdx in range(players):
        print("Your total score is", playerScore[playerIdx], '\n')
        currScore = 0

        while True:
            ifRoll = input("Would you like to roll (y): ")
            if ifRoll.islower() != 'y':
                break
            new = roll()
            if new == 1:
                print("You rolled a 1, turn done. ")
            else:
                print("you rolled a", new)
                currScore += new
            print(" your score is ", currScore)
        
        playerScore[playerIdx] += currScore
        print("Your total score is", playerScore[playerIdx])
max_score = max(playerScore)
winningIdx = playerScore.index(maxScore)
print("The player who won is", winningIdx +1, 
      'is the winner with score of: ', max_score)
