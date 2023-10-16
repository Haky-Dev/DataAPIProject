#5GHaky xhpMDatlPQddXaIoAqs3tqgHNuJY0Q2IwG_3ztonj0WSyeo
# -*- coding: utf-8 -*-
import webbrowser
import urllib.request
import urllib.parse

import json
import os

import http.client

class RiotApiParsing:
    # 초기화 : 서버, Key / PlayerID, AccountID는 함수에서 받아옴.
    def __init__(self):
        self.__Server = "kr.api.riotgames.com"
        self.__ApiKey = "RGAPI-c4416bbb-0596-41ea-abfe-36dded256e90"

    def getPlayerIDByName(self,PlayerName):

        conn = http.client.HTTPSConnection(self.__Server)
        PlayerName = urllib.parse.quote(PlayerName)
        conn.request("GET","/lol/summoner/v4/summoners/by-name/" + PlayerName +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        jsonTempData = json.loads(result)

        return (jsonTempData['id'], jsonTempData['accountId'])
    
    #return dict : Champion Mastery
    def getChampionMasteryByPlayerID(self, PlayerID):
                
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/champion-mastery/v4/champion-masteries/by-summoner/" + PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    #return dict : Player Ranking(League)
    def getPlayerLeagueByPlayerID(self, PlayerID):
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/league/v4/entries/by-summoner/" + PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    #return dict : Playing Game
    def getPlayingGameByPlayerID(self):
        conn = http.client.HTTPSConnection(self.__Server, PlayerID)

        conn.request("GET","/lol/spectator/v4/active-games/by-summoner/" + PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    #return dict : Matchs(Played Games)
    def getMatchsByAccountID(self, AccountID, champion, queue, season = 13, endIndex = 30, beginIndex = 0):
        #champion, queue, season, endIndex, beginIndex
        #queue - Solo : 420, Normal : 430, freeRank : 440, ARAM : 450
        
        conn = http.client.HTTPSConnection(self.__Server)
        filterOptions = "?"
        if champion != None:
            filterOptions += 'champion=' + str(champion) + '&'
        if queue != None:
            filterOptions += 'queue=' + str(queue) + '&'
        filterOptions += 'season=' + str(season) + '&endIndex=' + str(endIndex) + '&beginIndex=' + str(beginIndex)  + '&'
        conn.request("GET","/lol/match/v4/matchlists/by-account/" + AccountID + filterOptions + "api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    #return dict : ChmapionsData(name, keyID, title, story...) 
    def getAllChampionsData(self):

        conn = http.client.HTTPSConnection("ddragon.leagueoflegends.com")
        conn.request("GET","/cdn/9.10.1/data/ko_KR/champion.json")
        req = conn.getresponse()
        result = req.read().decode('utf-8')
        jsonTempData = json.loads(result)

        return jsonTempData['data']
         
	#이미지 파일 얻어오는코드
    def getImgByChampionsName(self, championName):
        url = "http://ddragon.leagueoflegends.com/cdn/9.10.1/img/champion/" + championName + ".png"
        #http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Azir_0.jpg

        outPath = "images/"
        outFile = "image_" + championName + ".png"

        if not os.path.isdir(outPath):
            os.makedirs(outPath)

        urllib.request.urlretrieve(url, outPath + outFile)
 # 사용하지 않는 클래스 : 저장 예시  
class Search(RiotApiParsing):

    def __init__(self, PlayerName):
        RiotApiParsing.__init__(self)
        self.getPlayerIDByName(PlayerName)
        self.saveRank(self.getPlayerLeagueByPlayerID())
        self.saveChampionMasteryTop3(self.getChampionMasteryByPlayerID())
        self.saveAllMatches(self.getMatchsByAccountID(None, None))

class championData:
    
    def __init__(self, data):
        #self.__championData = []
        temp = []
        for i in data['data'].items():
            #self.__championData.append(i)
           temp.append(i)
        self.__championData = tuple(temp)

        #for i in range(len(self.__championData)):
            #self.getImgByChampionsName(championData[i][0]) #img 호출 코드
            #print(self.__championData[i][0])
    def getChampionNames(self):
        temp = []
        for i in range(len(self.__championData)):
            temp.append(self.__championData[i][0])
        return temp

    def printChampionData(self):
        for i in self.__championData:
            print(i)


