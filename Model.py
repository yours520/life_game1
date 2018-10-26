import random
import numpy
import profile
from time import sleep
from threading import Timer


class Model():

    def __init__(self, map_rows=38, map_cols=38):
        '''地图将在逻辑模块进行初始化'''
        self.numRows = map_rows
        self.numCols = map_cols
        self.map = numpy.zeros((map_rows, map_cols), dtype=numpy.int)

        for i in range(map_cols):
            for j in range(map_rows):
                self.map[i][j] = random.randint(0, 1)

        pass

    def get_neighbor_count(self, map, row, col):
        '''地图上一个方格周围的活细胞数'''
        x = [-1, 0, 1, -1, 1, -1, 0, 1]
        y = [1, 1, 1, 0, 0, -1, -1, -1]
        count = 0
        for i in range(8):
            newX = row + x[i]
            newY = col + y[i]
            if newX >= 0 and newY >= 0 and newX < self.numCols and newY < self.numRows:
                if map[newX][newY] == 1:
                    count = count + 1
        return count
        pass

    def updateMap(self):
        '''更新地图信息'''

        oldMap = list()
        oldMap = [[self.map[i][j] for j in range(self.numCols)] for i in range(self.numRows)]
        for i in range(self.numRows):
            for j in range(self.numCols):
                # 获取周围细胞的活细胞数目
                neighbor_count = self.get_neighbor_count(oldMap, i, j)
                if neighbor_count == 3:
                    self.map[i][j] = 1
                elif neighbor_count != 2:
                    self.map[i][j] = 0
        pass
