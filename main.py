from Tracker import Tracker
from DateOccurencesRetriever import DateOccurencesRetriever

dateOccurencesRetriever = DateOccurencesRetriever("C:\\Users\\kmatysek\\OneDrive - Amadeus Workplace\\Desktop\\OPEN ACTIVITIES WEMEA RM-2023-03-10-11-30-30.xlsx", "C:\\Users\\kmatysek\\OneDrive - Amadeus Workplace\\Desktop\\FrenchTracker.xlsx")
dateOccurencesRetriever.retrieveFrenchDatesFromSalesForce()
dateOccurencesRetriever.countDateOccurencesFromSalesForce()
dateOccurencesRetriever.convertListOfStringsToDate("salesForce")
dateOccurencesRetriever.printEverything()
print("sharepointtt")

