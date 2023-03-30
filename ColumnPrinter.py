import pandas as pd

from Tracker import Tracker

class ColumnPrinter:

    def __init__(self, path):
        self.tracker = Tracker(path)
        self.listOfValues = []
        self.dictionary = {}

    def printData(self):
        print(self.tracker.getExcel())

    def retrieveDateColumn(self):
       self.tracker.dropFirst18Rows()
       self.tracker.setFirstRowAsHeader()
       #self.listOfValues = self.tracker.retrieveColumnWithDate().values.tolist()
       list = self.tracker.retrieveColumnWithDate().to_list()
       list.pop(0)
       self.dictionary = {}
       for x in list:
        if x in self.dictionary:
            self.dictionary[x] += 1
        else:
            self.dictionary[x] = 1

    def printDictionary(self):
        print(self.dictionary)

    def getListOfValies(self):
        print(self.listOfValues)

    def listToExcel(self):
        pd.DataFrame(self.listOfValues).to_excel('C:\\Users\\kmatysek\\OneDrive - Amadeus Workplace\\Desktop\\output.xlsx', header=False, index=False)

    def dateCounter(self):
        dateDictionary = {}
        for date in self.listOfValues:
            dateDictionary[date].append(date)


