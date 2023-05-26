import pandas as pd

class Tracker:

    def __init__(self, filePath, sheet):
        self.excelFile = pd.read_excel(filePath, sheet)

    def printExcel(self):
        print(self.excelFile)

    def printHeaders(self):
        print(self.excelFile.head())

    def removeIndex(self):
        dataframe = self.excelFile
        self.excelFile = dataframe.reset_index(drop=True)

    def dropFirsAndThirdColumn(self):
        self.excelFile.drop(columns=self.excelFile.columns[0],
                axis=1,
                inplace=True)
        self.excelFile.drop(columns=self.excelFile.columns[1],
                            axis=1,
                            inplace=True)

    def dropFirst18Rows(self):
        dataframe = self.excelFile
        self.dropFirsAndThirdColumn()
        self.excelFile = dataframe.iloc[16:]

    def dropFirstRow(self):
        dataframe = self.excelFile
        self.excelFile = dataframe.iloc[1:]

    def getDataFrame(self):
        return self.excelFile

    def setFirstRowAsHeader(self):
        self.excelFile.columns = self.excelFile.iloc[0]

    def dropIndex(self):
        df = self.excelFile
        df = df.reset_index(drop=True)
        self.excelFile = df

    def getColumnNames(self):
        return self.excelFile.columns.values

    def printDataType(self):
        print(type(self.excelFile))

    def retrieveFrance(self):
        return self.excelFile.loc[self.excelFile['Shipping Country'] == 'France']
    def toExcel(self):
        self.excelFile.to_excel('C:\\Users\\output.xlsx')

    def retrieveDateColumnFromSalesForce(self):
        return self.excelFile["Date"]

    def retrieveDateColumnFromFrenchTracker(self):
        return self.excelFile["Received date"]

    def convertToList(self):
        return self.excelFile.to_list()

    def printDataType(self):
        print(self.excelFile.dtypes)
