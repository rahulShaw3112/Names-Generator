import csv
import random

class DataSource:
    def __init__(self, fileName = 'names.csv'):
        self.firstNames = []
        self.lastNames = []
        self.records = 0
        self.fileName = fileName
        self.processRawData()

    def processRawData(self):
        with open(self.fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.firstNames.append(row[0])
                self.lastNames.append(row[1])
                line_count += 1
            self.records = line_count
            return self.records

    def getFirstNames(self):
        return self.firstNames

    def getLastNames(self):
        return self.lastNames

    def getRandomFirstName(self):
        return random.choice(self.firstNames)

    def getRandomLastName(self):
        return random.choice(self.lastNames)
