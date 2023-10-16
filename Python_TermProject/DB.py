class DB:
    def __init__(self):
        self.__playerName = ''
        self.__PlayerID = ''
        self.__AccountID = ''

        self.rawChampion = {}
        self.ChampionIDDict = {}
        self.__Rank = []
        self.__Mastery = []
        self.__Matches = []

#<<<<<<<<<<<<<<<Set>>>>>>>>>>>>>>>
    def setChampionData(self, data):
        self.rawChampion = data
        data = data.items()
        for i in data:
            self.ChampionIDDict[int(i[1]['key'])] = i[0]

    def setName(self, name):
        self.__playerName = name

    def setID(self, IDs):
        self.__PlayerID = IDs[0]
        self.__AccountID = IDs[1]

    def setRank(self, data):
        self.__Rank = []
        for i in range(len(data)):#queueType, tier, rank, point, wins, losses
            tempData = (data[i].get('queueType'),
                        data[i].get('tier'),
                        data[i].get('rank'),
                        data[i].get('leaguePoints'),
                        data[i].get('wins'),
                        data[i].get('losses'))
            self.__Rank.append(tempData)

    def setMasteryTop3(self, data):
        self.__Mastery = []
        for i in range(3):
            tempData = (data[i].get('championId'),
                        data[i].get('championLevel'),
                        data[i].get('championPoints'))
            self.__Mastery.append(tempData)
        
    def setMatches(self, data):
        data = data.get('matches')
        self.__Matches = []
        for i in range(len(data)):
            tempData = (data[i].get('gameId'),
                        data[i].get('champion'),
                        data[i].get('queue'))
            self.__Matches.append(tempData)

#<<<<<<<<<<<<<<<Get>>>>>>>>>>>>>>>

    def getName(self):
        return self.__playerName
    
    def getPlayerID(self):
        return self.__PlayerID
    
    def getAccountID(self):
        return self.__AccountID

    def getRank(self):
        return self.__Rank

    def getMastery(self):
        return self.__Mastery

    def getMatches(self):
        return self.__Matches

    def chp_getIDtoName(self, id):
        return self.ChampionIDDict[int(id)]
