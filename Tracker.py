import pandas as pd

class Tracker:

    def __init__(self, filePath):
        self.excelFile = pd.read_excel(filePath)

    def printDataFrame(self):
        print(self.excelFile)

    def printHeaders(self):
        print(self.excelFile.head())

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

    def getExcel(self):
        return self.excelFile

    def setFirstRowAsHeader(self):
        self.excelFile.columns = self.excelFile.iloc[0]

    def dropIndex(self):
        df = self.excelFile
        df = df.reset_index(drop=True)
        self.excelFile = df

    def getColumnNames(self):
        return self.excelFile.columns.values

    def retrieveColumnWithDate(self):
        return self.excelFile["Date"]

    def printDataType(self):
        print(type(self.excelFile))


