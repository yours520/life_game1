import tkinter as tk
import Model
import RepeatableTimer


class GUI:
    def __init__(self):
        # self.initWindow()
        self.window = tk.Tk()
        # 使窗口居中
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        ww = 800
        wh = 800
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.window.title('生命游戏')
        self.addMenu()
        self.model = Model.Model()
        # self.drawMap(self.model.map,self.model.numRows,self.model.numCols)
        self.canvas = tk.Canvas(self.window, height=5000, width=5000)
        self.window.mainloop()

    # 加入菜单
    def addMenu(self):
        # 创建一个菜单栏
        menubar = tk.Menu(self.window)
        # 定义一个空菜单单元
        gamemenu = tk.Menu(menubar, tearoff=0)
        # 将上面定义的空菜单命名 ,放在菜单栏中，就是装入那个容器中
        menubar.add_cascade(label='Game', menu=gamemenu)
        # 在Game 中加入菜单
        gamemenu.add_command(label='Start', command=self.startGame)
        # 改变window参数 将menubar加入window
        self.window.config(menu=menubar)

    def initMap(self):
        canvas = tk.Canvas(self.window, height=5000, width=5000)
        x0, y0, x1, y1 = 20, 20, 20 + 20, 20 + 20
        self.num = []
        for row in range(38):
            for col in range(38):
                t = canvas.create_rectangle(x0, y0, x1, y1, fill='white')
                x0 = x0 + 20
                x1 = x1 + 20
            y0 = y0 + 20
            y1 = y1 + 20
            x0 = 20
            x1 = x0 + 20
        canvas.pack()

    def drawMap(self, map, num_of_rows=38, num_of_cols=38):
        #  self.canvas.delete(self.canvas)
        x0, y0, x1, y1 = 20, 20, 20 + 20, 20 + 20
        self.canvas.create_rectangle(0, 0, 5000, 5000, fill="#fff", outline="#fff")
        for row in range(38):
            for col in range(38):
                if map[row][col] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='black', outline='white')
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='white')
                x0 = x0 + 20
                x1 = x1 + 20
            y0 = y0 + 20
            y1 = y1 + 20
            x0 = 20
            x1 = x0 + 20
        self.canvas.pack()
        pass

    def job(self):

        self.drawMap(self.model.map)
        self.model.updateMap()
        t = Model.Timer(0, self.job)
        t.start()

    def startGame(self):
        a = RepeatableTimer.RepeatableTimer(0, self.job)
        a.start()
