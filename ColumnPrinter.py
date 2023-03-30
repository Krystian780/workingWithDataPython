from Tracker import Tracker

class ColumnPrinter:

    def __init__(self, path):
        self.tracker = Tracker(path)

    def printData(self):
        print(self.tracker.getExcel())

    def printDateColumn(self):
       self.tracker.dropFirst18Rows()
       self.tracker.setFirstRowAsHeader()
       self.tracker = self.tracker.retrieveColumnWithDate()
       print(self.tracker)

