#Documentation de l'API Blaseball: https://docs.sibr.dev/docs/apis/docs/index.md
#Avoir le paquet requests
#Avoir les variables PATH d'Anaconda3 en place

import requests
import json

#Fonctions de requête

#Equipes
def getAllTeams():
    #(?)
    response = requests.get('https://sibr.stoplight.io/mocks/sibr/apis/2368896/database/allTeams')
    return response

def getTeamDetails(id):
    #Obtenir les stats d'une équipe spécifique
    response = requests.get('https://www.blaseball.com/database/team?id=' + id)
    return response

#Joueurs
def getAllPlayers():
    #Tous les joueurs dont nous avons conaissance
    response = requests.get('https://api.sibr.dev/chronicler/v1/players')
    return response

def getPlayerStats(id):
    #Obtenir les stats d'un joueur spécifique
    response = requests.get('https://www.blaseball.com/database/players?ids=' + id)
    return response

def getIncerated():
    #Avoir l'ID des incinérés avec compteur de peanuts (?)
    response = requests.get('https://www.blaseball.com/api/getTribute')
    return response

#Parties
def getGamesId(id):
    #Obtenir les infos d'une partie avec son ID
    response = requests.get('https://www.blaseball.com/database/gameById/' + id)
    return response

def getGamesId(season, day):
    #Obtenir les infos d'une partie avec sa saison et le jour
    response = requests.get('https://www.blaseball.com/database/games?season=' + season + 'day=' + day)
    return response

# Créer un print au format lisible json
def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

g = getTeamDetails('878c1bf6-0d21-4659-bfee-916c8314d69c')
jprint(g.json())
