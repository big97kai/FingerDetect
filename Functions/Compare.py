'''
    @FileName:Compare.py
    @Author:yikai yang
    @Date:2023/5/22
    @Desc:Null
'''
from PySide6.QtCharts import QLineSeries, QtCharts, QChart
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Compare():
    def __init__(self):
        self.firstModelTime = []
        self.secondModelTime = []
        self.firstCorretRate = []
        self.secondCorrenctRate = []

    def getFirstModelTime(self):
        return self.firstModelTime

    def getSocondModelTime(self):
        return self.secondModelTime

    def getFirstCorrectRate(self):
        return self.firstCorretRate

    def getSecondCorrentRate(self):
        return self.secondCorrenctRate

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

        chart = QChart()
        series_1 = QLineSeries()
        series_2 = QLineSeries()
        times = 0
        max_y1 = 0
        max_y2 = 0
        first_series = None
        second_series = None
        if boole:
            first_series = self.firstModelTime
            second_series = self.secondModelTime
            chart.setTitle("Model Time.")

        else:
            first_series = self.firstCorretRate
            second_series = self.secondCorrenctRate
            chart.setTitle("Mode Correct Rate.")

        for plot in first_series:
            series_1.append((times, plot))
            max_y1 = max(plot, max_y1)
            times += 1

        times = 0
        for plot in second_series:
            series_2.append((times, plot))
            max_y2 = max(plot, max_y2)
            times += 1

        chart.addSeries(series_1)
        chart.addSeries(series_2)
        # Create the X-axis
        # Create the X-axis
        axisX = QtCharts.QValueAxis()
        axisX.setRange(0, times)  # Set the range for the X-axis
        chart.addAxis(axisX, QtCharts.QtOrientation.Horizontal)  # Attach X-axis to the chart
        series_1.attachAxis(axisX)  # Attach X-axis to series1
        series_2.attachAxis(axisX)  # Attach X-axis to series2

        # Create the Y-axis for series1
        axisY1 = QtCharts.QValueAxis()
        axisY1.setRange(0, max_y1)  # Set the range for the Y-axis of series1
        chart.addAxis(axisY1, QtCharts.QtOrientation.Vertical)  # Attach Y-axis to the chart
        series_1.attachAxis(axisY1)  # Attach Y-axis to series1

        # Create the Y-axis for series2
        axisY2 = QtCharts.QValueAxis()
        axisY2.setRange(0, max_y2)  # Set the range for the Y-axis of series2
        chart.addAxis(axisY2, QtCharts.QtOrientation.Vertical)  # Attach Y-axis to the chart
        series_2.attachAxis(axisY2)  # Attach Y-axis to series2

        # Create a QChartView to display the chart
        chart_view = QtCharts.QChartView(chart)

        return chart_view
