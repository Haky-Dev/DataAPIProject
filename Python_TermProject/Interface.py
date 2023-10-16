from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from gmail import *

from API_Parsing import *
from DB import *
import random

#import GUI

class Interface:
    def __init__(self):
        self.__db = DB()
        self.__psEngine = RiotApiParsing()
        self.__db.setChampionData(self.__psEngine.getAllChampionsData())

        self.window = Tk()
        #window.geometry("500x1100+100+100")
        self.window.resizable(False, False)

        #<<<<<<<<<imgList>>>>>>>>>>>>
        self.imgChampionDict = {}
        self.imgTierDict = {}
        TierList = ['BRONZE','CHALLENGER','DIAMOND','GOLD','GRANDMASTER','IRON','MASTER','PLATINUM','SILVER']
        
        for i in self.__db.ChampionIDDict.items():
            self.imgChampionDict[i[0]] = PhotoImage(file = 'images/image_'+ i[1] +'.gif')

        for i in TierList:
            self.imgTierDict[i] = PhotoImage(file='tierImg/'+ i +'.gif')

        self.window.title("League Of Legends Search")

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame1>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame1 = Frame(self.window, borderwidth = 2, width = 500, height = 100, relief = 'solid')
        self.Frame1.grid(row = 0, column = 0)
        
        #class 상속으로 구현
        F1_Font = Font(size = 15)
        
        playerButton = Button(self.Frame1, text = "플레이어", width = 20)
        playerButton.pack(side = "left", fill = "x", padx = 5)

        inGameButton =  Button(self.Frame1, text = "인게임", width = 20)
        inGameButton.pack(side = "left", fill = "x", padx = 5)

        subFuncButton = Button(self.Frame1, text = "부가기능", width = 20, command = self.Btn_SubFunc)
        subFuncButton.pack(side = "left", fill = "x", padx = 5)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame2>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame2 = Frame(self.window, borderwidth = 2, width = 500, height = 1000, relief = 'solid')
        self.Frame2.grid(row = 1, column = 0)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame3>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame3 = Frame(self.Frame2, width = 500, height = 500, relief = 'solid')
        self.Frame3.grid(row = 0, column = 0)

        self.F2_SearchEntry = Entry(self.Frame3, text = "플레이어 이름", width = 50)
        self.F2_SearchEntry.bind("<Return>", self.Btn_Search) #엔터 입력시 함수 실행.
        self.F2_SearchEntry.grid(row = 0, column = 0)
        

        searchButton = Button(self.Frame3, text = "검색", width = 10, command = self.Btn_Search)
        searchButton.grid(row = 0, column = 1)  

        #<<<<<<<<<<<<<<<<<<<<<<<<<<FramePlayerInfo>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.FramePlayerInfo = Frame(self.Frame3, width = 500, height = 300, relief = 'solid')
        self.FramePlayerInfo.grid(row = 1, column = 0, columnspan = 2)

        self.tierFrame = Frame(self.FramePlayerInfo, relief = 'solid')
        self.tierFrame.pack(side = 'left')
        self.mostFrame = Frame(self.FramePlayerInfo, relief = 'solid')
        self.mostFrame.pack(side = 'right')

            #<<<<<<<<<<<<<<<<<<<<<<<<tierLabelLIst>>>>>>>>>>>>>>>>>>>>>>>
        self.tierLabelList = []
        self.tierLabelList.append(Label(self.tierFrame, image = self.imgTierDict['CHALLENGER']))
        self.tierLabelList.append(Label(self.tierFrame, text = 'QueueType'))
        self.tierLabelList.append(Label(self.tierFrame, text = 'Tier'))
        self.tierLabelList.append(Label(self.tierFrame, text = 'Rank'))
        self.tierLabelList.append(Label(self.tierFrame, text = "LP"))
        for i in self.tierLabelList:
            i.pack(side = 'top')
            #<<<<<<<<<<<<<<<<<<<<<<<<mostLabelLIst>>>>>>>>>>>>>>>>>>>>>>>
        
        self.mostLabelList = []
        for i in range(3):
            self.mostLabelList.append(Label(self.mostFrame, text = 'Point', image = self.imgChampionDict[1], compound = 'top'))
            self.mostLabelList[i].pack(side = 'left', padx = 2)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame4>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame4 = Frame(self.Frame2, width = 500, height = 500, relief = 'solid')#
        self.Frame4.grid(row = 1, column = 0)


        #<<<<<<<<<<<<<<<<<<<<<<<<<<FrameTab>>>>>>>>>>>>>>>>>>>>>>>>>>
        notebook = tkinter.ttk.Notebook(self.Frame4)
        FrameTab_entire = Canvas(self.Frame4, bg = 'white', width = 500, height = 300)
        FrameTab_soloRank = Frame(self.Frame4, width = 500, height = 300)
        FrameTab_normal = Frame(self.Frame4, width = 500, height = 300)
        FrameTab_ARAM = Frame(self.Frame4, width = 500, height = 300)
        FrameTab_freeRank = Frame(self.Frame4, width = 500, height = 300)
        
        notebook.add(FrameTab_entire, text="전체") 
        notebook.add(FrameTab_soloRank, text="솔랭") 
        notebook.add(FrameTab_normal, text="일반") 
        notebook.add(FrameTab_ARAM, text="칼바람") 
        notebook.add(FrameTab_freeRank, text="자유랭")
        #notebook.bind_all("<<NotebookTabChanged>>", self.tabChangedEvent) 
        notebook.pack()

        self.window.mainloop()

#<<<<<<<<<<<EVENT>>>>>>>>>>
    def Btn_EmailSend(self):
        recipientAddr = self.SF_Entry.get()
        mail_service = Mail_Service()
        mail_service.send_to_massage(recipientAddr, "전적 전송", str(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(),None,None)))
        print('완료')

    def Btn_DrawGraph(self):
        graphWindow = Toplevel(self.subFuncWindow)
        
        Matches = self.__db.getMatches()
        print(Matches)

        graphData = {}
        for i in Matches:
            if i[1] in graphData:
                graphData[i[1]] += 1
            else:
                graphData[i[1]] = 1
        print(graphData)
        value = graphData.values()
        maxCount = int(max(value))

        Width = 500
        Height = 300
        graphCanvas = Canvas(graphWindow, width = Width, height = Height, bg = 'white')
        graphCanvas.pack()
        graphCanvas.create_line(10, Height - 10, Width - 10, Height - 10)
        barW = (Width - 20) / len(graphData)
        graphData = list(graphData)
        value = list(value)
        for i in range(len(graphData)):
            graphCanvas.create_rectangle(i * barW + 10, Height - (Height - 20) * value[i] / maxCount,
                   (i + 1) * barW+10, Height - 10, fill = 'yellow', tags = "grim")
            graphCanvas.create_text(i*barW + 10 + 20, Height - 10+5, text = self.__db.chp_getIDtoName(graphData[i]), tags = "grim")
            graphCanvas.create_text(i*barW + 10 + 20, Height - (Height - 20) * value[i] / maxCount - 5,
                                   text = str(value[i]), tags = "grim")
        

    def Btn_SubFunc(self):
        self.subFuncWindow = Toplevel(self.window)
        self.subFuncWindow.geometry("200x100")
        Label(self.subFuncWindow, text = '전적 정보 이메일 전송',).pack(side = 'top')
        self.SF_Entry = Entry(self.subFuncWindow)
        self.SF_Entry.pack(side = 'top', fill = 'x')
        Button(self.subFuncWindow, text = "이메일 전송", command = self.Btn_EmailSend).pack(side = 'top', fill = "x")
        Button(self.subFuncWindow, text = "현재 전적 Champion Graph 출력", command = self.Btn_DrawGraph).pack(side = 'top', fill = "x")


    def Btn_Search(self, event = None):
        name = self.F2_SearchEntry.get()
        ID, AccountID = self.__psEngine.getPlayerIDByName(name)
        self.__db.setName(name)
        self.__db.setID((ID, AccountID))
        self.__db.setRank(self.__psEngine.getPlayerLeagueByPlayerID(ID))
        self.__db.setMasteryTop3(self.__psEngine.getChampionMasteryByPlayerID(ID))
        self.__db.setMatches(self.__psEngine.getMatchsByAccountID(AccountID, None, None))
        self.update_Search()

#<<<<<<<<<<<UPDATE>>>>>>>>>>

    def update_Search(self):
        #RANK DRAW
        rank = self.__db.getRank()       
        most = self.__db.getMastery()
        
        self.tierLabelList[0].configure(image = self.imgTierDict[rank[0][1]])
        self.tierLabelList[1].configure(text = rank[0][0])
        self.tierLabelList[2].configure(text = rank[0][1])
        self.tierLabelList[3].configure(text = rank[0][2])
        self.tierLabelList[4].configure(text = rank[0][3])

        for i in range(len(most)):
            self.mostLabelList[i].configure(image = self.imgChampionDict[most[i][0]], text = str(most[i][2]) + 'Pt')

            

Interface()