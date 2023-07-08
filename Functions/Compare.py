'''
    @FileName:Compare.py
    @Author:yikai yang
    @Date:2023/5/22
    @Desc:Null
'''
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure


class Compare():
    def __init__(self):
        self.firstModelTime = []
        self.secondModelTime = []
        self.firstCorretRate = []
        self.secondCorrenctRate = []

    def addFirstModelTime(self, time):
        self.firstModelTime.append(time)

    def addSocondModelTime(self, time):
        return self.secondModelTime.append(time)

    def addFirstCorrectRate(self, time):
        return self.firstCorretRate.append(time)

    def addSecondCorrentRate(self, time):
        return self.secondCorrenctRate.append(time)

    def clearAll(self):
        self.firstCorretRate.clear()
        self.secondCorrenctRate.clear()
        self.firstModelTime.clear()
        self.secondModelTime.clear()

    def createPlot(self, boole):

        figure = Figure()

        x = None

        if boole:
            x = range(len(self.firstModelTime))

            subplot1 = figure.add_subplot(1, 2, 1)
            subplot2 = figure.add_subplot(1, 2, 2)  # 1 row, 2 columns, subplot index 2


            subplot1.plot(x, self.firstModelTime, label='FirstModel')
            subplot2.plot(x, self.secondModelTime, label='SecondModel')
            # Set labels and title
            subplot1.set_xlabel('file')
            subplot1.set_ylabel('time')
        else:
            x = range(len(self.firstCorretRate))

            subplot1 = figure.add_subplot(1, 2, 1)
            subplot2 = figure.add_subplot(1, 2, 2)  # 1 row, 2 columns, subplot index 2

            subplot1.plot(x, self.firstCorretRate, label='FirstModel')
            subplot2.plot(x, self.secondCorrenctRate, label='SecondModel')
            # Set labels and title
            subplot1.set_xlabel('file')
            subplot1.set_ylabel('rate')

        canvas = FigureCanvas(figure)

        return canvas
