from matplotlib import pyplot
from openpyxl import load_workbook

DataFile = load_workbook("C:\\Users\\Dre\\Seafile\\p4ne_training\\data_analysis_lab.xlsx")
Sheet = DataFile['Data']


def getvalue(x): return x.value


Years = list(map(getvalue, Sheet['A'][1:]))
Temperature = list(map(getvalue, Sheet['C'][1:]))
Activity = list(map(getvalue, Sheet['D'][1:]))

pyplot.plot(Years, Temperature, label="Temperature")
pyplot.plot(Years, Activity, label="Activity")

pyplot.show()
