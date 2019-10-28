import csv

class File_reader:
    def __init__(self):
        self.allinputdata = [] 


    def read_csv(self, csvfile):
        with open(csvfile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.allinputdata.append() 
