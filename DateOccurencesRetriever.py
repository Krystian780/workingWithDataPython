from Tracker import Tracker
from datetime import datetime
import pandas as pd
class DateOccurencesRetriever:
    def __init__(self, salesForcePath, frenchTrackerPath):
        self.ordersFromSalesForce = Tracker(salesForcePath, "OPEN ACTIVITIES WEMEA RM")
        self.ordersFromFrenchTracker = Tracker(frenchTrackerPath, "ORDERING")
        self.FrenchOccurencesSalesForce = {}
        self.FrenchOccurencesSharePoint = {}
        self.frenchDatesSalesForce = []
        self.frenchDatesSharePoint = []

    def retrieveFrenchDatesFromSalesForce(self):
        self.ordersFromSalesForce.dropFirst18Rows()
        self.ordersFromSalesForce.setFirstRowAsHeader()
        self.ordersFromSalesForce.dropFirstRow()
        self.ordersFromSalesForce.removeIndex()
        self.ordersFromSalesForce.printExcel()
        self.ordersFromSalesForce = self.ordersFromSalesForce.retrieveFrance()
        self.ordersFromSalesForce = self.ordersFromSalesForce["Date"]

    def countDateOccurencesFromSalesForce(self):
        listOfDates = self.ordersFromSalesForce.to_list()
        for date in listOfDates:
            if date in self.FrenchOccurencesSalesForce:
               self.FrenchOccurencesSalesForce[date] += 1
            else:
                self.FrenchOccurencesSalesForce[date] = 1

    def printTheEarliestDate(self):
        self.returnListOfDatesFromSalesForce("salesForce")

    def returnTheEarliestDate(self):
        return min(self.frenchDatesSalesForce)

    def printEverything(self):
        print("French Occurences")
        print(self.FrenchOccurencesSalesForce)
        print("French Dates SalesFoce")
        print(self.frenchDatesSalesForce)
        print("earsliest date")
        print(self.returnTheEarliestDate())
#########################################################################
#########################################################################
#########################################################################
#########################################################################
    def retrieveFrenchDatesFromSharePoint(self):
        self.ordersFromFrenchTracker = self.ordersFromFrenchTracker.retrieveDateColumnFromFrenchTracker()
        list = self.ordersFromFrenchTracker.to_list
        print(type(list))
        dataframe = self.ordersFromFrenchTracker
        print(dataframe.dtypes)

    def countDateOccurencesSharePoint(self):
        listOfDates = self.ordersFromFrenchTracker.to_list()
        for date in listOfDates:
            if date in self.FrenchOccurencesSharePoint:
               self.FrenchOccurencesSharePoint[date] += 1
            else:
                self.FrenchOccurencesSharePoint[date] = 1

    def getDatesWithoutDuplicates(self, listName):
        if(listName == "salesForce"):
            return self.FrenchOccurencesSalesForce.keys()
        else:
            return self.FrenchOccurencesSharePoint.keys()

    def convertListOfStringsToDate(self, listName):
        listOfDates = self.getDatesWithoutDuplicates(listName)
        print("list of dates")
        print(len(listOfDates))
        keys = [key for key in listOfDates]
        if (listName == "salesForce"):
            dateFormat = "%d/%m/%Y"
        else:
            dateFormat = "%d.%m.%Y"

        for key in keys:
            try:
                if (listName == "salesForce"):
                    self.frenchDatesSalesForce.append(datetime.strptime(key, dateFormat))
                else:
                    self.frenchDatesSharePoint.append(datetime.strptime(key, dateFormat))
            except:
                pass
    def returnListOfDatesFromSalesForce(self, listName):
        self.convertListOfStringsToDate(listName)
    def returnListOfDatesFromSharePoint(self, listName):
        self.convertListOfStringsToDate(listName)

    def printEverything(self):
        print("French Occurences")
        print(self.FrenchOccurencesSharePoint)
        print("French Dates SalesFoce")
        print(self.frenchDatesSharePoint)
        print("earsliest date")
        print(self.returnTheEarliestDate())


#z trackera wyciagnac tylko te daty ktore sa pozniej badz rowne najmniejszej dacie
#porownac dwie daty loop
# ustaw pierwszy rzad jako header