import csv

class File_reader:
    def __init__(self, sourcefile):
        self.sourcefile = sourcefile
        self.allinputdata = [] 


    def read_csv(self):
        with open(self.sourcefile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.allinputdata.append() 
