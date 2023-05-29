from Tracker import Tracker
from datetime import datetime
import pandas as pd
class DateOccurenceCounter:
    def __init__(self, pathToSalesForceTracker, pathToFrenchTracker):
        self.salesForceTracker = Tracker(pathToSalesForceTracker, "OPEN ACTIVITIES WEMEA RM")
        self.sharePointTracker = Tracker(pathToFrenchTracker, "ORDERING")
        self.dateOccurenceSalesForce = {}
        self.dateOccurenceSharePoint = {}
        self.allDatesSalesForce = []
        self.allDatesSharePoint = []
        self.filteredDatesSharePoint = []
        self.filteredDatesSharePoint = {}
        self.mergedDictionaryValuesByKey = {}

    def retrieveFrenchDatesFromSalesForce(self):
        self.salesForceTracker.dropFirst18Rows()
        self.salesForceTracker.setFirstRowAsHeader()
        self.salesForceTracker.dropFirstRow()
        self.salesForceTracker.resetIndex()
        self.salesForceTracker.printDateFromTracker()
        self.salesForceTracker = self.salesForceTracker.retrieveFrance()
        self.salesForceTracker = self.salesForceTracker["Date"]

    def countDateOccurencesSalesForce(self):
        listOfDates = self.salesForceTracker.to_list()
        for date in listOfDates:
            if date in self.dateOccurenceSalesForce:
               self.dateOccurenceSalesForce[date] += 1
            else:
                self.dateOccurenceSalesForce[date] = 1

    def returnTheEarliestDateSalesForce(self):
        return min(self.allDatesSalesForce)

    def retrieveFrenchDates(self):
        self.sharePointTracker = self.sharePointTracker.retrieveColumnCalledReceivedDate()

    def countDateOccurencesSharePointTracker(self):
        listOfDates = self.sharePointTracker.to_list()
        earliestDate = self.returnTheEarliestDateSalesForce()
        for date in listOfDates:
         try:
            dateFormat = "%d.%m.%Y"
            dateTime = datetime.strptime(date, dateFormat)
            if dateTime >= earliestDate:
                date = dateTime.strftime("%d/%m/%Y")
                if date in self.dateOccurenceSharePoint:
                    self.dateOccurenceSharePoint[date] += 1
                else:
                    self.dateOccurenceSharePoint[date] = 1
            else:
                continue
         except:
             pass

    def getDatesWithoutDuplicates(self, listName):
        if(listName == "salesForce"):
            return self.dateOccurenceSalesForce.keys()
        else:
            return self.dateOccurenceSharePoint.keys()

    def convertStringToDateFormatForGivenList(self, listName):
        listOfDates = self.getDatesWithoutDuplicates(listName)
        keys = [key for key in listOfDates]
        if (listName == "salesForce"):
            dateFormat = "%d/%m/%Y"
        else:
            dateFormat = "%d.%m.%Y"
        for key in keys:
            try:
                if (listName == "salesForce"):
                    self.allDatesSalesForce.append(datetime.strptime(key, dateFormat))
                else:
                    self.allDatesSharePoint.append(datetime.strptime(key, dateFormat))
            except:
                pass
    def returnListOfDatesFromSalesForce(self, listName):
        self.convertStringToDateFormatForGivenList(listName)
    def returnListOfDatesFromSharePoint(self, listName):
        self.convertStringToDateFormatForGivenList(listName)

    def retrieveOnlyLaterThanGivenDate(self):
        date = self.returnTheEarliestDateSalesForce()
        for d in self.allDatesSharePoint:
            if d >= date:
                self.filteredDatesSharePoint.append(d)

    def countDateOccurenceFilteredSharePoint(self):
        for date in self.filteredDatesSharePoint:
            date = date.strftime("%d/%m/%Y")
            if date in self.filteredDatesSharePoint:
               self.filteredDatesSharePoint[date] += 1
            else:
                self.filteredDatesSharePoint[date] = 1

    def concatenateTwoDictionaries(self):
        for key in self.dateOccurenceSalesForce:
            if key in self.dateOccurenceSharePoint:
                valueSalesForce = str(self.dateOccurenceSharePoint.get(key))
                valueSharePoint = str(self.dateOccurenceSalesForce.get(key))
                concatenatedString = valueSalesForce + " " + valueSharePoint
                self.mergedDictionaryValuesByKey[key] = concatenatedString

    def moveExcelToDictionary(self):
        df = pd.DataFrame(data=self.mergedDictionaryValuesByKey, index=[1])
        df.to_excel("C:\\Users\\output.xlsx", index=False)
