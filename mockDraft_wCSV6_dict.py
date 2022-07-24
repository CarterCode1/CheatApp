import random
import csv
from collections import OrderedDict
players ={}
rank =[]
with open('Book2.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    players = {rows[0]:rows[1] for rows in csvReader}
with open('rank.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        rank.append(','.join(row))
yourPick = input('What pick do you want? ')

currentPosition = 'null'
teamNumber = 1
team = 'team'
yourTeam = team + (str(yourPick))
currentTeam = team+ (str(teamNumber))

teams = {"team1":[],"team2":[],"team3":[],"team4":[],"team5":[],"team6":[],"team7":[],"team8":[], "team9":[],    "team10":[],    "team11":[],"team12":[]}
teamsP = {"team1":[],"team2":[],"team3":[],"team4":[],"team5":[],"team6":[],"team7":[],"team8":[], "team9":[],    "team10":[],    "team11":[],"team12":[]}
teamCount = len(teams)
selectedPlayers = []
currentPick = 1
currentPlayer = "null"
currentPlayerTemp ="null"
remainingPlayers = {}
playerList = {}
remainingPlayers = players
seeList = 'null'
playerList = dict(list(players.items())[0: 3])
lowRank = 0 - int(yourPick)
highRank = 10
playerRange = 3
currentRound = 1
startPick = 1
endPick =12
thing = 1
while currentRound < 3:
    if currentRound % 2 == 0:
        startPick = int(12)
        endPick = int(1)
        thing = int(-1)
    else:
        startPick = 1
        endPick =12
        thing = 1

    for x in range(startPick,endPick,thing):
        if len(players) <3:
            playerRange = len(players)
            if len(players) == 0:
                break
        else:
            playerRange = 3
        playerList = dict(list(players.items())[0: playerRange])
        currentTeam = team+ (str(teamNumber))
        if currentTeam == yourTeam:
            if currentPick > teamCount:
                seeRank = input('Would you like to see Dave and Jamey players ranked in this range? ')
                if seeRank == 'Y':  
                    print (rank[lowRank:highRank])
            currentPlayerTemp = input('Pick a player: ')
            currentPosition = players.get(currentPlayerTemp)
            while currentPlayerTemp not in players or currentPlayerTemp in selectedPlayers: 
                if currentPlayerTemp in selectedPlayers:
                    seeList = input('Player has already been selected. Would you like to see a list of availble players? Y or N: ')
                elif currentPlayerTemp not in players:
                    seeList = input('Check your spelling. Would you like to see a list of availble players? Y or N: ')
                if seeList == 'Y':
                    print(dict(list(remainingPlayers.items())[0: 10]))
                    currentPlayerTemp = input('Pick a new player: ')
                else:
                    currentPlayerTemp = input('Pick a new player: ')
        else:
            currentPlayerTemp = random.choice(list(playerList))
            currentPosition = players.get(currentPlayer)
            while currentPlayerTemp in selectedPlayers:
                currentPlayerTemp = random.choice(list(playerList))
        currentPlayer = currentPlayerTemp
        currentPosition = players.get(currentPlayer)
        print ('The number',currentPick," pick is ", currentPlayer, " ", currentPosition)

        lowRank += 1
        highRank += 1
        currentPick +=1
        teams[currentTeam].append(currentPlayer)
        teamsP[currentTeam].append(currentPosition)
        selectedPlayers.append(currentPlayer)
        del players[(currentPlayer)]
        if teamNumber >= teamCount:
            teamNumber = 1
            currentRound +=1
            print('The round is ', currentRound)
        else:
            teamNumber +=1

for key, value in teams.items():
    print(key,':', value)


