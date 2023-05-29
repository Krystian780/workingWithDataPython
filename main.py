from Tracker import Tracker
from DateOccurenceCounter import DateOccurenceCounter

dateOccurencesRetriever = DateOccurenceCounter("C:\\Users\\kmatysek\\OneDrive - Amadeus Workplace\\Desktop\\OPEN ACTIVITIES WEMEA RM-2023-03-10-11-30-30.xlsx", "C:\\Users\\kmatysek\\OneDrive - Amadeus Workplace\\Desktop\\FrenchTracker.xlsx")
dateOccurencesRetriever.retrieveFrenchDatesFromSalesForce()
dateOccurencesRetriever.dateOccurenceSalesForce()
dateOccurencesRetriever.convertStringToDateFormatForGivenList("salesForce")
dateOccurencesRetriever.printEverything()
print("sharepointtt")
dateOccurencesRetriever.retrieveFrenchDates()
dateOccurencesRetriever.dateOccurenceSharePoint()
dateOccurencesRetriever.printsadasdas()
dateOccurencesRetriever.concatenateTwoDictionaries()
dateOccurencesRetriever.moveExcelToDictionary()

